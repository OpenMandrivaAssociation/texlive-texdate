Name:		texlive-texdate
Version:	49362
Release:	2
Summary:	Date printing, formatting, and manipulation in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texdate
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texdate.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeX and LaTeX provide few facilities for dates by default,
though many packages have filled this gap. This package fills
it, as well, with a pure TeX-primitive implementation. It can
print dates, advance them by numbers of days, weeks, or months,
determine the weekday automatically (with an algorithm cribbed
from the dayofweek.tex file written by Martin Minow), and print
them in (mostly) arbitrary format. It can also print calendars
(monthly and yearly) automatically, and can be easily localized
for non-English languages.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/texdate
%{_texmfdistdir}/tex/generic/texdate
%doc %{_texmfdistdir}/doc/generic/texdate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
