Summary:	Alternative implementation of the MSN protocol plug-in for libpurple
Name:     	pidgin-msn-pecan
Version:	0.1.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/Instant messaging
Source0: 	http://msn-pecan.googlecode.com/files/msn-pecan-%version.tar.bz2
URL:		http://code.google.com/p/msn-pecan/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pidgin-devel

%description
This is an alternative implementation of the MSN protocol plug-in for
libpurple.

It's based on the code from 2.2.2 but slowly becoming a completely different
code.

Features include:

 * Support for personal messages
 * Server-side storage for display names (private alias)
 * Partial direct connection support (p2p transfers)
 * Improved network IO (using GIOChannel)
 * Improved error handling
 * Network issues tested with netem
 * GObject usage

%files
%defattr(-, root, root)
%doc README ChangeLog TODO
%{_libdir}/purple-2/libmsn-pecan.so

#---------------------------------------------------------------------
%prep
%setup -q -n msn-pecan-%version

%build
#gw don't use setup_compile_flags, we want to backport to 2008.1.
export CFLAGS="%optflags"
export LDFLAGS="%ldflags"
%make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m0755 libmsn-pecan.so %buildroot%{_libdir}/purple-2/libmsn-pecan.so

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Tue Aug 02 2011 Götz Waschk <waschk@mandriva.org> 0.1.3-1mdv2012.0
+ Revision: 692805
- new version

* Thu May 05 2011 Götz Waschk <waschk@mandriva.org> 0.1.2-1
+ Revision: 669258
- update to new version 0.1.2

* Sat Sep 04 2010 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 575803
- update to new version 0.1.1

* Sun Feb 28 2010 Götz Waschk <waschk@mandriva.org> 0.1.0-1mdv2010.1
+ Revision: 512509
- final 0.1.0 version

* Fri Feb 12 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.1.0-0.rc4.1mdv2010.1
+ Revision: 504571
- 0.1.0-rc4

* Fri Jan 29 2010 Götz Waschk <waschk@mandriva.org> 0.1.0-0.rc3.1mdv2010.1
+ Revision: 498134
- new prerelease

* Mon Jan 04 2010 Götz Waschk <waschk@mandriva.org> 0.1.0-0.rc2.1mdv2010.1
+ Revision: 486152
- new prerelease

* Mon Jul 20 2009 Götz Waschk <waschk@mandriva.org> 0.1.0-0.rc1.1mdv2010.0
+ Revision: 398050
- new version

* Wed Jun 24 2009 Götz Waschk <waschk@mandriva.org> 0.0.19-1mdv2010.0
+ Revision: 388848
- update to new version 0.0.19

* Mon Feb 16 2009 Götz Waschk <waschk@mandriva.org> 0.0.18-1mdv2009.1
+ Revision: 340726
- update to new version 0.0.18
- spec fix for backports

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 0.0.17-1mdv2009.1
+ Revision: 308554
- update to new version 0.0.17

* Wed Oct 22 2008 Götz Waschk <waschk@mandriva.org> 0.0.16-1mdv2009.1
+ Revision: 296399
- update to new version 0.0.16

* Fri Jul 25 2008 Funda Wang <fwang@mandriva.org> 0.0.14-1mdv2009.0
+ Revision: 248339
- import pidgin-msn-pecan


