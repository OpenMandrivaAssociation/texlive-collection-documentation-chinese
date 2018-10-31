# revision 14384
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-chinese
Epoch:		1
Version:	20120224
Release:	10
Summary:	Chinese documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-chinese.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-ctex-faq
Requires:	texlive-latex-notes-zh-cn
Requires:	texlive-lshort-chinese
Requires:	texlive-texlive-zh-cn
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-chinese package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780208
- Update to latest release.
- Import texlive-collection-documentation-chinese
- Import texlive-collection-documentation-chinese

