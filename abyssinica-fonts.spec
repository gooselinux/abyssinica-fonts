%define fontname        abyssinica

Name:           %{fontname}-fonts
Version:        1.0
Release:        5.1%{?dist}
Summary:        SIL Abyssinica fonts

Group:          User Interface/X
License:        OFL
URL:            http://scripts.sil.org/AbyssinicaSIL_Download
# download from http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=AbyssinicaSIL1.0.zip&filename=AbyssinicaSIL1.0.zip
Source0:        AbyssinicaSIL%{version}.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

Requires:       fontpackages-filesystem
BuildRequires:  fontpackages-devel
BuildRequires:  dos2unix

# Providing the name of an upstream RPM
Provides:       fonts-sil-abyssinica = %{version}-%{release}

%description

SIL Abyssinica is a Unicode typeface family containing glyphs for the
Ethiopic script.

The Ethiopic script is used for writing many of the languages of Ethiopia and
Eritrea. Abyssinica SIL supports all Ethiopic characters which are in Unicode
including the Unicode 4.1 extensions. Some languages of Ethiopia are not yet
able to be fully represented in Unicode and, where necessary, we have included
non-Unicode characters in the Private Use Area (see Private-use (PUA)
characters supported by Abyssinica SIL).

Abyssinica SIL is based on Ethiopic calligraphic traditions. This release is
a regular typeface, with no bold or italic version available or planned.

%prep
%setup -q -c


%build
dos2unix FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt


%install
rm -rf %{buildroot}

#fonts
install -d -m 0755 %{buildroot}%{_fontdir}
install -m 0644 *.ttf %{buildroot}%{_fontdir}


%clean
rm -rf %{buildroot}


%_font_pkg *.ttf

%doc FONTLOG.txt OFL.txt OFL-FAQ.txt README.txt
%dir %{_fontdir}

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.0-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Bernie Innocenti <bernie@codewiz.org> 1.0-3
- Updated to current Fedora font packaging guidelines

* Thu Oct 04 2007 Todd Zullinger <tmz@pobox.com> 1.0-2
- use upstream zip file as Source0
- fix license tag

* Fri Sep 14 2007 Bernardo Innocenti <bernie@codewiz.org> 1.0-1
- Initial packaging, borrowing many things from gentium-fonts
