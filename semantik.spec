Summary:	Semantik
Summary(pl.UTF-8):	Semantik
Name:		semantik
Version:	0.5.8
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://freehackers.org/~tnagy/%{name}-%{version}.tar.bz2
# Source0-md5:	67ea70a8f3b124d81be9d97d63383d6c
Patch0:		%{name}-findqt4qmake.patch
URL:		http://freehackers.org/~tnagy/kdissert.html
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtTest-devel
BuildRequires:	QtXml-devel
BuildRequires:	ocaml
BuildRequires:	python >= 2.3
BuildRequires:	python-libs >= 2.3
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Semantik (previously Kdissert) is a mindmapping-like tool to help
students to produce complicated documents very quickly and efficiently
: presentations, dissertations, thesis, reports. While targetted
mostly at students, Kdissert can also help teachers, decision maker,
engineers and businessmen.

#%description -l pl.UTF-8

%prep
%setup -q
# this is so ugly, someone please shoot me, but there is no other way to patch that thing :/
./waf --help >/dev/null
%patch0 -p1

%build
./waf configure \
	--prefix=%{_prefix} \
%if "%{_lib}" == "lib64"
	--use64
%endif
./waf

%install
rm -rf $RPM_BUILD_ROOT

DESTDIR=$RPM_BUILD_ROOT ./waf install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/semantik
%attr(755,root,root) %{_libdir}/libnablah.so
%{_desktopdir}/semantik.desktop
%{_pixmapsdir}/semantik.png
%{_datadir}/semantik
