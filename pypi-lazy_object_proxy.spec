#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-lazy_object_proxy
Version  : 1.9.0
Release  : 70
URL      : https://files.pythonhosted.org/packages/20/c0/8bab72a73607d186edad50d0168ca85bd2743cfc55560c9d721a94654b20/lazy-object-proxy-1.9.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/20/c0/8bab72a73607d186edad50d0168ca85bd2743cfc55560c9d721a94654b20/lazy-object-proxy-1.9.0.tar.gz
Summary  : A fast and thorough lazy object proxy.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: pypi-lazy_object_proxy-filemap = %{version}-%{release}
Requires: pypi-lazy_object_proxy-lib = %{version}-%{release}
Requires: pypi-lazy_object_proxy-python = %{version}-%{release}
Requires: pypi-lazy_object_proxy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pip)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(six)
BuildRequires : pypi(tox)
BuildRequires : pypi(twine)
BuildRequires : pypi(virtualenv)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
========
Overview
========
.. start-badges
.. list-table::
:stub-columns: 1
* - docs
- |docs|
* - tests
- | |github-actions| |requires|
| |coveralls| |codecov|
* - package
- | |version| |wheel| |supported-versions| |supported-implementations|
| |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-lazy-object-proxy/badge/?style=flat
:target: https://python-lazy-object-proxy.readthedocs.io/
:alt: Documentation Status

%package filemap
Summary: filemap components for the pypi-lazy_object_proxy package.
Group: Default

%description filemap
filemap components for the pypi-lazy_object_proxy package.


%package lib
Summary: lib components for the pypi-lazy_object_proxy package.
Group: Libraries
Requires: pypi-lazy_object_proxy-filemap = %{version}-%{release}

%description lib
lib components for the pypi-lazy_object_proxy package.


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
Requires: pypi(pip)
Requires: pypi(six)
Requires: pypi(tox)
Requires: pypi(twine)
Requires: pypi(virtualenv)

%description python3
python3 components for the pypi-lazy_object_proxy package.


%prep
%setup -q -n lazy-object-proxy-1.9.0
cd %{_builddir}/lazy-object-proxy-1.9.0
pushd ..
cp -a lazy-object-proxy-1.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672933125
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-lazy_object_proxy

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
