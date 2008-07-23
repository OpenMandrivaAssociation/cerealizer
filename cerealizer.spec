%define name    cerealizer
%define oname   Cerealizer
%define version 0.6

Name:           %{name}
Version:        %{version}
Release:        %mkrel 3
License:        GPL
Url:		http://home.gna.org/oomadness/fr/cerealizer/index.html
Source:		http://download.gna.org/soya/%{oname}-%{version}.tar.bz2
Group:          Development/Python
Summary:        Python module that allows to save objects in file
BuildRequires:  python-devel 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch:	noarch

%description
Python module that allows to save objects in file

%prep
%setup -q  -n %{oname}-%{version}
rm -rf `find -name CVS` `find -name .cvswrappers`

%build

%{__python} setup.py build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%py_puresitedir/%{name}
%py_puresitedir/*.egg-info


