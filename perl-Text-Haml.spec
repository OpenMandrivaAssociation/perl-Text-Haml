%define upstream_name    Text-Haml
%define upstream_version 0.990116

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    2

Summary:    Haml Perl implementation

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CPAN::Meta)
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Section::Simple)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(Test::More)
BuildArch:  noarch

%description
the Text::Haml manpage implements Haml the
http://haml-lang.com/docs/yardoc/file.HAML_REFERENCE.html manpage
specification.

the Text::Haml manpage passes specification tests written by Norman Clarke
http://github.com/norman/haml-spec and supports only cross-language Haml
features. Do not expect Ruby specific things to work.

%prep
%autosetup -p1 -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot}
rm -f %{buildroot}/%{perl_vendorlib}/Text/README.pod

%files
%doc META.json META.yml MYMETA.yml
%doc %{_mandir}/man3/*
%{perl_vendorlib}/*
