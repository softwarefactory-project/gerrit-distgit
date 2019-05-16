#!/bin/sh -ex

VERSION=2.14.7
RELEASE=$(grep -e '^Release:' gerrit.spec  | awk '{print $2}' | grep -o '[[:digit:]]\+')
PLUGIN_BRANCH=stable-2.14
MYSQL_CONNECTOR_BUNDLE=5.1.41
PLUGINS="avatars-gravatar reviewers-by-blame oauth delete-project"

function install_bazel() {
    # Always pick the minimal bzl version for this particular gerrit version
    curl -L --output /tmp/bzl_install.sh https://github.com/bazelbuild/bazel/releases/download/0.14.0/bazel-0.14.0-installer-linux-x86_64.sh
    chmod +x /tmp/bzl_install.sh
    sudo /tmp/bzl_install.sh
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
    mkdir -p gf_plugins
    for plugin in ${PLUGINS}; do
       if [ "$plugin" == "avatars-gravatar" ]; then
           prefix="master-"
       else
           prefix=""
       fi
       curl -o gf_plugins/${plugin}.jar -L https://gerrit-ci.gerritforge.com/view/Plugins-${PLUGIN_BRANCH}/job/plugin-${plugin}-bazel-${prefix}${PLUGIN_BRANCH}/lastSuccessfulBuild/artifact/bazel-bin/plugins/${plugin}/${plugin}.jar
    done
}

function apply_patches() {
    git am -3 ../0001-QuickFix-read-only-usr-lib-dir.patch ../0001-Add-InitSFUser-method.patch ../0001-Fix-some-bazel-related-problems.patch
    TAG=v${VERSION}-sf
    git tag -d ${TAG} || true
    git tag -a -m ${TAG} ${TAG}
}

# Main functions
function gerrit_prepare() {
    type /usr/local/bin/bazel || install_bazel
    [ -d gerrit ] || fetch_gerrit_sources
}

function gerrit_build() {
    pushd gerrit
    apply_patches
    # First build may fail because of incorrect bazel version detection, fix by adding 'return True' in
    # vim /home/centos/.cache/bazel/_bazel_centos/0a7817c27ccc8fb2acf95e4072130a42/external/io_bazel_rules_closure/closure/repositories.bzl +164
    [ -f bazel-bin/release.war ] || /usr/local/bin/bazel build --jobs=1 release
    popd
}

function gerrit_install() {
    mkdir -p artifacts/lib artifacts/plugins
    cp -f gerrit/bazel-bin/release.war artifacts/
    cp -f gf_plugins/*.jar artifacts/plugins/
    pushd artifacts
    fetch_dependencies
    find ./ -type f -exec chmod 644 {} \;
    tar czf ../gerrit-${VERSION}-${RELEASE}.el7.tar.gz *
    popd
}

rm -f gerrit-${VERSION}.tar.gz
gerrit_prepare
gerrit_build
fetch_plugins
gerrit_install
