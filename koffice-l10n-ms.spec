Name: koffice-l10n-ms
Version: 1.9.98.5
Release: %mkrel 2
Summary: Language files for KOffice Malay
Group: System/Internationalization
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License: GPLv2+
URL: https://www.koffice.org
BuildArch: noarch
Source: ftp://ftp.kde.org/pub/kde/unstable/koffice-%version/src/koffice-l10n/%name-%version.tar.bz2
BuildRequires: gettext >= 0.15
BuildRequires: kdelibs4-devel
Requires: locales-ms
Requires: koffice-core
Provides: koffice-l10n

%description 
Provides Malay translations for KOffice.

%files 
%defattr(-,root,root,-)
%{_kde_datadir}/*/*/*

#------------------------------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.98.5-2mdv2011.0
+ Revision: 612641
- the mass rebuild of 2010.1 packages

* Sat Jan 17 2009 Funda Wang <fwang@mandriva.org> 1.9.98.5-1mdv2009.1
+ Revision: 330494
- new version 1.9.98.5

* Thu Dec 11 2008 Funda Wang <fwang@mandriva.org> 1.9.98.3-1mdv2009.1
+ Revision: 312731
- new version 1.9.98.3

* Thu Nov 20 2008 Funda Wang <fwang@mandriva.org> 1.9.98.2-1mdv2009.1
+ Revision: 305052
- add source and spec
- Created package structure for koffice-l10n-ms.

