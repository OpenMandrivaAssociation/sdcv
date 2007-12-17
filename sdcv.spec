%define	version	0.4.1
%define release	%mkrel 1

Summary:	Command-line version of StarDict dictionary
Name:		sdcv
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Text tools
URL:		http://sdcv.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRequires:	glib2-devel

%description
SDCV is simple, cross-platform text-base utility for work with
dictionaries in StarDict's format.


%prep
%setup -q

%build
%configure2_5x
%make


%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_mandir}/man1/sdcv*

