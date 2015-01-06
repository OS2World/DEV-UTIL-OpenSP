# Copyright (C) 2000 Matthias Clasen
# See the file COPYING for copying permissions.

Summary: The OpenJade Group's SGML and XML parsing tools
Name: OpenSP
Version: 1.5.1
Release: 1
BuildRoot: /tmp/OpenSP-1.5.1-buildroot
Copyright: Copyright 1997 James Clark
Group: Applications/Text
Source: http://download.sourceforge.net/openjade/OpenSP-1.5.1.tar.gz
URL: http://openjade.sourceforge.net/
Vendor: The OpenJade Team
Packager: Matthias Clasen <clasen@mathematik.uni-freiburg.de>
Requires: OpenSP-lib

%description
This package is a collection of SGML/XML tools called OpenSP. It is a fork from
James Clark's SP suite. These tools are used to parse, validate, and normalize
SGML and XML files.  
     
%package lib
Summary: Runtime library for the OpenJade group's SP suite
Group: System Environment/Libraries

%description lib 
This is the SP suite's shared library runtime support.  This C++
library contains entity management functions, parsing functions, and
other functions useful for SGML/XML/DSSSL development.

%package devel
Summary: Libraries and include files for developing OpenSP applications.
Group: Development/Libraries

%description devel 
This contains include files and libraries for OpenSP.
This C++ library contains entity management functions, parsing functions,
and other functions useful for SGML/XML/DSSSL development.

%prep
# check that rpm is new enough to know internal macros like %{_prefix}
rpmversion=`rpm -q --queryformat '%{RPMVERSION}' rpm | cut -d. -f1`
[ ${rpmversion} -lt 3 ] && { echo "please update rpm" exit 1 ; }
# unpack source .tar.gz package
%setup

%build
# configure build system according to rpm settings
./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} --bindir=%{_bindir} --sbindir=%{_sbindir} --libexecdir=%{_libexecdir} --datadir=%{_datadir} --sysconfdir=%{_sysconfdir} --sharedstatedir=%{_sharedstatedir} --localstatedir=%{_localstatedir} --libdir=%{_libdir} --includedir=%{_includedir} --oldincludedir=%{_oldincludedir} --infodir=%{_infodir} --mandir=%{_mandir}
# compile and link
make CFLAGS="${RPM_OPT_FLAGS}"

%install
# install all files
make "DESTDIR=${RPM_BUILD_ROOT}" install

%clean
test "$RPM_BUILD_ROOT" = "/" || rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/OpenSP/*
%doc %{_datadir}/doc/OpenSP/*

%files lib
%defattr(-, root, root)
%{_libdir}/*.so.*
%{_datadir}/locale/*/LC_MESSAGES/sp.mo

%files devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/OpenSP/*

%changelog
* Wed Feb 21 2001 Terje Bless <link@tss.no>
- Fixed name of l10n message files ("OpenSP" -> "sp").

* Tue Feb 20 2001 Terje Bless <link@tss.no>
- Tweaked strings, moved to Sourceforge.
