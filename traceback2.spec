#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : traceback2
Version  : 1.4.0
Release  : 63
URL      : http://pypi.debian.net/traceback2/traceback2-1.4.0.tar.gz
Source0  : http://pypi.debian.net/traceback2/traceback2-1.4.0.tar.gz
Source1  : http://pypi.debian.net/traceback2/traceback2-1.4.0.tar.gz.asc
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
BuildRequires : linecache2
BuildRequires : pbr
BuildRequires : testrepository
BuildRequires : testtools
BuildRequires : unittest2

%description
>>> import traceback2 as traceback
        
        Profit.
        
        Things to be aware of!
        
        In Python 2.x, unlike traceback, traceback2 creates unicode output (because it
        depends on the linecache2 module).
        
        Exception frame clearing silently does nothing if the interpreter in use does
        not support it.
        
        traceback2._some_str, which while not an official API is so old its likely in
        use behaves similarly to the Python3 version - objects where unicode(obj) fails
        but str(object) works will be shown as b'thestrvaluerepr'.

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
Provides: pypi(traceback2)
Requires: pypi(linecache2)

%description python3
python3 components for the traceback2 package.


%prep
%setup -q -n traceback2-1.4.0
cd %{_builddir}/traceback2-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603406446
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
