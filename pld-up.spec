Summary:	Packets Update Tool
Summary(pl):	Narzêdzie do aktualizacji pakietów
Name:		pldup
Version:	0.25
Release:	1
License:	GPL
Group:		Networking/Admin
Source0:	http://www.kki.net.pl/~adgor/%{name}-%{version}.tar.gz
Requires:	poldek
Requires:	grep
Requires:	sed
Requires:	textutils
Buildarch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%description -l pl
Prosty skrypt do aktualizacji pakietów w Twoim systemie
%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install pldupsrcs $RPM_BUILD_ROOT%{_sysconfdir}/
install -d $RPM_BUILD_ROOT%{_bindir}
install pldup $RPM_BUILD_ROOT%{_bindir}/
install -d $RPM_BUILD_ROOT%{_applnkdir}
install pldup.desktop $RPM_BUILD_ROOT%{_applnkdir}/
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install pldup.png $RPM_BUILD_ROOT%{_pixmapsdir}/

gzip -9nf README
gzip -9nf CHANGELOG
gzip -9nf TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz CHANGELOG.gz TODO.gz
%{_sysconfdir}/pldupsrcs
%{_applnkdir}/pldup.desktop
%{_pixmapsdir}/pldup.png
%attr(755,root,root) %{_bindir}/pldup
