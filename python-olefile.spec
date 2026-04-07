%define module olefile

Name:		python-olefile
Version:	0.47
Release:	1
Group:		Development/Python
Summary:	Foreign Function Interface for Python calling C code
License:	BSD-2-Clause
URL:		https://github.com/decalage2/olefile
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

# Redirect anyone still using dead py2 to py3 module
%rename python2-olefile

%description
Foreign Function Interface for Python calling C code.
The aim of this project is to provide a convenient and 
reliable way of calling C code from Python. 
The interface is based on LuaJIT’s FFI 

%files
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}*.*-info
