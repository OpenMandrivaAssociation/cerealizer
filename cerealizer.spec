%define name    cerealizer
%define oname   Cerealizer
%define version 0.7

Name:           %{name}
Version:        0.8.1
Release:        1
License:        GPL
Url:		http://home.gna.org/oomadness/fr/cerealizer/index.html
Source:		http://download.gna.org/soya/Cerealizer-%{version}.tar.bz2
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




%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.7-4mdv2011.0
+ Revision: 592376
- rebuild for python 2.7

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.7-3mdv2010.0
+ Revision: 436990
- rebuild

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.7-2mdv2009.1
+ Revision: 324175
- rebuild

* Sat Sep 06 2008 Emmanuel Andry <eandry@mandriva.org> 0.7-1mdv2009.0
+ Revision: 281879
- New version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.6-3mdv2009.0
+ Revision: 243474
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 15 2007 Emmanuel Andry <eandry@mandriva.org> 0.6-1mdv2008.1
+ Revision: 120399
- New version

* Tue Sep 11 2007 Emmanuel Andry <eandry@mandriva.org> 0.5-2mdv2008.0
+ Revision: 84538
- rebuild


* Sat Dec 16 2006 Olivier Blin <oblin@mandriva.com> 0.5-1mdv2007.0
+ Revision: 98150
- 0.5 (with register_alias support, #24821)

* Fri Dec 15 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-3mdv2007.1
+ Revision: 97486
- Fix File list
- Fix File list
- Rebuild against new python
- Import cerealizer

* Tue Jul 11 2006 Lenny Cartier <lenny@mandriva.com> 0.4-1mdv2007.0
- new


