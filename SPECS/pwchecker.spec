%define debug_package %{nil}

Summary:	A handy tool which will check if users have passwords
Name:		pwchecker
Version:	1.1
Release:	2.vortex%{?dist}
Vendor:		Vortex RPM
BuildArch:	noarch
License:	GPLv3
Group:		Applications/System
URL:		http://thesharp.ru/pwchecker
Source0:	http://thesharp.ru/pwchecker/pwchecker-%{version}.tar.gz
Requires:	mailx
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
A handy tool which will check if users have passwords.

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
%doc ChangeLog LICENSE

%changelog
* Thu Sep 08 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-2.vortex
- Add mailx to Requires.

* Thu Sep 08 2011  Ilya A. Otyutskiy <sharp@thesharp.ru> - 1.1-1.vortex
- Version bump.
- License under GPLv3.
- Update URL.

* Tue Apr 25 2011  Ilya A. Otyutskiy <otyutskiy@wiw.ru> - 1.0-1
- Initial packaging for CentOS.

