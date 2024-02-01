Summary:	Z39.50 protocol support library
Summary(pl.UTF-8):	Biblioteka obsługująca protokół Z39.50
Name:		yaz
Version:	5.34.0
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://ftp.indexdata.dk/pub/yaz/%{name}-%{version}.tar.gz
# Source0-md5:	2fd487d5d44a5ce2d7d58a117b64411c
URL:		https://www.indexdata.com/resources/software/yaz/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	bison
BuildRequires:	gnutls-devel
BuildRequires:	hiredis-devel >= 0.10
BuildRequires:	libgcrypt-devel >= 1.2
BuildRequires:	libicu-devel >= 3.4
BuildRequires:	libmemcached-devel >= 0.40
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libwrap-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 5.0
BuildRequires:	tcl >= 8.2
Requires:	hiredis >= 0.10
Requires:	libgcrypt >= 1.2
Requires:	libmemcached >= 0.40
Requires:	libxslt >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAZ is a C library for developing client - and server applications
using the ANSI/NISO Z39.50 protocol for Information Retrieval.

%description -l pl.UTF-8
YAZ to biblioteka w C do tworzenia aplikacji klienckich i serwerów
korzystających z protokołu ANSI/NISO Z39.50 do uzyskiwania informacji.

%package devel
Summary:	Header files for YAZ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki YAZ
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls-devel
Requires:	hiredis-devel >= 0.10
Requires:	libgcrypt-devel >= 1.2
Requires:	libicu-devel >= 3.4
Requires:	libmemcached-devel >= 0.40
Requires:	libwrap-devel
Requires:	libxml2-devel >= 2.0
Requires:	libxslt-devel >= 1.1.0

%description devel
Header files for YAZ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki YAZ.

%package static
Summary:	YAZ static libraries
Summary(pl.UTF-8):	Statyczne biblioteki YAZ
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
YAZ static libraries.

%description static -l pl.UTF-8
Statyczne biblioteki YAZ.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-tcpd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	docDATA_INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_docdir}/yaz doc-dist

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libyaz*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE NEWS README.md
%attr(755,root,root) %{_bindir}/yaz-asncomp
%attr(755,root,root) %{_bindir}/yaz-client*
%attr(755,root,root) %{_bindir}/yaz-iconv
%attr(755,root,root) %{_bindir}/yaz-icu
%attr(755,root,root) %{_bindir}/yaz-illclient
%attr(755,root,root) %{_bindir}/yaz-json-parse
%attr(755,root,root) %{_bindir}/yaz-marcdump
%attr(755,root,root) %{_bindir}/yaz-record-conv
%attr(755,root,root) %{_bindir}/yaz-url
%attr(755,root,root) %{_bindir}/yaz-ztest*
%attr(755,root,root) %{_bindir}/zoomsh
%attr(755,root,root) %{_libdir}/libyaz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyaz.so.5
%attr(755,root,root) %{_libdir}/libyaz_icu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyaz_icu.so.5
%attr(755,root,root) %{_libdir}/libyaz_server.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyaz_server.so.5
%dir %{_datadir}/yaz
%{_datadir}/yaz/etc
%{_datadir}/yaz/ill
%{_datadir}/yaz/z39.50
%{_mandir}/man1/yaz-asncomp.1*
%{_mandir}/man1/yaz-client*.1*
%{_mandir}/man1/yaz-iconv.1*
%{_mandir}/man1/yaz-icu.1*
%{_mandir}/man1/yaz-illclient.1*
%{_mandir}/man1/yaz-json-parse.1*
%{_mandir}/man1/yaz-marcdump.1*
%{_mandir}/man1/yaz-record-conv.1*
%{_mandir}/man1/yaz-url.1*
%{_mandir}/man1/zoomsh.1*
%{_mandir}/man7/bib1-attr.7*
%{_mandir}/man7/yaz.7*
%{_mandir}/man7/yaz-log.7*
%{_mandir}/man8/yaz-ztest*.8*

%files devel
%defattr(644,root,root,755)
%doc doc-dist/* 
%attr(755,root,root) %{_bindir}/yaz-config
%attr(755,root,root) %{_libdir}/libyaz.so
%attr(755,root,root) %{_libdir}/libyaz_icu.so
%attr(755,root,root) %{_libdir}/libyaz_server.so
%{_includedir}/yaz
%{_pkgconfigdir}/yaz.pc
%{_pkgconfigdir}/yaz-icu.pc
%{_pkgconfigdir}/yaz-server.pc
%{_aclocaldir}/yaz.m4
%{_mandir}/man1/yaz-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libyaz.a
%{_libdir}/libyaz_icu.a
%{_libdir}/libyaz_server.a
