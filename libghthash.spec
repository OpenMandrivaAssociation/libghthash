%define	major 1
%define libname	%mklibname ghthash %{major}
%define develname %mklibname ghthash -d

Summary:	Generic Hash Table library
Name:		libghthash
Version:	0.6.2
Release:	%mkrel 2
Group:		System/Libraries
License:	GPL
URL:		http://www.ipd.bth.se/ska/sim_home/libghthash.html
Source0:	http://www.ipd.bth.se/ska/sim_home/filer/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
Provides:	ghthash-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	ghthash-devel libghthash-devel
Obsoletes:	%{mklibname ghthash 2}-devel
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname ghthash 0}-devel

%description -n	%{develname}
The GHT (Generic Hash Table) library is a hash table
implementation in C for storing arbitrary types of data. It is
meant to be small, easily extensible (in terms of hash functions
etc), and easy to understand codewise.

This package contains the static libghthash library and its header
files.

%prep

%setup -q

%build
rm -f configure
libtoolize --copy --force; aclocal; autoconf; automake --add-missing --copy --foreign; autoconf

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# cleanup
pushd examples
    make clean
    rm -f Makefile.win
popd

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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
%{_libdir}/*.la
%{_mandir}/man3/*
