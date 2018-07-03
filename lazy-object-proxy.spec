#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lazy-object-proxy
Version  : 1.3.1
Release  : 25
URL      : http://pypi.debian.net/lazy-object-proxy/lazy-object-proxy-1.3.1.tar.gz
Source0  : http://pypi.debian.net/lazy-object-proxy/lazy-object-proxy-1.3.1.tar.gz
Summary  : A fast and thorough lazy object proxy.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: lazy-object-proxy-python3
Requires: lazy-object-proxy-python
Requires: Sphinx
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
Overview
        ========
        
        
        
        A fast and thorough lazy object proxy.

%package python
Summary: python components for the lazy-object-proxy package.
Group: Default
Requires: lazy-object-proxy-python3

%description python
python components for the lazy-object-proxy package.


%package python3
Summary: python3 components for the lazy-object-proxy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the lazy-object-proxy package.


%prep
%setup -q -n lazy-object-proxy-1.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523290981
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
