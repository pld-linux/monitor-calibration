Summary:	Monitor calibration tool
Summary(pl.UTF-8):	Narzędzie do kalibracji monitora
Name:		monitor-calibration
Version:	0.1.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.burtonini.com/computing/%{name}-%{version}.tar.gz
# Source0-md5:	918b877e6a15ff90657d344b9ce3d48a
Patch0:		%{name}-libXxf86vm.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitor calibration tool formally known as GammaarRRr. This tool
features Black point calibration, per-Display gamma calibration for
arbitrary target gamma values and a graphical editor for calibrating
the gamma.

%description -l pl.UTF-8
Narzędzie do kalibracji monitora formalnie znane jako GammaarRRr. To
narzędzie obsługuje kalibrację czarnego punktu, kalibrację korekty
gamma pod wyświetlacz dla dowolnych wartości gamma oraz graficzny
edytor do kalibracji gamma.

%prep
%setup -q
%patch -P0 -p1

%build
%{__autoconf}
%{__aclocal}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
