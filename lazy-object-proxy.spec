#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lazy-object-proxy
Version  : 1.2.2
Release  : 10
URL      : http://pypi.debian.net/lazy-object-proxy/lazy-object-proxy-1.2.2.tar.gz
Source0  : http://pypi.debian.net/lazy-object-proxy/lazy-object-proxy-1.2.2.tar.gz
Summary  : A fast and thorough lazy object proxy.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: lazy-object-proxy-python
Requires: Sphinx
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

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
- | |travis| |appveyor| |requires|
| |coveralls| |codecov|
| |landscape| |scrutinizer| |codacy| |codeclimate|
* - package
- |version| |downloads| |wheel| |supported-versions| |supported-implementations|

%package python
Summary: python components for the lazy-object-proxy package.
Group: Default

%description python
python components for the lazy-object-proxy package.


%prep
%setup -q -n lazy-object-proxy-1.2.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488044519
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1488044519
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
