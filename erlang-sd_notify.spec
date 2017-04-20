%global realname sd_notify
%global upstream systemd


Name:		erlang-%{realname}
Version:	1.0
Release:	2%{?dist}
Summary:	Erlang interface to systemd notify subsystem
License:	MIT
URL:		https://github.com/%{upstream}/erlang-%{realname}
VCS:		scm:git:https://github.com/%{upstream}/erlang-%{realname}.git
Source0:	https://github.com/%{upstream}/erlang-%{realname}/archive/v%{version}/erlang-%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar
BuildRequires:	systemd-devel
%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
%{summary}.


%prep
%setup -q


%build
%{erlang_compile}


%install
%{erlang_install}


%check
%{erlang_test}


%files
%license LICENSE
%{erlang_appdir}/


%changelog
* Thu Apr 20 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.0-2
- Remove out-of-tree makefile (upstreamed)

* Thu Apr 20 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.0-1
- Ver. 1.0 (backwards API/ABI compatible)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 0.1-11
- Rebuild

* Fri Apr 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1-10
- Drop unneeded macro

* Wed Mar 30 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1-9
- Rebuild with Erlang 18.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1-7
- Rebuild with Erlang 18.2.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 04 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-5
- Rebuild with Erlang 17.3.3

* Thu Oct  2 2014 John Eckersberg <eck@redhat.com> - 0.1-4
- Explicitly link shared library with libsystemd (#1148604)

* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-3
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 03 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-1
- initial build
