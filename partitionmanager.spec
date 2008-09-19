%define		state		ALPHA1

Summary:	KDE Partition Manager
Name:		partitionmanager
Version:	1.0.0
Release:	0.%{state}.1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/partitionman/%{name}-%{version}-%{state}.tar.bz2
# Source0-md5:	621c52c4c12333515066706d21596e19
URL:		http://
BuildRequires:	cmake >= 2.4.8
BuildRequires:	kde4-kdebase-devel >= 4.1.0
BuildRequires:	libuuid-devel
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _kde_prefix     %{_prefix}
%define         _kde_libdir     %{_libdir}
%define         _kde_share_dir  %{_datadir}
%define         _kde_html_dir   %{_kdedocdir}
%define         _kde_config_dir %{_datadir}/config

%description
Easily manage disks, partitions and file systems on your KDE Desktop:
Create, resize, move, copy, back up, restore or delete partitions.

%prep
%setup -q -n %{name}-%{version}-%{state}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_kde_prefix} \
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
%{_datadir}/apps/partitionmanager/partitionmanagerui.rc
