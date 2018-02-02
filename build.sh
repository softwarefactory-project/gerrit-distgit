#!/bin/sh -ex

VERSION=2.14.6
PLUGIN_BRANCH=stable-2.14
MYSQL_CONNECTOR_BUNDLE=5.1.41
PLUGINS="avatars-gravatar delete-project reviewers-by-blame"

function install_bazel() {
    cat >> /etc/yum.repos.d/bazel.repos <<EOF
[vbatts-bazel]
name=Copr repo for bazel owned by vbatts
baseurl=https://copr-be.cloud.fedoraproject.org/results/vbatts/bazel/epel-7-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://copr-be.cloud.fedoraproject.org/results/vbatts/bazel/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1
EOF
    yum install -y bazel
}

function fetch_gerrit_sources() {
    git clone --recursive https://gerrit.googlesource.com/gerrit
    pushd gerrit
    git checkout v${VERSION}
    git submodule foreach --recursive git checkout v${VERSION}
    popd
}

function fetch_dependencies() {
    [ -f lib/mysql-connector-java-${MYSQL_CONNECTOR_BUNDLE}.jar ] || curl \
        -o lib/mysql-connector-java-${MYSQL_CONNECTOR_BUNDLE}.jar \
        -L https://repo1.maven.org/maven2/mysql/mysql-connector-java/${MYSQL_CONNECTOR_BUNDLE}/mysql-connector-java-${MYSQL_CONNECTOR_BUNDLE}.jar
}

function fetch_plugins() {
    pushd plugins
    for plugin in ${PLUGINS}; do
        [ -d ${plugin} ] || git clone https://gerrit.googlesource.com/plugins/${plugin}
        pushd ${plugin}
            # Do not fail here because some plugin doesn't have stable branch
            git checkout ${PLUGIN_BRANCH} || true
        popd
    done
    popd
}

function fix_var_lib_usage() {
    sed -i 's|if (copy) {|if (false) {|' gerrit-pgm/src/main/java/com/google/gerrit/pgm/init/InitContainer.java
    sed -i \
        -e 's|extract(site.*||' \
        -e 's|chmod(site.*||' \
        -e 's|mkdir(.*||' \
        gerrit-pgm/src/main/java/com/google/gerrit/pgm/init/SitePathInitializer.java
    git commit -a -m "QuickFix read-only /usr/lib dir" && git tag -a -m v${VERSION}-sf v${VERSION}-sf || true
}

# Main functions
function gerrit_prepare() {
    type bazel || install_bazel
    [ -d gerrit ] || fetch_gerrit_sources
}

function gerrit_build() {
    pushd gerrit
    fix_var_lib_usage
    # First build may fail because of incorrect bazel version detection, fix by adding 'return True' in
    # vim /home/centos/.cache/bazel/_bazel_centos/0a7817c27ccc8fb2acf95e4072130a42/external/io_bazel_rules_closure/closure/repositories.bzl +164
    [ -f bazel-bin/release.war ] || bazel build release
    fetch_plugins
    for plugin in ${PLUGINS}; do
        bazel build plugins/${plugin}
    done
    popd
}

function gerrit_install() {
    mkdir -p artifacts/lib artifacts/plugins
    cp gerrit/bazel-bin/release.war artifacts/
    cp gerrit/bazel-bin/plugins/*/*.jar artifacts/plugins/
    rm -f artifacts/plugins/*-class.jar
    pushd artifacts
    fetch_dependencies
    tar czf ../gerrit-${VERSION}.tar.gz *
    popd
}

rm -f gerrit-${VERSION}.tar.gz
gerrit_prepare
gerrit_build
gerrit_install
