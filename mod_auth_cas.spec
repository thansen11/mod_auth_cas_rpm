Name:           mod_auth_cas
Version:        1.2
Release:        1%{?dist}
Summary:        Apache CAS Authentication Module for the JASIG/Apereo CAS Server

License:        APLv2
URL:            https://github.com/apereo/mod_auth_cas
Source0:        https://github.com/apereo/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        auth_cas_mod.conf
Source2:        auth_cas_httpd.conf

BuildRequires:  openssl-devel
BuildRequires:  httpd-devel
BuildRequires:  m4, readline-devel, autoconf, automake
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  pcre-devel

Requires:       httpd
Requires:       mod_ssl

%description
The purpose of this module is to allow an Apache web server to interact
with an authentication server that conforms to the CAS version 1 or 2
protocol or SAML protocol as used by the JASIG/Apereo CAS Server

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -vif #BZ926155 - support aarch64
%configure --with-apxs=%{_httpd_apxs}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} LIBEXECDIR=%{_httpd_moddir}
install -Dp -m 644 %{SOURCE1} %{buildroot}%{_httpd_modconfdir}/10-auth_cas.conf
install -Dp -m 644 %{SOURCE2} %{buildroot}%{_httpd_confdir}/auth_cas.conf

mkdir -p %{buildroot}/var/cache/httpd/%{name}

%files
%defattr(-,root,root,-)
%doc README
%{_libdir}/httpd/modules/*.so
%config(noreplace) %{_httpd_confdir}/*.conf
%config(noreplace) %{_httpd_modconfdir}/*.conf

%defattr(-,apache,apache,-)
%dir /var/cache/httpd/%{name}

%changelog
* Tue Mar 02 2021 Scott Williams <vwbusguy@fedoraproject.org> - 1.2-0
- Version bump to v1.2 and support for EL8

* Fri Sep 02 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-3
- Fix /var/cache/httpd/mod_auth_cas directory ownership (BZ#1368448)

* Fri Sep 02 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-2
- Fix EPEL6 conditionals for 1.1 update

* Thu Jun 16 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-1
- Update to latest stable upstream

* Wed May 11 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-0.2.rc3
- Update refs to apache versions
- Fix entry module conf in _httpd_modconfdir
- Add conf to _httpd_confdir
- Add cachedir

* Tue May 10 2016 Adam Miller <maxamillion@fedoraproject.org> - 1.1-0.1.rc3
- Pull in latest RC from upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Adam Miller <maxamillion@fedoraproject.org> - 1.0.9.1-1
- Update to latest upstream.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-8
- BZ926155 - support aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  2 2012 Joe Orton <jorton@redhat.com> - 1.0.8.1-5
- update packaging (#803065)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 29 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-2
- Fixed svn export link, upstream changed canonical URL names.

* Wed Apr 28 2010 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8.1-1
- added requires of httpd
- fixed mixed use of macros
- updated to latest version

* Fri Aug 07 2009 Adam Miller <maxamillion@fedoraproject.org> - 1.0.8-1
- First attempt to package mod_auth_cas for Fedora
