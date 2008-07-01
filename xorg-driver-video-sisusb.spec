Summary:	X.org video driver for SiS video chips connected via a Net2280-based USB dongle
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów SiS podłączonych poprzez przejściówkę USB Net2280
Name:		xorg-driver-video-sisusb
Version:	0.9.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-sisusb-%{version}.tar.bz2
# Source0-md5:	7b1f5465f423a859f306f4f1d6306a1b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for SiS video chips connected via a Net2280-based
USB dongle. It supports SiS315E/PRO video chipset.

Note: it requires a Linux kernel driver (included in Linux 2.6.12 and
later).

%description -l pl.UTF-8
Sterownik obrazu X.org dla układów SiS podłączonych poprzez
przejściówkę USB opartą na układzie Net2280. Obsługuje układ graficzny
SiS315E/PRO.

Uwaga: wymaga sterownika jądra Linuksa (załączonego w wersji Linuksa
2.6.12 i późniejszych).

%prep
%setup -q -n xf86-video-sisusb-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sisusb_drv.so
%{_mandir}/man4/sisusb.4*
