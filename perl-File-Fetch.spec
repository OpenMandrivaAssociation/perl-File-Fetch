%define upstream_name    File-Fetch
%define upstream_version 0.28

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A generic file fetching mechanism
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

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

%check
make test

%install
%makeinstall_std

%files 
%doc README CHANGES
%{perl_vendorlib}/File
%{_mandir}/*/*


%changelog
* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 597101
- update to 0.28

* Thu Jan 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 487043
- update to 0.24

* Sun Nov 22 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 468939
- update to 0.22

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-2mdv2010.0
+ Revision: 410182
- fix buildrequires
- force rebuild
- rebuild using %%perl_convert_version

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2010.0
+ Revision: 390329
- update to new version 0.20

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2009.1
+ Revision: 320560
- update to new version 0.18

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2009.1
+ Revision: 292159
- update to new version 0.16

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.14-3mdv2009.0
+ Revision: 256879
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2008.1
+ Revision: 138046
- update to new version 0.14

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2008.1
+ Revision: 105343
- fix build dependencies
- new version
- update to new version 0.12


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2007.0
+ Revision: 133684
- new version
- Import perl-File-Fetch

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2007.0
- New version 0.08
- drop patch 0 (merged)

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-2mdv2007.0
- fix handlers return status (CPAN bug #18942)

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdk
- first mdk release

