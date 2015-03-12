#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : traceback2
Version  : 1.4.0
Release  : 5
URL      : https://pypi.python.org/packages/source/t/traceback2/traceback2-1.4.0.tar.gz
Source0  : https://pypi.python.org/packages/source/t/traceback2/traceback2-1.4.0.tar.gz
Summary  : Backports of the traceback module
Group    : Development/Tools
License  : Python-2.0
Requires: traceback2-python
BuildRequires : contextlib2
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures
BuildRequires : linecache2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository
BuildRequires : testtools
BuildRequires : unittest2

%description
A backport of traceback to older supported Pythons.
>>> import traceback2 as traceback

%package python
Summary: python components for the traceback2 package.
Group: Default

%description python
python components for the traceback2 package.


%prep
%setup -q -n traceback2-1.4.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
