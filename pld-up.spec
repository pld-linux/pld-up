Summary:	Packets Update Tool
Summary(pl):	Narzêdzie do aktualizacji pakietów
Name:		pld-up
Version:	0.28
Release:	1
License:	GPL
Group:		Networking/Admin
#Source0:	http://free.of.pl/a/adgor/%{name}-%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	df23068242a75d45750fdf83f47535e5
Requires:	grep
Requires:	poldek
Requires:	sed
Requires:	textutils
BuildArch:	noarch
Obsoletes:	pldup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple script that can update your system.

%description -l pl
Prosty skrypt do aktualizacji pakietów w Twoim systemie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_applnkdir},%{_pixmapsdir}}

install pldupsrcs $RPM_BUILD_ROOT%{_sysconfdir}
install pldup $RPM_BUILD_ROOT%{_bindir}
install pldup.desktop $RPM_BUILD_ROOT%{_applnkdir}
install pldup.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG TODO
%attr(755,root,root) %{_bindir}/pldup
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pldupsrcs
%{_applnkdir}/pldup.desktop
%{_pixmapsdir}/pldup.png
