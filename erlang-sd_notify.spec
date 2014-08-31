%global realname sd_notify
%{?filter_setup:
%filter_provides_in %{_libdir}/erlang/lib/.*\.so$
%filter_setup
}
%{expand: %(NIF_VER=`rpm -q erlang-erts --provides | grep --color=no erl_nif_version` ; if [ "$NIF_VER" != "" ]; then echo %%global __erlang_nif_version $NIF_VER ; fi)}
%{expand: %(DRV_VER=`rpm -q erlang-erts --provides | grep --color=no erl_drv_version` ; if [ "$DRV_VER" != "" ]; then echo %%global __erlang_drv_version $DRV_VER ; fi)}


Name:		erlang-%{realname}
Version:	0.1
Release:	3%{?dist}
Summary:	Erlang interface to systemd notify subsystem
Group:		Development/Languages
License:	MIT
URL:		https://github.com/lemenkov/erlang-sd_notify
VCS:		scm:git:https://github.com/lemenkov/erlang-sd_notify.git
Source0:	https://github.com/lemenkov/erlang-sd_notify/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar
BuildRequires:	systemd-devel
Requires:	erlang-erts%{?_isa}
Requires:	erlang-kernel%{?_isa}
Requires:	erlang-stdlib%{?_isa}
%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
%{summary}.


%prep
%setup -q


%build
CFLAGS="%{optflags}" REBAR_FLAGS="--verbose 2" make %{?_smp_mflags}


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/{ebin,priv}
install -m 644 -p ebin/%{realname}.app $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 644 -p ebin/%{realname}.beam $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
install -m 755 -p priv/%{realname}_drv.so $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/priv


%check
# Empty for now
#rebar eunit -v


%files
%doc LICENSE
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/ebin/
%dir %{_libdir}/erlang/lib/%{realname}-%{version}/priv/
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.app
%{_libdir}/erlang/lib/%{realname}-%{version}/ebin/%{realname}.beam
%{_libdir}/erlang/lib/%{realname}-%{version}/priv/%{realname}_drv.so


%changelog
* Thu Aug 28 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-3
- Rebuild with Erlang 17.2.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 03 2014 Peter Lemenkov <lemenkov@gmail.com> - 0.1-1
- initial build
