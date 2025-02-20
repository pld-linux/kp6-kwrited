#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.3.1
%define		qtver		5.15.2
%define		kpname		kwrited
Summary:	kwrited
Name:		kp6-%{kpname}
Version:	6.3.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		Base
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ba99fb62f638e9452ee68b0627f46d0b
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= 1.4.0
BuildRequires:	kf6-kcoreaddons-devel
BuildRequires:	kf6-kdbusaddons-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-knotifications-devel
BuildRequires:	kf6-kpty-devel
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Plasma daemon listening for wall and write messages.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/kwrited.so
%{_datadir}/knotifications6/kwrited.notifyrc
