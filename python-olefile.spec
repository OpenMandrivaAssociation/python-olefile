%define pypi_name olefile

Name:           python-%{pypi_name}
Version:        0.46
Release:        2
Group:          Development/Python
Summary:        Foreign Function Interface for Python calling C code
BuildArch:	noarch
License:        MIT
URL:            http://pypi.python.org/pypi/olefile
Source0:	https://github.com/decalage2/olefile/archive/v%{version}.tar.gz
BuildRequires:  python-sphinx

BuildRequires:  pkgconfig(python2)
BuildRequires:  python2-setuptools
BuildRequires:  python2-cython
BuildRequires:  python2-cparser
 
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
BuildRequires:  python-cython
BuildRequires:  python-cparser
 

%description
Foreign Function Interface for Python calling C code.
The aim of this project is to provide a convenient and 
reliable way of calling C code from Python. 
The interface is based on LuaJIT’s FFI 

%package -n     python2-%{pypi_name}
Summary:        Foreign Function Interface for Python calling C code
 

%description -n python2-%{pypi_name}
Foreign Function Interface for Python 3 calling C code.
The aim of this project is to provide a convenient and 
reliable way of calling C code from Python 3. 
The interface is based on LuaJIT’s FFI 

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'


%build
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%endif

pushd %{py2dir}
CFLAGS="%{optflags}" %{__python2} setup.py build build_ext -ldl
popd

CFLAGS="%{optflags}" %{__python} setup.py build build_ext -ldl

%install
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%{__python} setup.py install --skip-build --root %{buildroot}

%files
%{py_puresitedir}/%{pypi_name}
%{py_puresitedir}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name}
%{py2_puresitedir}/%{pypi_name}
%{py2_puresitedir}/%{pypi_name}-%{version}-py?.?.egg-info
