# revision 19614
# category Package
# catalog-ctan /macros/latex/contrib/rvwrite
# catalog-date 2010-08-31 12:08:50 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-rvwrite
Version:	1.2
Release:	2
Summary:	Increase the number of available output streams in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rvwrite
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rvwrite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rvwrite.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 755783
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719475
- texlive-rvwrite
- texlive-rvwrite
- texlive-rvwrite
- texlive-rvwrite

