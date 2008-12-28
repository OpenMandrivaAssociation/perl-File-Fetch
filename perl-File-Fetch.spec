%define module  File-Fetch
%define name    perl-%{module}
%define version 0.18
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A generic file fetching mechanism
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.bz2
Buildrequires:  perl-version
Buildrequires:  perl(IPC::Cmd) >= 0.42
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
File::Fetch is a generic file fetching mechanism.

It allows you to fetch any file pointed to by a ftp, http, file, or rsync uri
by a number of different means.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/File
%{_mandir}/*/*


