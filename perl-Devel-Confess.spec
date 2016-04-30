#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-Confess
Version  : 0.008000
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Devel-Confess-0.008000.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Devel-Confess-0.008000.tar.gz
Summary  : 'Include stack traces on all warnings and errors'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Devel-Confess-doc

%description
NAME
Devel::Confess - Include stack traces on all warnings and errors
SYNOPSIS
Use on the command line:

%package doc
Summary: doc components for the perl-Devel-Confess package.
Group: Documentation

%description doc
doc components for the perl-Devel-Confess package.


%prep
%setup -q -n Devel-Confess-0.008000

%build
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/Devel/Confess.pm
/usr/lib/perl5/site_perl/5.22.0/Devel/Confess/Builtin.pm
/usr/lib/perl5/site_perl/5.22.0/Devel/Confess/Source.pm
/usr/lib/perl5/site_perl/5.22.0/Devel/Confess/_Util.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
