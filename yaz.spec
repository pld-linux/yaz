Summary:	Z39.50 protocol support library
Summary(pl):	Biblioteka obsługująca protokół Z39.50
Name:		yaz
Version:	2.0.15
Release:	1
License:	BSD-like
Vendor:		Index Data ApS <info@indexdata.dk>
Group:		Libraries
Source0:	http://ftp.indexdata.dk/pub/yaz/%{name}-%{version}.tar.gz
# Source0-md5:	88dfe2d30bc6644a8919b8dca7a437c9
Patch0:		%{name}-libwrap-fix.patch
Patch1:		%{name}-link.patch
URL:		http://www.indexdata.dk/yaz/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
BuildRequires:	libwrap-devel
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAZ is a C library for developing client - and server applications
using the ANSI/NISO Z39.50 protocol for Information Retrieval.

%description -l pl
YAZ to biblioteka w C do tworzenia aplikacji klienckich i serwerów
korzystających z protokołu ANSI/NISO Z39.50 do uzyskiwania informacji.

%package devel
Summary:	Header files for YAZ library
Summary(pl):	Pliki nagłówkowe biblioteki YAZ
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libwrap-devel

%description devel
Header files for YAZ library.

%description devel -l pl
Pliki nagłówkowe biblioteki YAZ.

%package static
Summary:	YAZ static libraries
Summary(pl):	Statyczne biblioteki YAZ
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
YAZ static libraries.

%description static -l pl
Statyczne biblioteki YAZ.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-tcpd \
	--with-openssl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C doc \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_docdir}/yaz ./doc-dist

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README TODO
%attr(755,root,root) %{_bindir}/yaz-asncomp
%attr(755,root,root) %{_bindir}/yaz-client*
%attr(755,root,root) %{_bindir}/yaz-iconv
%attr(755,root,root) %{_bindir}/yaz-marcdump
%attr(755,root,root) %{_bindir}/yaz-ztest*
%attr(755,root,root) %{_bindir}/zoomsh
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_datadir}/yaz
%{_datadir}/yaz/etc
%{_datadir}/yaz/ill
%{_datadir}/yaz/z39.50
%{_mandir}/man1/yaz-asncomp.1*
%{_mandir}/man1/yaz-client*.1*
%{_mandir}/man1/yaz-iconv.1*
%{_mandir}/man1/yaz-marcdump.1*
%{_mandir}/man1/zoomsh.1*
%{_mandir}/man7/yaz.7*
%{_mandir}/man8/yaz-ztest*.8*

%files devel
%defattr(644,root,root,755)
%doc doc-dist/*
%attr(755,root,root) %{_bindir}/yaz-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/yaz
%{_aclocaldir}/yaz.m4
%{_mandir}/man8/yaz-config.8*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
