#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-lazy_object_proxy
Version  : 1.6.0
Release  : 59
URL      : https://files.pythonhosted.org/packages/bb/f5/646893a04dcf10d4acddb61c632fd53abb3e942e791317dcdd57f5800108/lazy-object-proxy-1.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/bb/f5/646893a04dcf10d4acddb61c632fd53abb3e942e791317dcdd57f5800108/lazy-object-proxy-1.6.0.tar.gz
Summary  : A fast and thorough lazy object proxy.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-lazy_object_proxy-filemap = %{version}-%{release}
Requires: pypi-lazy_object_proxy-lib = %{version}-%{release}
Requires: pypi-lazy_object_proxy-license = %{version}-%{release}
Requires: pypi-lazy_object_proxy-python = %{version}-%{release}
Requires: pypi-lazy_object_proxy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(pip)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(six)
BuildRequires : pypi(twine)
BuildRequires : pypi(virtualenv)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
Patch1: deps.patch

%description
Overview
        ========
        
        
        
        A fast and thorough lazy object proxy.

%package filemap
Summary: filemap components for the pypi-lazy_object_proxy package.
Group: Default

%description filemap
filemap components for the pypi-lazy_object_proxy package.


%package lib
Summary: lib components for the pypi-lazy_object_proxy package.
Group: Libraries
Requires: pypi-lazy_object_proxy-license = %{version}-%{release}
Requires: pypi-lazy_object_proxy-filemap = %{version}-%{release}

%description lib
lib components for the pypi-lazy_object_proxy package.


%package license
Summary: license components for the pypi-lazy_object_proxy package.
Group: Default

%description license
license components for the pypi-lazy_object_proxy package.


%package python
Summary: python components for the pypi-lazy_object_proxy package.
Group: Default
Requires: pypi-lazy_object_proxy-python3 = %{version}-%{release}

%description python
python components for the pypi-lazy_object_proxy package.


%package python3
Summary: python3 components for the pypi-lazy_object_proxy package.
Group: Default
Requires: pypi-lazy_object_proxy-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(lazy_object_proxy)

%description python3
python3 components for the pypi-lazy_object_proxy package.


%prep
%setup -q -n lazy-object-proxy-1.6.0
cd %{_builddir}/lazy-object-proxy-1.6.0
%patch1 -p1
pushd ..
cp -a lazy-object-proxy-1.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653341545
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-lazy_object_proxy
cp %{_builddir}/lazy-object-proxy-1.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-lazy_object_proxy/145bfd0484ce08e6fd2c5b7d07e10e7e18da1216
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-lazy_object_proxy

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-lazy_object_proxy/145bfd0484ce08e6fd2c5b7d07e10e7e18da1216

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
