%define		state		BETA1a
%define		kdever		4.1.96
%define		qtver		4.4.3

Summary:	KDE Partition Manager
Name:		partitionmanager
Version:	1.0.0
Release:	0.%{state}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/partitionman/%{name}-%{version}-%{state}.tar.bz2
# Source0-md5:	df34662e959e12018e24158e7062b9a5
URL:		http://sourceforge.net/projects/partitionman/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	cmake >= 2.6.2
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	libuuid-devel
BuildRequires:	parted-devel
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easily manage disks, partitions and file systems on your KDE Desktop:
Create, resize, move, copy, back up, restore or delete partitions.

%prep
%setup -q -n %{name}-%{version}-BETA1

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang partitionmanager --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/partitionmanager
%attr(755,root,root) %{_libdir}/libpartitionmanagerprivate.so
%dir %{_datadir}/apps/partitionmanager
%{_datadir}/apps/partitionmanager/partitionmanagerui.rc
%{_desktopdir}/kde4/partitionmanager.desktop
