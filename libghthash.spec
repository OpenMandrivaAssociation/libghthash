%define	major 1
%define libname	%mklibname ghthash %{major}
%define develname %mklibname ghthash -d

Summary:	Generic Hash Table library
Name:		libghthash
Version:	0.6.2
Release:	%mkrel 9
Group:		System/Libraries
License:	GPL
URL:		http://www.ipd.bth.se/ska/sim_home/libghthash.html
Source0:	http://www.ipd.bth.se/ska/sim_home/filer/%{name}-%{version}.tar.bz2
Patch0:		libghthash-automake-1.13.patch

%description
The GHT (Generic Hash Table) library is a hash table
implementation in C for storing arbitrary types of data. It is
meant to be small, easily extensible (in terms of hash functions
etc), and easy to understand codewise.

%package -n	%{libname}
Summary:	Generic Hash Table library
Group:		System/Libraries

%description -n	%{libname}
The GHT (Generic Hash Table) library is a hash table
implementation in C for storing arbitrary types of data. It is
meant to be small, easily extensible (in terms of hash functions
etc), and easy to understand codewise.

%package -n	%{develname}
Summary:	Static library and header files for the Generic Hash Table library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	ghthash-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	ghthash-devel
Obsoletes:	%{mklibname ghthash 0}-devel
Obsoletes:	%{mklibname ghthash 2}-devel

%description -n	%{develname}
The GHT (Generic Hash Table) library is a hash table
implementation in C for storing arbitrary types of data. It is
meant to be small, easily extensible (in terms of hash functions
etc), and easy to understand codewise.

This package contains the static libghthash library and its header
files.

%prep
%setup -q
%apply_patches

%build
rm -f configure
libtoolize --copy --force; aclocal; autoconf; automake --add-missing --copy --foreign; autoconf

%configure2_5x

%make

%install
%makeinstall_std

# cleanup
pushd examples
    make clean
    rm -f Makefile.win
popd

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc examples html TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*


%changelog
* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-9mdv2011.0
+ Revision: 660253
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-8mdv2011.0
+ Revision: 602549
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-7mdv2010.1
+ Revision: 520812
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6.2-6mdv2010.0
+ Revision: 425547
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.6.2-5mdv2009.0
+ Revision: 222571
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.6.2-4mdv2008.1
+ Revision: 150567
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-3mdv2008.0
+ Revision: 61509
- try to fix build (take #2)

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.2-2mdv2008.0
+ Revision: 61407
- try to fix build (take #1)

* Mon Jul 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-1mdv2008.0
+ Revision: 52462
- new version
- new devel library policy
- drop buildrequires on old autotools
- fix mixture of tabs and spaces


* Wed Nov 01 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.1-1mdv2007.0
+ Revision: 74840
- 0.6.1
- Import libghthash

* Fri Jun 02 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6.0-1mdv2007.0
- 0.6.0
- major change...

* Sat Jul 23 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.6-1mdk
- initial Mandriva package

