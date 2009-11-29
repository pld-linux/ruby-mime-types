# TODO:
# - MIME subdir in ri
Summary:	MIME::Types for Ruby
Summary(hu.UTF-8):	MIME::Types Rubyhoz
Summary(pl.UTF-8):	MIME::Types dla języka Ruby
Name:		ruby-mime-types
Version:	1.16
Release:	1
License:	Ruby's, Artistic or GPLv2+
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/52549/mime-types-%{version}.tar.gz
# Source0-md5:	70190fa0bd562f323449b151e7247333
URL:		http://raa.ruby-lang.org/project/mime-types/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb >= 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
MIME::Types provides the ability for detailed information about MIME
entities to be determined and used programmatically.

This is largely based on Perl MIME::Types 1.13. Please see the main
documentation for more information.

%description -l hu.UTF-8
MIME::Types egy felületet biztosít a MIME bejegyzések lekérdezéséhez
és programozásához.

Nagyban a Perl MIME::Types 1.13 az alapja a modulnak. A fő
dokumentációban találsz több információt.

%description -l pl.UTF-8
MIME::Types pozwala na programowe określanie i wykorzystywanie
szczegółowych informacji o elementach MIME.

Moduł ten jest w dużej części oparty na perlowym MIME::Types 1.13.
Więcej informacji znajduje się w głównej dokumentacji.

%package rdoc
Summary:	Documentation files for mime-types
Summary(hu.UTF-8):	A mime-types dokumentációja
Summary(pl.UTF-8):	Pliki dokumentacji do mime-types
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for mime-types.

%description rdoc -l hu.UTF-8
A mime-types dokumentációja.

%description rdoc -l pl.UTF-8
Pliki dokumentacji do mime-types.

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
rm -f ri/created.rid
rm -rf ri/MIME/InvalidContentType

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{ruby_rubylibdir}/mime
%{ruby_rubylibdir}/mime/types.rb
%{ruby_rubylibdir}/mime/types.rb.data

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%dir %{ruby_ridir}/MIME
%{ruby_ridir}/MIME/*.yaml
%{ruby_ridir}/MIME/Type
%{ruby_ridir}/MIME/Types
