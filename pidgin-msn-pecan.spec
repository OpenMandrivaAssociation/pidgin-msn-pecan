Summary:	Alternative implementation of the MSN protocol plug-in for libpurple
Name:     	pidgin-msn-pecan
Version:	0.0.14
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
%setup_compile_flags
%make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m0755 libmsn-pecan.so %buildroot%{_libdir}/purple-2/libmsn-pecan.so

%clean
rm -rf $RPM_BUILD_ROOT
