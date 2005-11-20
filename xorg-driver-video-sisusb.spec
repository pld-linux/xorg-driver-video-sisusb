Summary:	X.org video driver for SiS video chips connected via a Net2280-based USB dongle
Summary(pl):	Sterownik obrazu X.org dla uk³adów SiS pod³±czonych poprzez przej¶ciówkê USB Net2280
Name:		xorg-driver-video-sisusb
Version:	0.7.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/driver/xf86-video-sisusb-%{version}.tar.bz2
# Source0-md5:	906394f9d341e57eb062b68d11d173b1
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
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel >= 0.99.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for SiS video chips connected via a Net2280-based
USB dongle. It supports SiS315E/PRO video chipset.

Note: it requires a Linux kernel driver (included in Linux 2.6.12 and
later).

%description -l pl
Sterownik obrazu X.org dla uk³adów SiS pod³±czonych poprzez
przej¶ciówkê USB opart± na uk³adzie Net2280. Obs³uguje uk³ad graficzny
SiS315E/PRO.

Uwaga: wymaga sterownika j±dra Linuksa (za³±czonego w wersji Linuksa
2.6.12 i pó¼niejszych).

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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/sisusb_drv.so
%{_mandir}/man4/sisusb.4x*
