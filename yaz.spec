Summary:	Z39.50 protocol support library
Summary(pl):	Biblioteka obs³uguj±ca protokó³ Z39.50
Name:		yaz
Version:	1.8.6
Release:	1
License:	BSD-like
Vendor:		Index Data ApS <info@indexdata.dk>
Group:		Libraries
Source0:	http://ftp.indexdata.dk/pub/yaz/%{name}-%{version}.tar.gz
Patch0:		%{name}-libwrap-fix.patch
URL:		http://www.indexdata.dk/yaz/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libwrap-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAZ is a C library for developing client - and server applications
using the ANSI/NISO Z39.50 protocol for Information Retrieval.

%description -l pl
YAZ to biblioteka w C do tworzenia aplikacji klienckich i serwerów
korzystaj±cych z protoko³u ANSI/NISO Z39.50 do uzyskiwania informacji.

%package devel
Summary:	Header files for YAZ library
Summary(pl):	Pliki nag³ówkowe biblioteki YAZ
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libwrap-devel

%description devel
Header files for YAZ library.

%description devel -l pl
Pliki nag³ówkowe biblioteki YAZ.

%package static
Summary:	YAZ static libraries
Summary(pl):	Statyczne biblioteki YAZ
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
YAZ static libraries.

%description static -l pl
Statyczne biblioteki YAZ.

%prep
%setup -q
%patch -p1

%build
aclocal
autoconf
automake -a -c -f --foreign
%configure \
	--enable-shared \
	--enable-tcpd

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C doc \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/yaz/doc ./doc-dist

gzip -9nf README LICENSE CHANGELOG TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%config %{_datadir}/yaz/tab
%attr(755,root,root) %{_bindir}/yaz-client
%attr(755,root,root) %{_bindir}/yaz-ztest
%attr(755,root,root) %{_bindir}/yaz-comp
%attr(755,root,root) %{_bindir}/zoomsh
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/yaz

%files devel
%defattr(644,root,root,755)
%doc doc-dist/*
%attr(755,root,root) %{_bindir}/yaz-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/yaz
%{_aclocaldir}/yaz.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
