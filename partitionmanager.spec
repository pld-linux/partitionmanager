%define		kdever		4.4.5
%define		qtver		4.6.3

Summary:	KDE Partition Manager
Name:		partitionmanager
Version:	1.0.3
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/partitionman/%{name}-%{version}.tar.bz2
# Source0-md5:	1f987d314c717ba2579c69eeef16336d
URL:		http://partitionman.sourceforge.net/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gettext-tools
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	libblkid-devel
BuildRequires:	libuuid-devel
BuildRequires:	parted-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easily manage disks, partitions and file systems on your KDE Desktop:
Create, resize, move, copy, back up, restore or delete partitions.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DPARTMAN_KCM=ON \
	-DPARTMAN_KPART=ON \
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
%attr(755,root,root) %{_bindir}/partitionmanager-bin
%attr(755,root,root) %{_libdir}/libpartitionmanagerprivate.so
%attr(755,root,root) %{_libdir}/kde4/kcm_partitionmanager.so
%attr(755,root,root) %{_libdir}/kde4/partitionmanagerpart.so
%dir %{_datadir}/apps/partitionmanager
%{_datadir}/apps/partitionmanager/partitionmanagerui.rc
%dir %{_datadir}/apps/partitionmanagerpart
%{_datadir}/apps/partitionmanagerpart/partitionmanagerpart.rc
%{_desktopdir}/kde4/partitionmanager.desktop
%{_datadir}/kde4/services/kcm_partitionmanager.desktop
%{_datadir}/kde4/services/partitionmanagerpart.desktop
%{_iconsdir}/hicolor/*x*/apps/partitionmanager.png
