%define	major	1
%define libname	%mklibname ghthash %{major}
%define devname	%mklibname ghthash -d

Summary:	Generic Hash Table library
Name:		libghthash
Version:	0.6.2
Release:	16
Group:		System/Libraries
License:	GPLv2
Url:		http://www.ipd.bth.se/ska/sim_home/libghthash.html
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

%package -n	%{devname}
Summary:	Development library and header files for the Generic Hash Table library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	ghthash-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the development libghthash library and its header
files.

%prep
%setup -q
%apply_patches
rm -f configure
libtoolize --copy --force; aclocal; autoconf; automake --add-missing --copy --foreign; autoconf

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

# cleanup
pushd examples
    make clean
    rm -f Makefile.win
popd

%files -n %{libname}
%{_libdir}/libghthash.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog README
%doc examples html TODO
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*

