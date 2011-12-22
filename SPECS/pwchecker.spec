%define debug_package %{nil}

Summary:	A cronjob which reports of users with passwords
Name:		pwchecker
Version:	1.3
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
BuildArch:	noarch
License:	GPLv3
Group:		Applications/System
URL:		https://fedorahosted.org/pwchecker
Source0:	https://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.gz
Requires:	mailx
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This script will email you a daily report about users which have passwords
on your system. Exclude list for users is supported.

%prep
%setup -q -n pwchecker-%{version}

%build

%install
rm -rf %{buildroot}
%{__install} -D -p -m 0755 cron.daily/pwchecker %{buildroot}/%{_sysconfdir}/cron.daily/pwchecker
%{__install} -D -p -m 0644 sysconfig/pwchecker %{buildroot}/%{_sysconfdir}/sysconfig/pwchecker

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/cron.daily/pwchecker
%config(noreplace) %{_sysconfdir}/sysconfig/pwchecker
%doc ChangeLog LICENSE README

%changelog
* Thu Dec 22 2011 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.3-1.vortex
- New upstream release.
- Update URL and Source0 URLs.

* Wed Sep 21 2011 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.2-1.vortex
- New upstream release.
- Update URL and Source0 URLs.
- Add README to doc section.

* Thu Sep 08 2011 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-2.vortex
- Add mailx to Requires.

* Thu Sep 08 2011 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-1.vortex
- Version bump.
- License under GPLv3.
- Update URL.

* Tue Apr 25 2011 Ilya A. Otyutskiy <otyutskiy@wiw.ru> - 1.0-1
- Initial packaging for CentOS.

