%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname Werkzeug

Name:           python-werkzeug
Version:        0.9.3
Release:        2%{?dist}
Summary:        The Swiss Army knife of Python web development 

Group:          Development/Libraries
License:        BSD
URL:            http://werkzeug.pocoo.org/
Source0:        http://pypi.python.org/packages/source/W/Werkzeug/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel
BuildRequires:  python-sphinx10
BuildRequires:  python-jinja2-27

%description
Werkzeug
========

Werkzeug started as simple collection of various utilities for WSGI
applications and has become one of the most advanced WSGI utility
modules.  It includes a powerful debugger, full featured request and
response objects, HTTP utilities to handle entity tags, cache control
headers, HTTP dates, cookie handling, file uploads, a powerful URL
routing system and a bunch of community contributed addon modules.

Werkzeug is unicode aware and doesn't enforce a specific template
engine, database adapter or anything else.  It doesn't even enforce
a specific way of handling requests and leaves all that up to the
developer. It's most useful for end user applications which should work
on as many server environments as possible (such as blogs, wikis,
bulletin boards, etc.).

%package doc
Summary:        Documentation for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}


%description doc
Documentation and examples for %{name}.

%prep
%setup -q -n %{srcname}-%{version}
%{__sed} -i 's/\r//' LICENSE
%{__sed} -i '1d' werkzeug/testsuite/multipart/collect.py
%{__sed} -i "2i __requires__ = ['Jinja2>=2.7']" setup.py


%build
%{__python} setup.py build build_sphinx
find examples/ -name '*.py' -executable | xargs chmod -x
find examples/ -name '*.png' -executable | xargs chmod -x

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
%{__rm} -rf examples/cupoftee/db.pyc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS LICENSE PKG-INFO CHANGES
%{python_sitelib}/*

%files doc
%defattr(-,root,root,-)
%doc build/sphinx/html examples

%changelog
* Tue Feb 11 2014 Johan De Wit <johan@open-future.be> - 0.9.3-1
- Updated to version 0.9.3 - puppetboard

* Fri Jul 13 2012 Ricky Elrod <codeblock@fedoraproject.org> - 0.8.3-2
- Start the process of getting Werkzeug in EPEL 6.

* Sun Feb  5 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.3-1
- upstream 0.8.3 (fixes XSS security issues)

* Wed Jan 25 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 0.8.2-1
- upstream 0.8.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun May 23 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6.2-1
- Updating because upstream release of Werkzeug 0.6.2

* Sat Mar 05 2010 Peter Halliday <phalliday@excelsiorsystems.net> - 0.6-1
- Updating because upstream release of Werkzeug 0.6

* Tue Aug 25 2009 Peter Halliday <phalliday@excelsiorsystems.net> - 0.5.1-1
- Initial package
