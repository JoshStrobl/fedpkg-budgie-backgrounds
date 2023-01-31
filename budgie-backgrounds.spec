Name:           budgie-backgrounds
Version:        1.0
Release:        1%{?dist}
Summary:     Default set of background images for the Budgie Desktop

License:         CC0-1.0
URL:                https://github.com/BuddiesOfBudgie/budgie-backgrounds
Source0:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        https://serebit.com/openpgp/git-at-serebit-dot-com.asc

BuildArch: noarch
BuildRequires: ImageMagick
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: jhead
BuildRequires: meson

%description
Default set of background images for the Budgie Desktop.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/backgrounds/budgie
%dir %{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/budgie/*.jpg
%{_datadir}/gnome-background-properties/%{name}.xml

%changelog
* Sun Jan 29 2023 Joshua Strobl <me@joshuastrobl.com> - 1.0-1
- Initial inclusion of Budgie Backgrounds
