#!/bin/sh -ex

VERSION=2.16.8
PLUGIN_BRANCH=stable-2.16
MYSQL_CONNECTOR_BUNDLE=5.1.41
PLUGINS="avatars-gravatar delete-project reviewers-by-blame oauth"

function install_bazel() {
    sudo curl -o /etc/yum.repos.d/bazel.repo https://copr.fedorainfracloud.org/coprs/vbatts/bazel/repo/epel-7/vbatts-bazel-epel-7.repo
    sudo yum install -y bazel
}

function fetch_gerrit_sources() {
    git clone --recursive https://gerrit.googlesource.com/gerrit
    pushd gerrit
    git checkout v${VERSION}
    git submodule foreach --recursive git checkout v${VERSION}
    popd
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
    git am -3 ../0001-QuickFix-read-only-usr-lib-dir.patch ../0001-Add-InitSFUser-method.patch
    TAG=v${VERSION}-sf
    git tag -d ${TAG} || true
    git tag -a -m ${TAG} ${TAG}
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
        bazel build plugins/${plugin}:${plugin}.jar
    done
    popd
}

function gerrit_install() {
    mkdir -p artifacts/lib artifacts/plugins
    cp -f gerrit/bazel-bin/release.war artifacts/
    cp -f gerrit/bazel-genfiles/plugins/*/*.jar artifacts/plugins/
    pushd artifacts
    # This plugin cause a stacktrace on start
    rm -f plugins/gr-delete-repo-static.jar plugins/cm-static.jar
    find ./ -type f -exec chmod 644 {} \;
    tar czf ../gerrit-${VERSION}.tar.gz *
    popd
}

rm -f gerrit-${VERSION}.tar.gz
gerrit_prepare
gerrit_build
gerrit_install
