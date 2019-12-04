Name:           opensp
Version:        1.5.2
Release:        31
Summary:        SGML and XML parser
License:        MIT
BuildRequires:  gcc-c++ xmlto
Requires:       sgml-common >= 0.5
URL:            http://openjade.sourceforge.net/
Source:         http://download.sourceforge.net/openjade/OpenSP-%{version}.tar.gz

Patch0001:      opensp-multilib.patch
Patch0002:      opensp-nodeids.patch
Patch0003:      opensp-sigsegv.patch
Patch0004:      opensp-manpage.patch

%description
The OpenSP is an SGML(Standard Generalized Markup Language) System
Conforming to International Standard ISO 8879.
The OpenSP package contains a C++ library for using SGML/XML files.


%package   devel
Summary:   Files for developing applications using OpenSP
Requires:  %{name} = %{version}-%{release}

%description devel
The opensp-devel package contains header files and
libtool library for developing applications using OpenSP.


%prep
%autosetup -n OpenSP-%{version} -p1
iconv -f latin1 -t utf8 ChangeLog -o ChangeLog.tmp
mv -f ChangeLog.tmp ChangeLog
touch lib/parser_inst.cxx

%build
%configure \
 --disable-dependency-tracking --disable-static --enable-http \
 --enable-default-catalog=%{_sysconfdir}/sgml/catalog \
 --enable-default-search-path=%{_datadir}/sgml:%{_datadir}/xml
%make_build

%install
%make_install
%delete_la

for file in nsgmls sgmlnorm spam spent sx ; do
   ln -s o$file $RPM_BUILD_ROOT%{_bindir}/$file
   echo ".so man1/o${file}.1" > $RPM_BUILD_ROOT%{_mandir}/man1/${file}.1
done

mv $RPM_BUILD_ROOT%{_bindir}/sx $RPM_BUILD_ROOT%{_bindir}/sgml2xml
mv $RPM_BUILD_ROOT%{_mandir}/man1/sx.1 $RPM_BUILD_ROOT%{_mandir}/man1/sgml2xml.1


%find_lang sp5


%check
make check || :


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files -f sp5.lang
%exclude %{_docdir}/OpenSP
%exclude %{_datadir}/OpenSP
%doc doc/*.htm
%doc docsrc/releasenotes.html
%doc AUTHORS BUGS COPYING ChangeLog NEWS README
%doc pubtext/opensp-implied.dcl
%{_bindir}/*
%{_libdir}/libosp.so.*
%{_mandir}/man1/*.1*

%files devel
%exclude %{_docdir}/OpenSP
%exclude %{_datadir}/OpenSP
%{_includedir}/OpenSP/
%{_libdir}/libosp.so


%changelog
* Sat Nov 30 2019 zoushuangshuang<zoushuangshuang@huawei.com> - 1.5.2-31
- Package init
