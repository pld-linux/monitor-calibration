Summary:	Monitor calibration tool
Summary(pl):	Narzêdzie do kalibracji monitora
Name:		monitor-calibration
Version:	0.1.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.burtonini.com/computing/%{name}-%{version}.tar.gz
# Source0-md5:	918b877e6a15ff90657d344b9ce3d48a
Patch0:		%{name}-libXxf86vm.patch
BuildRequires:	X11-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Monitor calibration tool formally known as GammaarRRr. This tool
features Black point calibration, per-Display gamma calibration for
arbitrary target gamma values and a graphical editor for calibrating
the gamma.

%description -l pl
Narzêdzie do kalibracji monitora formalnie znane jako GammaarRRr. To
narzêdzie obs³uguje kalibracjê czarnego punktu, kalibracjê korekty
gamma pod wy¶wietlacz dla dowolnych warto¶ci gamma oraz graficzny
edytor do kalibracji gamma.

%prep
%setup -q
%patch0 -p1

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
