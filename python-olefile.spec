%define pypi_name olefile

Name:           python-%{pypi_name}
Version:        0.44
Release:        1
Group:          Development/Python
Summary:        Foreign Function Interface for Python calling C code
BuildArch:	noarch
License:        MIT
URL:            http://cffi.readthedocs.org/
Source0:	https://pypi.python.org/packages/35/17/c15d41d5a8f8b98cc3df25eb00c5cee76193114c78e5674df6ef4ac92647/%{pypi_name}-%{version}.zip
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
%{py_puresitedir}/Ole*

%files -n python2-%{pypi_name}
%{py2_puresitedir}/%{pypi_name}
%{py2_puresitedir}/%{pypi_name}-%{version}-py?.?.egg-info
%{py2_puresitedir}/Ole*
