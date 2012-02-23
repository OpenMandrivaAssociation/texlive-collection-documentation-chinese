# revision 14384
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-chinese
Version:	20120223
Release:	1
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
