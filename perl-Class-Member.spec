#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Class
%define	pnam	Member
Summary:	Class::Member - A set of modules to make the module developement easier
#Summary(pl.UTF-8):	
Name:		perl-Class-Member
Version:	1.6
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/O/OP/OPI/Class-Member-1.6.tar.gz
# Source0-md5:	43819bd7853c6c251e4bdf2bf1e81831
URL:		http://search.cpan.org/~opi/Class-Member/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl class instances are mostly blessed HASHes or GLOBs and store member
variables either as $self->{membername} or
${*$self}{membername} respectively.

This is very error prone when you start to develope derived classes based
on such modules. The developer of the derived class must watch the
member variables of the base class to avoid name conflicts.

To avoid that Class::Member::XXX stores member variables in its own
namespace prepending the package name to the variable name, e.g.

 package My::New::Module;

 use Class::Member::HASH qw/member_A memberB/;

will store member_A as $self->{'My::New::Module::member_A'}.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/*.pm
%{perl_vendorlib}/Class/Member
%{_mandir}/man3/*
