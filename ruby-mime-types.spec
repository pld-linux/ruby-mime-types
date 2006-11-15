Summary:	MIME::Types for Ruby
Summary(pl):	MIME::Types dla jêzyka Ruby
Name:		ruby-mime-types
Version:	1.13.1
Release:	1
License:	Ruby's, Artistic or GPLv2+
Group:		Development/Languages
Source0:	http://raa.ruby-lang.org/cache/mime-types/mime-types-%{version}.tar.gz
# Source0-md5:	49fb7abf6730ebae1e32fc2d8ccc928e
URL:		http://raa.ruby-lang.org/project/mime-types/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Types provides the ability for detailed information about MIME
entities to be determined and used programmatically.

This is largely based on Perl MIME::Types 1.13. Please see the main
documentation for more information.

%description -l pl
MIME::Types pozwala na programowe okre¶lanie i wykorzystywanie
szczegó³owych informacji o elementach MIME.

Modu³ ten jest w du¿ej czê¶ci oparty na perlowym MIME::Types 1.13.
Wiêcej informacji znajduje siê w g³ównej dokumentacji.

%prep
%setup -q -n mime-types-%{version}
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
