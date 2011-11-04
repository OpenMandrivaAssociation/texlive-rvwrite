# revision 19614
# category Package
# catalog-ctan /macros/latex/contrib/rvwrite
# catalog-date 2010-08-31 12:08:50 +0200
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-rvwrite
Version:	1.2
Release:	1
Summary:	Increase the number of available output streams in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rvwrite
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rvwrite.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rvwrite.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package addresses, for LaTeX documents, the severe
limitation on the number of output streams that TeX provides.
The package uses a single TeX output stream, and writes
"marked-up" output to this stream. The user may then post-
process the marked-up output file, using LaTeX, and the
document's output appears as separate files, according to the
calls made to the package. The output to be post-processed uses
macros from the widely-available ProTeX package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rvwrite/rvwrite.sty
%doc %{_texmfdistdir}/doc/latex/rvwrite/Makefile
%doc %{_texmfdistdir}/doc/latex/rvwrite/README
%doc %{_texmfdistdir}/doc/latex/rvwrite/rvwrite-doc.pdf
%doc %{_texmfdistdir}/doc/latex/rvwrite/rvwrite-doc.tex
%doc %{_texmfdistdir}/doc/latex/rvwrite/test.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
