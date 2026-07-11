%global tl_name texdate
%global tl_revision 49362

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Date printing, formatting, and manipulation in TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/texdate
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdate.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texdate.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX and LaTeX provide few facilities for dates by default, though many
packages have filled this gap. This package fills it, as well, with a
pure TeX-primitive implementation. It can print dates, advance them by
numbers of days, weeks, or months, determine the weekday automatically
(with an algorithm cribbed from the dayofweek.tex file written by Martin
Minow), and print them in (mostly) arbitrary format. It can also print
calendars (monthly and yearly) automatically, and can be easily
localized for non-English languages.

