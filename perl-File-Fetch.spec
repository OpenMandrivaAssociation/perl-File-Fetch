%define upstream_name    File-Fetch
%define upstream_version 0.22

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A generic file fetching mechanism
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:  perl-version
Buildrequires:  perl(IPC::Cmd) >= 0.420.0
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
File::Fetch is a generic file fetching mechanism.

It allows you to fetch any file pointed to by a ftp, http, file, or rsync uri
by a number of different means.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
