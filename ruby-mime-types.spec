%define pkgname mime-types
Summary:	MIME::Types for Ruby
Summary(hu.UTF-8):	MIME::Types Rubyhoz
Summary(pl.UTF-8):	MIME::Types dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.23
Release:	3
License:	MIT, Artistic or GPL v2+
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	26b9ebe2f50e7ed6348475f7c520cfaf
URL:		http://mime-types.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %(locale -a | grep -q '^en_US$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Types provides the ability for detailed information about MIME
entities to be determined and used programmatically.

%description -l hu.UTF-8
MIME::Types egy felületet biztosít a MIME bejegyzések lekérdezéséhez
és programozásához.

%description -l pl.UTF-8
MIME::Types pozwala na programowe określanie i wykorzystywanie
szczegółowych informacji o elementach MIME.

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
%__gem_helper spec

# rdoc fails if not UTF-8 locale
export LC_ALL=en_US.UTF-8
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

install -d $RPM_BUILD_ROOT%{ruby_specdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rdoc History.rdoc Licence.rdoc
%dir %{ruby_vendorlibdir}/mime
%{ruby_vendorlibdir}/mime-types.rb
%{ruby_vendorlibdir}/mime/types.rb
%{ruby_vendorlibdir}/mime/types
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/MIME
