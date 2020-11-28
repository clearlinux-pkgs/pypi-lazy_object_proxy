#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lazy-object-proxy
Version  : 1.5.2
Release  : 46
URL      : https://files.pythonhosted.org/packages/95/b7/8823606ab25245effb6907fd7699f2234ae0bbd39e0c7b10b84def966f45/lazy-object-proxy-1.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/95/b7/8823606ab25245effb6907fd7699f2234ae0bbd39e0c7b10b84def966f45/lazy-object-proxy-1.5.2.tar.gz
Summary  : A fast and thorough lazy object proxy.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: lazy-object-proxy-license = %{version}-%{release}
Requires: lazy-object-proxy-python = %{version}-%{release}
Requires: lazy-object-proxy-python3 = %{version}-%{release}
Requires: pip
Requires: setuptools
Requires: six
Requires: twine
Requires: virtualenv
BuildRequires : buildreq-distutils3
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : six
BuildRequires : tox
BuildRequires : twine
BuildRequires : virtualenv

%description
Overview
        ========
        
        
        
        A fast and thorough lazy object proxy.

%package license
Summary: license components for the lazy-object-proxy package.
Group: Default

%description license
license components for the lazy-object-proxy package.


%package python
Summary: python components for the lazy-object-proxy package.
Group: Default
Requires: lazy-object-proxy-python3 = %{version}-%{release}

%description python
python components for the lazy-object-proxy package.


%package python3
Summary: python3 components for the lazy-object-proxy package.
Group: Default
Requires: python3-core
Provides: pypi(lazy_object_proxy)

%description python3
python3 components for the lazy-object-proxy package.


%prep
%setup -q -n lazy-object-proxy-1.5.2
cd %{_builddir}/lazy-object-proxy-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1606586159
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lazy-object-proxy
cp %{_builddir}/lazy-object-proxy-1.5.2/LICENSE %{buildroot}/usr/share/package-licenses/lazy-object-proxy/145bfd0484ce08e6fd2c5b7d07e10e7e18da1216
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lazy-object-proxy/145bfd0484ce08e6fd2c5b7d07e10e7e18da1216

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
