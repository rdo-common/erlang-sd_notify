%global realname sd_notify
%global upstream lemenkov
%{?filter_setup:
%filter_provides_in %{_libdir}/erlang/lib/.*\.so$
%filter_setup
}


Name:		erlang-%{realname}
Version:	0.1
Release:	9%{?dist}
Summary:	Erlang interface to systemd notify subsystem
Group:		Development/Languages
License:	MIT
URL:		https://github.com/%{upstream}/erlang-%{realname}
%if 0%{?el7}%{?fedora}
VCS:		scm:git:https://github.com/%{upstream}/erlang-%{realname}.git
%endif
Source0:	https://github.com/%{upstream}/erlang-%{realname}/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
Source1:	erlang-sd_notify-rebar.config
BuildRequires:	erlang-rebar
BuildRequires:	systemd-devel
%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
%{summary}.


%prep
%setup -q
cp %{SOURCE1} rebar.config


%build
%{erlang_compile}


%install
%{erlang_install}


%check
# Empty for now
%{erlang_test}


%files
%license LICENSE
%{erlang_appdir}/


%changelog
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
