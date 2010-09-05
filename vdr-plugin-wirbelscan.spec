
%define plugin	wirbelscan
%define name	vdr-plugin-%plugin
%define version	0.0.5
%define pre	pre12a
%define rel	1

Summary:	VDR plugin: DVB and pvrinput channel scan
Name:		%name
Version:	%version
Release:	%mkrel 0.%pre.%rel
Group:		Video
License:	GPLv2+
URL:		http://wirbel.htpc-forum.de/wirbelscan/index2.html
Source:		http://wirbel.htpc-forum.de/wirbelscan/vdr-%plugin-%version-%pre.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This VDR plugin performs a channel scans for digital terrestrial and
digital cable TV and analog ivtv cards, satellite is also supported.

A service API is included to allow other plugins to use the scanning
capabilities of wirbelscan.

%prep
%setup -q -n %plugin-%version-%pre
# nice unaccessable directories...
chmod +x */

iconv -f ISO-8859-15 -t UTF-8 -o HISTORY.utf8 HISTORY
mv -f HISTORY.utf8 HISTORY

%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY

