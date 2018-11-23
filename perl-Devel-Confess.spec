#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Confess
Version  : 0.009004
Release  : 17
URL      : https://www.cpan.org/authors/id/H/HA/HAARG/Devel-Confess-0.009004.tar.gz
Source0  : https://www.cpan.org/authors/id/H/HA/HAARG/Devel-Confess-0.009004.tar.gz
Summary  : 'Include stack traces on all warnings and errors'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Devel::Confess - Include stack traces on all warnings and errors
SYNOPSIS
Use on the command line:

%package dev
Summary: dev components for the perl-Devel-Confess package.
Group: Development
Provides: perl-Devel-Confess-devel = %{version}-%{release}

%description dev
dev components for the perl-Devel-Confess package.


%prep
%setup -q -n Devel-Confess-0.009004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Devel/Confess.pm
/usr/lib/perl5/vendor_perl/5.28.0/Devel/Confess/Builtin.pm
/usr/lib/perl5/vendor_perl/5.28.0/Devel/Confess/Source.pm
/usr/lib/perl5/vendor_perl/5.28.0/Devel/Confess/_Util.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::Confess.3
/usr/share/man/man3/Devel::Confess::Builtin.3
