Name:          gerrit
Version:       2.14.7
Release:       2%{?dist}
Summary:       Code review system

License:       APACHE-2
URL:           https://www.gerritcodereview.com
Source0:       https://softwarefactory-project.io/mirrors/gerrit/gerrit-%{version}-%{release}.tar.gz
Source1:       gerrit.service
Source2:       gerrit.sh

BuildRequires: systemd
Requires:      java-1.8.0-openjdk
Requires:      wait4service

%description
Gerrit provides web based code review and repository management for the Git version control system.

%package plugin-commit-message-length-validator
Requires:      gerrit
Summary:       Gerrit commit-message-length-validator plugin

%description plugin-commit-message-length-validator
Gerrit commit-message-length-validator plugin

%package plugin-download-commands
Requires:      gerrit
Summary:       Gerrit download-commands plugin

%description plugin-download-commands
Gerrit download-commands plugin

%package plugin-replication
Requires:      gerrit
Summary:       Gerrit replication plugin

%description plugin-replication
Gerrit replication plugin

%package plugin-reviewnotes
Requires:      gerrit
Summary:       Gerrit reviewnotes plugin

%description plugin-reviewnotes
Gerrit reviewnotes plugin

%package plugin-singleusergroup
Requires:      gerrit
Summary:       Gerrit singleusergroup plugin

%description plugin-singleusergroup
Gerrit singleusergroup plugin

%package plugin-avatars-gravatar
Requires:      gerrit
Summary:       Gerrit avatars-gravatar plugin

%description plugin-avatars-gravatar
Gerrit avatars-gravatar plugin

%package plugin-delete-project
Requires:      gerrit
Summary:       Gerrit delete-project plugin

%description plugin-delete-project
Gerrit delete-project plugin

%package plugin-reviewers-by-blame
Requires:      gerrit
Summary:       Gerrit reviewers-by-blame plugin

%description plugin-reviewers-by-blame
Gerrit reviewers-by-blame plugin

%package plugin-oauth
Requires:      gerrit
Summary:       Gerrit oauth plugin

%description plugin-oauth
Gerrit oauth plugin


%prep
%setup -q -c gerrit-%{version}

%install
install -p -D -m 755 release.war %{buildroot}%{_libdir}/gerrit/release.war
install -p -D -m 644 lib/mysql-connector-java-5.1.41.jar %{buildroot}%{_libdir}/gerrit/lib/mysql-connector-java-5.1.41.jar

install -d -m 755 %{buildroot}%{_libdir}/gerrit/plugins
mv plugins/*.jar %{buildroot}%{_libdir}/gerrit/plugins

install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/gerrit.service
install -p -D -m 755 %{SOURCE2} %{buildroot}%{_libexecdir}/gerrit/gerrit.sh

install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig/
echo "GERRIT_HEAP_LIMIT=2g" > %{buildroot}%{_sysconfdir}/sysconfig/gerrit
install -d -m 755 %{buildroot}%{_sysconfdir}/gerrit
install -d -m 750 %{buildroot}%{_localstatedir}/log/gerrit

install -d -m 755 %{buildroot}%{_sharedstatedir}/gerrit/
install -d -m 755 %{buildroot}%{_sharedstatedir}/gerrit/hooks
ln -s /usr/lib64/gerrit/ %{buildroot}%{_sharedstatedir}/gerrit/bin
ln -s /usr/lib64/gerrit/plugins/ %{buildroot}%{_sharedstatedir}/gerrit/plugins
ln -s %{_localstatedir}/log/gerrit/ %{buildroot}%{_sharedstatedir}/gerrit/logs
ln -s /usr/lib64/gerrit/lib/ %{buildroot}%{_sharedstatedir}/gerrit/lib
ln -s /etc/gerrit/ %{buildroot}%{_sharedstatedir}/gerrit/etc

%pre
# Create users
getent group gerrit >/dev/null || groupadd -r gerrit
getent passwd gerrit > /dev/null || useradd -r -g gerrit \
    -d %{_sharedstatedir}/gerrit -s /sbin/nologin \
    -c "Gerrit service account" gerrit
exit 0

%post
%systemd_post gerrit.service

%preun
%systemd_preun gerrit.service

%postun
%systemd_postun gerrit.service

%files
%{_libdir}/gerrit/release.war
%{_libdir}/gerrit/lib/
%{_libdir}/gerrit/plugins/hooks.jar
%{_sysconfdir}/gerrit
%{_sysconfdir}/sysconfig/gerrit
%{_unitdir}/gerrit.service
%{_libexecdir}/gerrit/gerrit.sh
%attr(0750,gerrit,gerrit) %dir %{_localstatedir}/log/gerrit
%attr(0755,gerrit,gerrit) %dir %{_sharedstatedir}/gerrit
%attr(0755,gerrit,gerrit) %dir %{_sysconfdir}/gerrit
%{_sharedstatedir}/gerrit/*

%files plugin-commit-message-length-validator
%{_libdir}/gerrit/plugins/commit-message-length-validator.jar

%files plugin-download-commands
%{_libdir}/gerrit/plugins/download-commands.jar

%files plugin-replication
%{_libdir}/gerrit/plugins/replication.jar

%files plugin-reviewnotes
%{_libdir}/gerrit/plugins/reviewnotes.jar

%files plugin-singleusergroup
%{_libdir}/gerrit/plugins/singleusergroup.jar

%files plugin-avatars-gravatar
%{_libdir}/gerrit/plugins/avatars-gravatar.jar

%files plugin-delete-project
%{_libdir}/gerrit/plugins/delete-project.jar

%files plugin-reviewers-by-blame
%{_libdir}/gerrit/plugins/reviewers-by-blame.jar

%files plugin-oauth
%{_libdir}/gerrit/plugins/oauth.jar


%changelog
* Thu May 16 2019 Matthieu Huin <mhuin@redhat.com> - 2.14.7-2
- add oauth plugin

* Wed Mar 28 2018 Tristan Cacqueray <tdecacqu@redhat.com> - 2.14.7-1
- Update version to 2.14.7

* Fri Feb 23 2018 Fabien Boucher <fboucher@redhat.com> 2.11.10-3
- Bump JSCH to 0.1.54

* Thu Apr 27 2017 Fabien Boucher <fboucher@redhat.com> 2.11.10-2
- Change gerrit.service mode to 644

* Sun Dec 04 2016 Tristan Cacqueray <tdecacqu@redhat.com> 1.0.2-1
- First (dirty) package
