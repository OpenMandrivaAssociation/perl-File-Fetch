%define upstream_name    File-Fetch
%define upstream_version 0.48

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A generic file fetching mechanism
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/File-Fetch-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-version
BuildRequires:	perl(HTML::HeadParser)
BuildRequires:	perl(IPC::Cmd) >= 0.420.0
BuildArch:	noarch

%description
File::Fetch is a generic file fetching mechanism.

It allows you to fetch any file pointed to by a ftp, http, file, or rsync uri
by a number of different means.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files 
%doc README CHANGES
%{perl_vendorlib}/File
%{_mandir}/*/*
