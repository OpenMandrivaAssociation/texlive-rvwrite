Name:		texlive-rvwrite
Version:	19614
Release:	2
Summary:	Increase the number of available output streams in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rvwrite
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rvwrite.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rvwrite.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package addresses, for LaTeX documents, the severe
limitation on the number of output streams that TeX provides.
The package uses a single TeX output stream, and writes
"marked-up" output to this stream. The user may then post-
process the marked-up output file, using LaTeX, and the
document's output appears as separate files, according to the
calls made to the package. The output to be post-processed uses
macros from the widely-available ProTeX package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rvwrite/rvwrite.sty
%doc %{_texmfdistdir}/doc/latex/rvwrite/Makefile
%doc %{_texmfdistdir}/doc/latex/rvwrite/README
%doc %{_texmfdistdir}/doc/latex/rvwrite/rvwrite-doc.pdf
%doc %{_texmfdistdir}/doc/latex/rvwrite/rvwrite-doc.tex
%doc %{_texmfdistdir}/doc/latex/rvwrite/test.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
