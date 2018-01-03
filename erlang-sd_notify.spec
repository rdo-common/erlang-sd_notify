%global realname sd_notify
%global have_rebar 0
%{?filter_setup:
%filter_provides_in %{_libdir}/erlang/lib/.*\.so$
%filter_setup
}
%{expand: %(NIF_VER=`rpm -q erlang-erts --provides | grep --color=no erl_nif_version` ; if [ "$NIF_VER" != "" ]; then echo %%global __erlang_nif_version $NIF_VER ; fi)}
%{expand: %(DRV_VER=`rpm -q erlang-erts --provides | grep --color=no erl_drv_version` ; if [ "$DRV_VER" != "" ]; then echo %%global __erlang_drv_version $DRV_VER ; fi)}


Name:		erlang-%{realname}
Version:	0.1
Release:	9%{?dist}
Summary:	Erlang interface to systemd notify subsystem
Group:		Development/Languages
License:	MIT
URL:		https://github.com/lemenkov/erlang-sd_notify
VCS:		scm:git:https://github.com/lemenkov/erlang-sd_notify.git
Source0:	https://github.com/lemenkov/erlang-sd_notify/archive/%{version}/erlang-%{realname}-%{version}.tar.gz
Source1:	sd_notify.app
%if %{have_rebar}
BuildRequires:	erlang-rebar
%else
BuildRequires:  erlang-compiler
BuildRequires:  erlang-erl_interface
%endif %{have_rebar}
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
%if %{have_rebar}
CFLAGS="%{optflags}" LDFLAGS=-lsystemd REBAR_FLAGS="--verbose 2" make %{?_smp_mflags}
%else
mkdir ebin priv
export CFLAGS="%{optflags}"
%{__cc} -c $CFLAGS -g -Wall -fPIC  -I %{_libdir}/erlang/lib/erl_interface-*/include -I %{_libdir}/erlang/erts-*/include   c_src/sd_notify.c -o c_src/sd_notify.o
%{__cc} c_src/sd_notify.o $LDFLAGS -shared  -L %{_libdir}/erlang/lib/erl_interface-*/lib -lerl_interface -lei -lsystemd -o priv/sd_notify_drv.so
erlc -o ebin/ src/sd_notify.erl
%endif %{have_rebar}


%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/{ebin,priv}
%if %{have_rebar}
install -m 644 -p ebin/%{realname}.app $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%else
install -m 644 -p %{S:1} $RPM_BUILD_ROOT%{_libdir}/erlang/lib/%{realname}-%{version}/ebin
%endif %{have_rebar}
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
* Wed Apr 13 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.1-9
- Re-enable building w/o rebar.

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
