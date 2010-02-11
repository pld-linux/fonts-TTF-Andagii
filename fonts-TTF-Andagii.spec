Summary:	Free TrueType font for Osmanya, Ugaritic and Shavian scripts
Summary(pl.UTF-8):	Wolnodostępny font TrueType dlapism: osmanija, ugaryckiego i Shawa
Name:		fonts-TTF-Andagii
Version:	1.0
Release:	1
License:	Copyleft
Group:		Fonts
Source0:	http://www.i18nguy.com/unicode/andagii.zip
# Source0-md5:	cb4c49de7e3af594e87e4e4ad9d06f42
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Mark Williamson has created a TrueType font for the Osmanya script
named Andagii. The font file also supports Ugaritic and Shavian.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.TTF $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%{ttffontsdir}/*.TTF
