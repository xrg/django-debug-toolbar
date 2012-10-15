%define git_repo django-debug-toolbar
%define git_head HEAD

%define realname django-debug-toolbar
%define name    python-%{realname}

Name:           %{name}
Version:	%git_get_ver
Release:        %mkrel %git_get_rel
Summary:        Panels for debugging of Django
Group:          Development/Python
License:        BSD
URL:            https://github.com/django-debug-toolbar/django-debug-toolbar
Source:         %git_bs_source %{name}-%{version}.tar.gz
Source1:	%{name}-gitrpm.version
Source2:	%{name}-changelog.gitrpm.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
A configurable set of panels that display various debug information about the
current request/response.

%prep
%git_get_source
%setup -q

%build
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}
rm -rf %{buildroot}/usr/templates

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.rst LICENSE AUTHORS
%{py_puresitedir}/debug_toolbar
%{py_puresitedir}/django_debug_toolbar-%{version}-py%{pyver}.egg-info

%changelog -f %{_sourcedir}/%{name}-changelog.gitrpm.txt

