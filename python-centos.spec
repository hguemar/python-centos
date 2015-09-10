%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:		python-centos
Version:	0.0.4
Release:	1%{?dist}
Summary:	Python bindings for the CentOS account system, CBS and other services

Group:		Applications/System
License:	GPLv2
URL:		https://centos.org/
Source0:	python-centos-%{version}.tar.gz

BuildRequires:	python-devel, python-setuptools
Requires:	python-requests, python-fedora
Requires:   pyOpenSSL

BuildArch: noarch

%description
Provides python bindings for the infrastructure services in the CentOS project

%prep
%setup -q -c -n %{name}-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc COPYING
%{python_sitelib}/*

%changelog
* Thu Sep 03 2015 brian@bstinson.com 0.0.4-1
- Add the AccountSystem and a BR for python-fedora

* Tue Aug 11 2015 brian@bstinson.com 0.0.2-1
- Updated to dev version of library defaults 

* Sun Jul 26 2015 brian@bstinson.com 0.0.1-1
- First build


