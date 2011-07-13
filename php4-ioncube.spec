%ifarch %{ix86}
%define         ver     4.0.9
%endif
%ifarch %{x8664}
%define         ver     4.0.9
%endif
%ifarch ppc
%define         ver     3.1.33
%endif
%define		_name		ioncube
Summary:	ionCube loader module for PHP
Summary(pl.UTF-8):	Moduł wczytujący ionCube dla PHP
Name:		php4-%{_name}
Version:	%{ver}
Release:	1
License:	redistributable
Group:		Libraries
Source0:	http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86.tar.bz2
# Source0-md5:	fbf099576e0c2e869f24de5fdde2c6d7
Source1:	http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.bz2
# Source1-md5:	97c56bc8ff9fc3f9bba442c178b804d2
Source2:	http://downloads2.ioncube.com/loader_downloads/ioncube_loaders_lin_ppc.tar.bz2
# Source2-md5:	c9f44f2245e41cba0617c452488c3dc4
URL:		http://www.ioncube.com/
BuildRequires:	php4-devel >= 3:4.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php4-common >= 3:4.4.0-3
ExclusiveArch:	%{ix86} %{x8664} ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ionCube loader module for PHP.

%description -l pl.UTF-8
Moduł wczytujący ionCube dla PHP.

%prep
%ifarch %{ix86}
%setup -q -T -b 0 -n %{_name}
%endif
%ifarch %{x8664}
%setup -q -T -b 1 -n %{_name}
%endif
%ifarch ppc
%setup -q -T -b 2 -n %{_name}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_extensiondir},%{php_sysconfdir}/conf.d}

install $(ls -1 *lin_4.*_ts.so  | sort | tail -n 1) $RPM_BUILD_ROOT%{php_extensiondir}/%{_name}.so
echo "zend_extension_ts=%{php_extensiondir}/%{_name}.so" > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_name}.ini

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php4_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php4_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc *.txt *.php
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_name}.ini
%attr(755,root,root) %{php_extensiondir}/ioncube.so
