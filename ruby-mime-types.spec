%define pkgname mime-types
Summary:	MIME::Types for Ruby
Summary(hu.UTF-8):	MIME::Types Rubyhoz
Summary(pl.UTF-8):	MIME::Types dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.16
Release:	3
License:	Ruby's, Artistic or GPL v2+
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	2c9b8568a76cc632578a292db4a71b9a
URL:		http://raa.ruby-lang.org/project/mime-types/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{ruby_vendorlibdir}/mime
%{ruby_vendorlibdir}/mime/types.rb
%{ruby_vendorlibdir}/mime/types.rb.data

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/MIME
