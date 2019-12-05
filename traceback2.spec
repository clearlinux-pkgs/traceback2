#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : traceback2
Version  : 1.4.0
Release  : 51
URL      : http://pypi.debian.net/traceback2/traceback2-1.4.0.tar.gz
Source0  : http://pypi.debian.net/traceback2/traceback2-1.4.0.tar.gz
Source99 : http://pypi.debian.net/traceback2/traceback2-1.4.0.tar.gz.asc
Summary  : Backports of the traceback module
Group    : Development/Tools
License  : Python-2.0
Requires: traceback2-python = %{version}-%{release}
Requires: traceback2-python3 = %{version}-%{release}
Requires: linecache2
BuildRequires : Babel
BuildRequires : buildreq-distutils3
BuildRequires : contextlib2
BuildRequires : fixtures
BuildRequires : pbr
BuildRequires : testrepository
BuildRequires : testtools
BuildRequires : unittest2

%description
A backport of traceback to older supported Pythons.
>>> import traceback2 as traceback

%package python
Summary: python components for the traceback2 package.
Group: Default
Requires: traceback2-python3 = %{version}-%{release}

%description python
python components for the traceback2 package.


%package python3
Summary: python3 components for the traceback2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the traceback2 package.


%prep
%setup -q -n traceback2-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554340140
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
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
