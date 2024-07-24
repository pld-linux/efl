# TODO:
# - Xpresent
# - use system liblinebreak?
# - eio-devel conflicts with libeio-devel
#	file /usr/lib64/libeio.so from install of eio-devel-0.1.0.65643-1.x86_64 conflicts with file from package libeio-devel-1.0-1.x86_64
#
# Conditional build:
%bcond_without	drm		# DRM engine
%bcond_without	egl		# EGL rendering support
%bcond_without	fb		# Linux FrameBuffer support
%bcond_without	gstreamer	# GStreamer support
%bcond_with	gesture		# Xgesture support in Ecore_X
%bcond_without	harfbuzz	# HarfBuzz complex text shaping and layouting support
%bcond_without	ibus		# IBus input module
%bcond_without	luajit		# LuaJIT as Lua engine (Lua 5.1 interpreter if disabled)
%bcond_with	pixman		# pixman for software rendering
%bcond_without	scim		# SCIM input module
%bcond_without	sdl		# SDL support
%bcond_with	systemd		# systemd journal support in Eina, daemon support in Ecore
%bcond_without	wayland		# Wayland display server support
%bcond_with	wayland_egl	# Wayland display server support [only with GLES instead of GL]
%bcond_with	xcb		# use XCB API instead of Xlib
%bcond_without	xine		# Xine support
%bcond_with	gnutls		# use GnuTLS as crypto library (default is OpenSSL)
%bcond_without	static_libs	# static libraries build
#
%ifnarch %{ix86} %{x8664} %{arm} mips ppc
%undefine	with_luajit
%endif
Summary:	EFL - The Enlightenment Foundation Libraries
Summary(pl.UTF-8):	EFL (Enlightenment Foundation Libraries) - biblioteki tworzące Enlightment
Name:		efl
Version:	1.10.3
Release:	9
License:	LGPL v2.1+, BSD (depends on component)
Group:		Libraries
Source0:	https://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.bz2
# Source0-md5:	6b3d88134d3d27dd9b41a4a46d718a19
Patch0:		%{name}-pc.patch
Patch1:		%{name}-wayland.patch
Patch2:		%{name}-am.patch
URL:		https://www.enlightenment.org/docs/efl/start
%{?with_egl:BuildRequires:	EGL-devel}
BuildRequires:	OpenGL-GLX-devel
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.0}
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1.6
BuildRequires:	avahi-devel
BuildRequires:	bullet-devel >= 2.80
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	fontconfig-devel >= 2.5.0
BuildRequires:	freetype-devel >= 1:2.2
BuildRequires:	fribidi-devel >= 0.19.2
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 2.0
%{?with_gnutls:BuildRequires:	gnutls-devel >= 2.12.16}
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
%endif
%{?with_harfbuzz:BuildRequires:	harfbuzz-devel >= 0.9.0}
%{?with_ibus:BuildRequires:	ibus-devel >= 1.4}
%{?with_drm:BuildRequires:	libdrm-devel >= 2.4}
%{?with_gnutls:BuildRequires:	libgcrypt-devel >= 1.2.0}
BuildRequires:	libjpeg-devel
BuildRequires:	libmount-devel >= 2.18.0
BuildRequires:	libpng-devel >= 1.2.10
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwebp-devel
%{!?with_luajit:BuildRequires:	lua51 >= 5.1.0}
%{?with_luajit:BuildRequires:	luajit >= 2.0.0}
BuildRequires:	libtool >= 2:2
BuildRequires:	openjpeg2-devel >= 2
%{!?with_gnutls:BuildRequires:	openssl-devel}
%if %{with pixman} || %{with xcb}
BuildRequires:	pixman-devel
%endif
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	pulseaudio-devel
%{?with_scim:BuildRequires:	scim-devel}
%{?with_systemd:BuildRequires:	systemd-devel >= 1:192}
BuildRequires:	tslib-devel
BuildRequires:	udev-devel >= 1:148
%{?with_xine:BuildRequires:	xine-lib-devel >= 2:1.1.1}
%{?with_gesture:BuildRequires:	xorg-lib-libXgesture-devel}
%if %{with drm} || %{with wayland}
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.3.0
%endif
BuildRequires:	zlib-devel >= 1.2.3
%if %{with xcb}
BuildRequires:	libxcb-devel
BuildRequires:	xcb-util-devel >= 0.3.8
BuildRequires:	xcb-util-image-devel >= 0.2.1
BuildRequires:	xcb-util-keysyms-devel >= 0.3.8
BuildRequires:	xcb-util-wm-devel >= 0.3.8
%else
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.6
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.3.3
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
%endif
%if %{with wayland}
BuildRequires:	wayland-devel >= 1.3.0
%if %{with wayland_egl}
BuildRequires:	EGL-devel
BuildRequires:	pkgconfig(egl) >= 7.10
BuildRequires:	wayland-egl-devel >= 9.2.0
%endif
%endif
# svg tests - exist in m4, but not called from configure
#BuildRequires:	esvg-devel >= 0.0.18
#BuildRequires:	ender-devel >= 0.0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# it used to be linux-gnu-ARCH before...
%define		arch_tag	v-1.10

%description
EFL - The Enlightenment Foundation Libraries.

%description -l pl.UTF-8
EFL (Enlightenment Foundation Libraries) - biblioteki tworzące
Enlightment.

%package -n ecore
Summary:	Enlightened Core event abstraction library
Summary(pl.UTF-8):	Biblioteka interfejsu abstrakcji zdarzeń Enlightened Core
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	eina = %{version}-%{release}
Requires:	eo = %{version}-%{release}
%{?with_systemd:Requires:	systemd-libs >= 1:192}
Obsoletes:	ecore-config < 1.8
Obsoletes:	ecore-config-devel < 1.8
Obsoletes:	ecore-config-static < 1.8
Obsoletes:	ecore-directfb < 1.8
Obsoletes:	ecore-directfb-devel < 1.8
Obsoletes:	ecore-directfb-static < 1.8
Obsoletes:	ecore-desktop < 1
Obsoletes:	ecore-job < 1
Obsoletes:	ecore-libs < 0.9.9.036-2
Obsoletes:	ecore-txt < 1

%description -n ecore
Ecore is the event/X abstraction layer that makes doing selections,
Xdnd, general X stuff, event loops, timeouts and idle handlers fast,
optimized, and convenient. It's a separate library so anyone can make
use of the work put into Ecore to make this job easy for applications.

%description -n ecore -l pl.UTF-8
Ecore to warstwa abstrakcji zdarzeń/X, która powoduje, że dokonywanie
zaznaczeń, Xdnd, ogólne operacje X, pętle zdarzeń, obsługa timeoutów i
bezczynności są szybkie, zoptymalizowane i wygodne. Jest to wydzielona
biblioteka, więc każdy może skorzystać z pracy włożonej w Ecore do
ułatwienia swojej pracy przy aplikacjach.

%package -n ecore-devel
Summary:	Header files for Ecore library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ecore
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eina-devel = %{version}-%{release}
Requires:	eo-devel = %{version}-%{release}
Requires:	glib2-devel >= 2.0
%{?with_systemd:Requires:	systemd-devel >= 1:192}

%description -n ecore-devel
Header files for Ecore library.

%description -n ecore-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ecore.

%package -n ecore-static
Summary:	Static Ecore library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-devel = %{version}-%{release}

%description -n ecore-static
Static Ecore library.

%description -n ecore-static -l pl.UTF-8
Statyczna biblioteka Ecore.

%package -n ecore-cxx-devel
Summary:	C++ API for Ecore library
Summary(pl.UTF-8):	API języka C++ do biblioteki Ecore
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-devel = %{version}-%{release}
Requires:	eina-cxx-devel = %{version}-%{release}
Requires:	eo-cxx-devel = %{version}-%{release}

%description -n ecore-cxx-devel
C++ API for Ecore library.

%description -n ecore-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Ecore.

%package -n ecore-system-systemd
Summary:	systemd system module for Ecore library
Summary(pl.UTF-8):	Moduł systemu systemd dla biblioteki Ecore
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}

%description -n ecore-system-systemd
systemd system module for Ecore library.

%description -n ecore-system-systemd -l pl.UTF-8
Moduł systemu systemd dla biblioteki Ecore.

%package -n ecore-system-upower
Summary:	UPower system module for Ecore library
Summary(pl.UTF-8):	Moduł systemu UPower dla biblioteki Ecore
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}

%description -n ecore-system-upower
UPower system module for Ecore library.

%description -n ecore-system-upower -l pl.UTF-8
Moduł systemu UPower dla biblioteki Ecore.

%package -n ecore-audio
Summary:	Ecore Audio library
Summary(pl.UTF-8):	Biblioteka dźwięku Ecore Audio
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eet = %{version}-%{release}

%description -n ecore-audio
Ecore Audio Library.

%description -n ecore-audio -l pl.UTF-8
Biblioteka dźwięku Ecore Audio.

%package -n ecore-audio-devel
Summary:	Header file for Ecore Audio library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Audio
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-audio = %{version}-%{release}
Requires:	ecore-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	libsndfile-devel
Requires:	pulseaudio-devel

%description -n ecore-audio-devel
Header file for Ecore Audio library.

%description -n ecore-audio-devel -l pl.UTF-8
Plik nagłówkowy biblioteki dźwięku Ecore Audio.

%package -n ecore-audio-static
Summary:	Static Ecore Audio library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore Audio
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-audio-devel = %{version}-%{release}

%description -n ecore-audio-static
Static Ecore Audio library.

%description -n ecore-audio-static -l pl.UTF-8
Statyczna biblioteka dźwięku Ecore Audio.

%package -n ecore-audio-cxx-devel
Summary:	C++ API for Ecore Audio library
Summary(pl.UTF-8):	API języka C++ do biblioteki Ecore Audio
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-audio-devel = %{version}-%{release}
Requires:	eo-cxx-devel = %{version}-%{release}

%description -n ecore-audio-cxx-devel
C++ API for Ecore Audio library.

%description -n ecore-audio-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Ecore Audio.

%package -n ecore-avahi
Summary:	Ecore Avahi integration library
Summary(pl.UTF-8):	Biblioteka integracji Ecore z Avahi
License:	unknown
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eina = %{version}-%{release}
Requires:	eo = %{version}-%{release}

%description -n ecore-avahi
Ecore Avahi integration library.

%description -n ecore-avahi -l pl.UTF-8
Biblioteka integracji Ecore z Avahi.

%package -n ecore-avahi-devel
Summary:	Header file for Ecore Avahi library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Avahi
License:	unknown
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	avahi-devel
Requires:	ecore-avahi = %{version}-%{release}
Requires:	ecore-devel = %{version}-%{release}
Requires:	eina-devel = %{version}-%{release}
Requires:	eo-devel = %{version}-%{release}

%description -n ecore-avahi-devel
Header file for Ecore Avahi library.

%description -n ecore-avahi-devel -l pl.UTF-8
Plik nagłówkowy biblioteki dźwięku Ecore Avahi.

%package -n ecore-avahi-static
Summary:	Static Ecore Avahi library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore Avahi
License:	unknown
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-avahi-devel = %{version}-%{release}

%description -n ecore-avahi-static
Static Ecore Avahi library.

%description -n ecore-avahi-static -l pl.UTF-8
Statyczna biblioteka dźwięku Ecore Avahi.

%package -n ecore-con
Summary:	Ecore Con(nection) library
Summary(pl.UTF-8):	Biblioteka połączeń Ecore Con
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
Requires:	eet = %{version}-%{release}
%{?with_gnutls:Requires:	gnutls >= 2.12.16}
%{?with_gnutls:Requires:	libgcrypt >= 1.2.0}

%description -n ecore-con
Ecore Con(nection) Library.

%description -n ecore-con -l pl.UTF-8
Biblioteka połączeń Ecore Con.

%package -n ecore-con-devel
Summary:	Header file for Ecore Con library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Con
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con = %{version}-%{release}
Requires:	ecore-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
%{?with_gnutls:Requires:	gnutls-devel >= 2.12.16}
%{?with_gnutls:Requires:	libgcrypt-devel >= 1.2.0}
%{!?with_gnutls:Requires:	openssl-devel}

%description -n ecore-con-devel
Header file for Ecore Con(nection) library.

%description -n ecore-con-devel -l pl.UTF-8
Plik nagłówkowy biblioteki połączeń Ecore Con.

%package -n ecore-con-static
Summary:	Static Ecore Con library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore Con
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con-devel = %{version}-%{release}

%description -n ecore-con-static
Static Ecore Con(nection) library.

%description -n ecore-con-static -l pl.UTF-8
Statyczna biblioteka połączeń Ecore Con.

%package -n ecore-drm
Summary:	Ecore DRM library
Summary(pl.UTF-8):	Biblioteka Ecore DRM
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}
Requires:	libdrm >= 2.4
Requires:	udev-libs >= 1:148
Requires:	xorg-lib-libxkbcommon >= 0.3.0

%description -n ecore-drm
Ecore DRM library.

%description -n ecore-drm -l pl.UTF-8
Biblioteka Ecore DRM.

%package -n ecore-drm-devel
Summary:	Header file for Ecore DRM library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore DRM
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-drm = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	libdrm-devel >= 2.4
Requires:	udev-devel >= 1:148
Requires:	xorg-lib-libxkbcommon-devel >= 0.3.0

%description -n ecore-drm-devel
Header file for Ecore DRM (frame buffer system functions) library.

%description -n ecore-drm-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore DRM (funkcji systemowych
framebuffera).

%package -n ecore-drm-static
Summary:	Static Ecore DRM library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore DRM
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-drm-devel = %{version}-%{release}

%description -n ecore-drm-static
Static Ecore DRM (frame buffer system functions) library.

%description -n ecore-drm-static -l pl.UTF-8
Statyczna biblioteka Ecore DRM (funkcji systemowych framebuffera).

%package -n ecore-evas
Summary:	Ecore Evas library
Summary(pl.UTF-8):	Biblioteka Ecore Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}
%{?with_drm:Requires:	ecore = %{version}-%{release}}
Requires:	ecore-input = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	evas = %{version}-%{release}

%description -n ecore-evas
Ecore Evas library.

%description -n ecore-evas -l pl.UTF-8
Biblioteka Ecore Evas.

%package -n ecore-evas-devel
Summary:	Header file for Ecore Evas library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Evas
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-devel = %{version}-%{release}
%{?with_drm:Requires:	ecore-drm = %{version}-%{release}}
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-input-evas-devel = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n ecore-evas-devel
Header file for Ecore Evas library.

%description -n ecore-evas-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore Evas.

%package -n ecore-evas-static
Summary:	Static Ecore Evas library
Summary(pl.UTF-8):	Biblioteka statyczna Ecore Evas
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas-devel = %{version}-%{release}

%description -n ecore-evas-static
Static Ecore Evas library.

%description -n ecore-evas-static -l pl.UTF-8
Biblioteka statyczna Ecore Evas.

%package -n ecore-evas-engine-drm
Summary:	DRM engine module for Ecore Evas library
Summary(pl.UTF-8):	Moduł silnika DRM dla biblioteki Ecore Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	evas-engine-drm = %{version}-%{release}

%description -n ecore-evas-engine-drm
DRM engine module for Ecore Evas library.

%description -n ecore-evas-engine-drm -l pl.UTF-8
Moduł silnika DRM dla biblioteki Ecore Evas.

%package -n ecore-evas-engine-extn
Summary:	extn engine module for Ecore Evas library
Summary(pl.UTF-8):	Moduł silnika extn dla biblioteki Ecore Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-ipc = %{version}-%{release}

%description -n ecore-evas-engine-extn
extn engine module for Ecore Evas library.

%description -n ecore-evas-engine-extn -l pl.UTF-8
Moduł silnika extn dla biblioteki Ecore Evas.

%package -n ecore-evas-engine-fb
Summary:	Framebuffer engine module for Ecore Evas library
Summary(pl.UTF-8):	Moduł silnika framebuffer dla biblioteki Ecore Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-fb = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	evas-engine-fb = %{version}-%{release}

%description -n ecore-evas-engine-fb
Framebuffer engine module for Ecore Evas library.

%description -n ecore-evas-engine-fb -l pl.UTF-8
Moduł silnika framebuffer dla biblioteki Ecore Evas.

%package -n ecore-evas-engine-sdl
Summary:	SDL engine module for Ecore Evas library
Summary(pl.UTF-8):	Moduł silnika SDL dla biblioteki Ecore Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	ecore-sdl = %{version}-%{release}
Requires:	evas-engine-gl_sdl = %{version}-%{release}

%description -n ecore-evas-engine-sdl
SDL engine module for Ecore Evas library.

%description -n ecore-evas-engine-sdl -l pl.UTF-8
Moduł silnika SDL dla biblioteki Ecore Evas.

%package -n ecore-evas-engine-wayland
Summary:	Wayland engine module for Ecore Evas library
Summary(pl.UTF-8):	Moduł silnika Wayland dla biblioteki Ecore Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	ecore-wayland = %{version}-%{release}
# ?
%if %{with wayland_egl}
Requires:	evas-engine-wayland_egl = %{version}-%{release}
%endif
Requires:	evas-engine-wayland_shm = %{version}-%{release}

%description -n ecore-evas-engine-wayland
Wayland engine module for Ecore Evas library.

%description -n ecore-evas-engine-wayland -l pl.UTF-8
Moduł silnika Wayland dla biblioteki Ecore Evas.

%package -n ecore-evas-engine-x
Summary:	X engine module for Ecore Evas library
Summary(pl.UTF-8):	Moduł silnika X dla biblioteki Ecore Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
# ?
Requires:	evas-engine-gl_x11 = %{version}-%{release}
Requires:	evas-engine-software_x11 = %{version}-%{release}

%description -n ecore-evas-engine-x
X engine module for Ecore Evas library.

%description -n ecore-evas-engine-x -l pl.UTF-8
Moduł silnika X dla biblioteki Ecore Evas.

%package -n ecore-fb
Summary:	Ecore FB (frame buffer system functions) library
Summary(pl.UTF-8):	Biblioteka Ecore FB (funkcji systemowych framebuffera)
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}

%description -n ecore-fb
Ecore FB (frame buffer system functions) library.

%description -n ecore-fb -l pl.UTF-8
Biblioteka Ecore FB (funkcji systemowych framebuffera).

%package -n ecore-fb-devel
Summary:	Header file for Ecore FB library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore FB
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-fb = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	tslib-devel

%description -n ecore-fb-devel
Header file for Ecore FB (frame buffer system functions) library.

%description -n ecore-fb-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore FB (funkcji systemowych
framebuffera).

%package -n ecore-fb-static
Summary:	Static Ecore FB library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore FB
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-fb-devel = %{version}-%{release}

%description -n ecore-fb-static
Static Ecore FB (frame buffer system functions) library.

%description -n ecore-fb-static -l pl.UTF-8
Statyczna biblioteka Ecore FB (funkcji systemowych framebuffera).

%package -n ecore-file
Summary:	Ecore File library
Summary(pl.UTF-8):	Biblioteka Ecore File
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con = %{version}-%{release}

%description -n ecore-file
Ecore File library.

%description -n ecore-file -l pl.UTF-8
Biblioteka Ecore File.

%package -n ecore-file-devel
Summary:	Header file for Ecore File library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore File
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con-devel = %{version}-%{release}
Requires:	ecore-file = %{version}-%{release}

%description -n ecore-file-devel
Header file for Ecore File library.

%description -n ecore-file-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore File.

%package -n ecore-file-static
Summary:	Static Ecore File library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore File
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-file-devel = %{version}-%{release}

%description -n ecore-file-static
Static Ecore File library.

%description -n ecore-file-static -l pl.UTF-8
Statyczna biblioteka Ecore File.

%package -n ecore-imf
Summary:	Ecore IMF library
Summary(pl.UTF-8):	Biblioteka Ecore IMF
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}

%description -n ecore-imf
Ecore IMF library.

%description -n ecore-imf -l pl.UTF-8
Biblioteka Ecore IMF.

%package -n ecore-imf-devel
Summary:	Header file for Ecore IMF library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore IMF
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-imf = %{version}-%{release}

%description -n ecore-imf-devel
Header file for Ecore IMF library.

%description -n ecore-imf-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore IMF.

%package -n ecore-imf-static
Summary:	Static Ecore IMF library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore IMF
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf-devel = %{version}-%{release}

%description -n ecore-imf-static
Static Ecore IMF library.

%description -n ecore-imf-static -l pl.UTF-8
Statyczna biblioteka Ecore IMF.

%package -n ecore-imf-module-ibus
Summary:	Ecore IMF IBus input method module
Summary(pl.UTF-8):	Ecore IMF - moduł metody wprowadzania znaków IBus
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-imf = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
Requires:	ibus >= 1.4
Obsoletes:	ecore-module-ibus < 1.8

%description -n ecore-imf-module-ibus
Ecore IMF IBus input method module.

%description -n ecore-imf-module-ibus -l pl.UTF-8
Ecore IMF - moduł metody wprowadzania znaków IBus.

%package -n ecore-imf-module-scim
Summary:	Ecore IMF SCIM input method module
Summary(pl.UTF-8):	Ecore IMF - moduł metody wprowadzania znaków SCIM
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-imf = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
Requires:	scim
Obsoletes:	ecore-module-scim < 1.8

%description -n ecore-imf-module-scim
Ecore IMF SCIM input method module.

%description -n ecore-imf-module-scim -l pl.UTF-8
Ecore IMF - moduł metody wprowadzania znaków SCIM.

%package -n ecore-imf-module-wayland
Summary:	Ecore IMF Wayland input method module
Summary(pl.UTF-8):	Ecore IMF - moduł metody wprowadzania znaków Wayland
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-imf = %{version}-%{release}
Requires:	ecore-wayland = %{version}-%{release}

%description -n ecore-imf-module-wayland
Ecore IMF Wayland input method module.

%description -n ecore-imf-module-wayland -l pl.UTF-8
Ecore IMF - moduł metody wprowadzania znaków Wayland.

%package -n ecore-imf-module-xim
Summary:	Ecore IMF XIM input method module
Summary(pl.UTF-8):	Ecore IMF - moduł metody wprowadzania znaków XIM
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
Obsoletes:	ecore-module-xim < 1.8

%description -n ecore-imf-module-xim
Ecore IMF XIM input method module.

%description -n ecore-imf-module-xim -l pl.UTF-8
Ecore IMF - moduł metody wprowadzania znaków XIM.

%package -n ecore-imf-evas
Summary:	Ecore IMF Evas library
Summary(pl.UTF-8):	Biblioteka Ecore IMF Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf = %{version}-%{release}
Requires:	evas = %{version}-%{release}

%description -n ecore-imf-evas
Ecore IMF Evas library.

%description -n ecore-imf-evas -l pl.UTF-8
Biblioteka Ecore IMF Evas.

%package -n ecore-imf-evas-devel
Summary:	Header file for Ecore IMF Evas library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore IMF Evas
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf-devel = %{version}-%{release}
Requires:	ecore-imf-evas = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n ecore-imf-evas-devel
Header file for Ecore IMF Evas library.

%description -n ecore-imf-evas-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore IMF Evas.

%package -n ecore-imf-evas-static
Summary:	Static Ecore IMF Evas library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore IMF Evas
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-imf-evas-devel = %{version}-%{release}

%description -n ecore-imf-evas-static
Static Ecore IMF Evas library.

%description -n ecore-imf-evas-static -l pl.UTF-8
Statyczna biblioteka Ecore IMF Evas.

%package -n ecore-input
Summary:	Ecore Input library
Summary(pl.UTF-8):	Biblioteka Ecore Input
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore = %{version}-%{release}

%description -n ecore-input
Ecore Input library.

%description -n ecore-input -l pl.UTF-8
Biblioteka Ecore Input.

%package -n ecore-input-devel
Summary:	Header file for Ecore Input library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Input
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-devel = %{version}-%{release}
Requires:	ecore-input = %{version}-%{release}

%description -n ecore-input-devel
Header file for Ecore Input library.

%description -n ecore-input-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore Input.

%package -n ecore-input-static
Summary:	Static Ecore Input library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore Input
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-devel = %{version}-%{release}

%description -n ecore-input-static
Static Ecore Input library.

%description -n ecore-input-static -l pl.UTF-8
Statyczna biblioteka Ecore Input.

%package -n ecore-input-evas
Summary:	Ecore Input Evas extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia Ecore Input Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}
Requires:	evas = %{version}-%{release}

%description -n ecore-input-evas
Ecore Input Evas extension library.

%description -n ecore-input-evas -l pl.UTF-8
Biblioteka rozszerzenia Ecore Input Evas.

%package -n ecore-input-evas-devel
Summary:	Header file for Ecore Input Evas extension library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki rozszerzenia Ecore Input Evas
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-input-evas = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n ecore-input-evas-devel
Header file for Ecore Input Evas extension library.

%description -n ecore-input-evas-devel -l pl.UTF-8
Plik nagłówkowy biblioteki rozszerzenia Ecore Input Evas.

%package -n ecore-input-evas-static
Summary:	Static Ecore Input Evas extension library
Summary(pl.UTF-8):	Statyczna biblioteka rozszerzenia Ecore Input Evas
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-evas-devel = %{version}-%{release}

%description -n ecore-input-evas-static
Static Ecore Input Evas extension library.

%description -n ecore-input-evas-static -l pl.UTF-8
Statyczna biblioteka rozszerzenia Ecore Input Evas.

%package -n ecore-ipc
Summary:	Ecore IPC (inter-process communication functions) library
Summary(pl.UTF-8):	Biblioteka Ecore IPC (funkcji komunikacji międzyprocesowej)
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con = %{version}-%{release}

%description -n ecore-ipc
Ecore IPC (inter-process communication functions) library.

%description -n ecore-ipc -l pl.UTF-8
Biblioteka Ecore IPC (funkcji komunikacji międzyprocesowej).

%package -n ecore-ipc-devel
Summary:	Header file for Ecore IPC library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore IPC
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-con-devel = %{version}-%{release}
Requires:	ecore-ipc = %{version}-%{release}

%description -n ecore-ipc-devel
Header file for Ecore IPC (inter-process communication functions)
library.

%description -n ecore-ipc-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore IPC (funkcji komunikacji
międzyprocesowej).

%package -n ecore-ipc-static
Summary:	Static Ecore IPC library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore IPC
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-ipc-devel = %{version}-%{release}

%description -n ecore-ipc-static
Static Ecore IPC (inter-process communication functions) library.

%description -n ecore-ipc-static -l pl.UTF-8
Statyczna biblioteka Ecore IPC (funkcji komunikacji międzyprocesowej).

%package -n ecore-sdl
Summary:	Ecore SDL library
Summary(pl.UTF-8):	Biblioteka Ecore SDL
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input = %{version}-%{release}
Requires:	SDL >= 1.2.0

%description -n ecore-sdl
Ecore SDL library.

%description -n ecore-sdl -l pl.UTF-8
Biblioteka Ecore SDL.

%package -n ecore-sdl-devel
Summary:	Header file for Ecore SDL library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore SDL
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-sdl = %{version}-%{release}
Requires:	SDL-devel >= 1.2.0

%description -n ecore-sdl-devel
Header file for Ecore SDL library.

%description -n ecore-sdl-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore SDL.

%package -n ecore-sdl-static
Summary:	Static Ecore SDL library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore SDL
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ecore
Requires:	ecore-sdl-devel = %{version}-%{release}

%description -n ecore-sdl-static
Static Ecore SDL library.

%description -n ecore-sdl-static -l pl.UTF-8
Statyczna biblioteka Ecore SDL.

%package -n ecore-wayland
Summary:	Ecore Wayland library
Summary(pl.UTF-8):	Biblioteka Ecore Wayland
Group:		Libraries
Requires:	ecore = %{version}-%{release}
Requires:	ecore-input = %{version}-%{release}
Requires:	wayland >= 1.3.0
Requires:	xorg-lib-libxkbcommon >= 0.3.0

%description -n ecore-wayland
Ecore Wayland library.

%description -n ecore-wayland -l pl.UTF-8
Biblioteka Ecore Wayland.

%package -n ecore-wayland-devel
Summary:	Header file for Ecore Wayland library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Ecore Wayland
Group:		Development/Libraries
Requires:	ecore-devel = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-wayland = %{version}-%{release}
Requires:	wayland-devel >= 1.3.0
Requires:	xorg-lib-libxkbcommon-devel >= 0.3.0

%description -n ecore-wayland-devel
Header file for Ecore Wayland library.

%description -n ecore-wayland-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Ecore Wayland.

%package -n ecore-wayland-static
Summary:	Static Ecore Wayland library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore Wayland
Group:		Development/Libraries
Requires:	ecore-wayland-devel = %{version}-%{release}

%description -n ecore-wayland-static
Static Ecore Wayland library.

%description -n ecore-wayland-static -l pl.UTF-8
Statyczna biblioteka Ecore Wayland.

%package -n ecore-x
Summary:	Ecore X (functions for dealing with the X Window System) library
Summary(pl.UTF-8):	Biblioteka Ecore X (funkcji do obsługi X Window System)
Group:		X11/Libraries
Requires:	ecore = %{version}-%{release}
Requires:	ecore-input = %{version}-%{release}
%if %{with xcb}
Requires:	xcb-util >= 0.3.8
Requires:	xcb-util-image >= 0.2.1
Requires:	xcb-util-keysyms >= 0.3.8
Requires:	xcb-util-wm >= 0.3.8
%else
Requires:	xorg-lib-libXi >= 1.6
Requires:	xorg-lib-libXrandr >= 1.3.3
%endif

%description -n ecore-x
Ecore X (functions for dealing with the X Window System) library.

%description -n ecore-x -l pl.UTF-8
Biblioteka Ecore X (funkcji do obsługi X Window System).

%package -n ecore-x-devel
Summary:	Header files for Ecore X library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Ecore X
Group:		Development/Libraries
Requires:	ecore-devel = %{version}-%{release}
Requires:	ecore-input-devel = %{version}-%{release}
Requires:	ecore-x = %{version}-%{release}
%if %{with xcb}
Requires:	libxcb-devel
Requires:	pixman-devel
Requires:	xcb-util-devel >= 0.3.8
Requires:	xcb-util-image-devel >= 0.2.1
Requires:	xcb-util-keysyms-devel >= 0.3.8
Requires:	xcb-util-wm-devel >= 0.3.8
%else
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXScrnSaver-devel
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXi-devel >= 1.6
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXrandr-devel >= 1.3.3
Requires:	xorg-lib-libXrender-devel
Requires:	xorg-lib-libXtst-devel
%endif

%description -n ecore-x-devel
Header files for Ecore X (functions for dealing with the X Window
System) library.

%description -n ecore-x-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Ecore X (funkcji do obsługi X Window
System).

%package -n ecore-x-static
Summary:	Static Ecore X library
Summary(pl.UTF-8):	Statyczna biblioteka Ecore X
Group:		Development/Libraries
Requires:	ecore-x-devel = %{version}-%{release}

%description -n ecore-x-static
Static Ecore X (functions for dealing with the X Window System)
library.

%description -n ecore-x-static -l pl.UTF-8
Statyczna biblioteka Ecore X (funkcji do obsługi X Window System).

%package -n edje
Summary:	Complex Graphical Design/Layout Engine
Summary(pl.UTF-8):	Złożony silnik graficznego projektowania/planowania
License:	BSD (library), GPL v2 (epp)
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	edje-libs = %{version}-%{release}
Requires:	evas-loader-png = %{version}-%{release}

%description -n edje
Edje is a complex graphical design and layout engine. It provides a
mechanism for allowing configuration data to define visual elements in
terms of layout, behavior, and appearance. Edje allows for multiple
collections of layouts in one file, allowing a complete set of images,
animations, and controls to exist as a unified whole.

Edje separates the arrangement, appearance, and behavior logic into
distinct independent entities. This allows visual objects to share
image data and configuration information without requiring them to do
so. This separation and simplistic event driven style of programming
can produce almost any look and feel one could want for basic visual
elements. Anything more complex is likely the domain of an application
or widget set that may use Edje as a convenient way of being able to
configure parts of the display.

%description -n edje -l pl.UTF-8
Edje to złożony silnik graficznego projektowania i planowania.
Dostarcza mechanizm pozwalający na definiowanie elementów graficznych
za pomocą danych konfiguracyjnych poprzez rozmieszczenie, zachowanie i
wygląd. Edje pozwala na wiele kolekcji projektów w jednym pliku,
zezwalając na istnienie pełnego zbioru obrazów, animacji i kontrolek
jako całości.

Edje oddziela rozmieszczenie, wygląd i logikę zachowania na różne,
niezależne elementy. Pozwala to na współdzielenie danych obrazów i
informacji o konfiguracji elementów graficznych bez wymagania tego.
Rozdzielenie to i uproszczony model programowania sterowanego
zdarzeniami może stworzyć prawie dowolny wygląd i zachowanie
podstawowych elementów graficznych. Wszystko bardziej złożone jest
raczej domeną aplikacji lub zbioru widgetów, które mogą używać Edje
jako wygodnego sposobu konfigurowania części ekranu.

%package -n edje-libs
Summary:	Edje library
Summary(pl.UTF-8):	Biblioteka edje
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	ecore-audio = %{version}-%{release}
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-file = %{version}-%{release}
Requires:	ecore-imf-evas = %{version}-%{release}
Requires:	eina = %{version}-%{release}
Requires:	eio = %{version}-%{release}
Requires:	eet = %{version}-%{release}
Requires:	embryo = %{version}-%{release}
Requires:	ephysics = %{version}-%{release}
%{!?with_luajit:Requires:	lua51 >= 5.1.0}
%{?with_luajit:Requires:	luajit >= 2.0.0}

%description -n edje-libs
Edje library.

%description -n edje-libs -l pl.UTF-8
Biblioteka edje.

%package -n edje-devel
Summary:	Edje header files
Summary(pl.UTF-8):	Pliki nagłówkowe Edje
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	ecore-audio-devel = %{version}-%{release}
Requires:	ecore-evas-devel = %{version}-%{release}
Requires:	ecore-file-devel = %{version}-%{release}
Requires:	ecore-imf-evas-devel = %{version}-%{release}
Requires:	edje-libs = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	eio-devel = %{version}-%{release}
Requires:	embryo-devel = %{version}-%{release}
Requires:	ephysics-devel = %{version}-%{release}
%{!?with_luajit:Requires:	lua51-devel >= 5.1.0}
%{?with_luajit:Requires:	luajit-devel >= 2.0.0}

%description -n edje-devel
Header files for Edje.

%description -n edje-devel -l pl.UTF-8
Pliki nagłówkowe Edje.

%package -n edje-static
Summary:	Static Edje library
Summary(pl.UTF-8):	Statyczna biblioteka Edje
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	edje-devel = %{version}-%{release}

%description -n edje-static
Static Edje library.

%description -n edje-static -l pl.UTF-8
Statyczna biblioteka Edje.

%package -n edje-cxx-devel
Summary:	C++ API for Edje library
Summary(pl.UTF-8):	API języka C++ do biblioteki Edje
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Edje
Requires:	edje-devel = %{version}-%{release}
Requires:	eo-cxx-devel = %{version}-%{release}

%description -n edje-cxx-devel
C++ API for Edje library.

%description -n edje-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Edje.

%package -n edje-module-emotion
Summary:	Emotion module for Edje library
Summary(pl.UTF-8):	Moduł Emotion dla biblioteki Edje
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	edje-libs = %{version}-%{release}
Requires:	emotion = %{version}-%{release}

%description -n edje-module-emotion
Emotion module for Edje library.

%description -n edje-module-emotion -l pl.UTF-8
Moduł Emotion dla biblioteki Edje.

%package -n eet
Summary:	Library for speedy data storage, retrieval, and compression
Summary(pl.UTF-8):	Biblioteka do szybkiego zapisywania, odtwarzania i kompresji danych
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eet
Requires:	eina = %{version}-%{release}
%{?with_gnutls:Requires:	gnutls >= 2.12.16}
%{?with_gnutls:Requires:	libgcrypt >= 1.2.0}
Requires:	zlib >= 1.2.3

%description -n eet
Eet is a tiny library designed to write an arbitary set of chunks of
data to a file and optionally compress each chunk (very much like a
zip file) and allow fast random-access reading of the file later on.
It does not do zip as a zip itself has more complexity than is needed,
and it was much simpler to implement this once here.

It also can encode and decode data structures in memory, as well as
image data for saving to eet files or sending across the network to
other machines, or just writing to arbitary files on the system. All
data is encoded in a platform independant way and can be written and
read by any architecture.

%description -n eet -l pl.UTF-8
Eet to mała biblioteka zaprojektowana do zapisu dowolnego zbioru
porcji danych do pliku i opcjonalnej kompresji każdej porcji (podobnie
do pliku zip) oraz umożliwienia później szybkiego odczytu pliku ze
swobodnym dostępem. Nie jest to zip, jako że sam zip jest bardziej
złożony niż trzeba, a było dużo prościej zaimplementować to tak, jak
jest.

Biblioteka może także kodować i dekodować struktury danych w pamięci,
a także dane obrazów do zapisu do plików eet lub wysyłania po sieci na
inne maszyny, lub po prostu zapisywania do dowolnych plików w
systemie. Wszystkie dane są kodowane w sposób niezależny od platformy
i mogą być zapisywane i odczytywane na dowolnej architekturze.

%package -n eet-devel
Summary:	Header files for Eet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Eet
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eet
Requires:	eet = %{version}-%{release}
Requires:	eina-devel = %{version}-%{release}
%{?with_gnutls:Requires:	gnutls-devel >= 2.12.16}
%{?with_gnutls:Requires:	libgcrypt-devel >= 1.2.0}
%{!?with_gnutls:Requires:	openssl-devel}
Requires:	libjpeg-devel
Requires:	zlib-devel >= 1.2.3

%description -n eet-devel
Header files for Eet library.

%description -n eet-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Eet.

%package -n eet-static
Summary:	Static Eet library
Summary(pl.UTF-8):	Statyczna biblioteka Eet
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eet
Requires:	eet-devel = %{version}-%{release}

%description -n eet-static
Static Eet library.

%description -n eet-static -l pl.UTF-8
Statyczna biblioteka Eet.

%package -n eet-cxx-devel
Summary:	C++ API for Eet library
Summary(pl.UTF-8):	API języka C++ do biblioteki Eet
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eet
Requires:	eet-devel = %{version}-%{release}
Requires:	eina-cxx-devel = %{version}-%{release}
Requires:	eo-cxx-devel = %{version}-%{release}

%description -n eet-cxx-devel
C++ API for Eet library.

%description -n eet-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Eet.

%package -n eeze
Summary:	Library for manipulating devices through udev
Summary(pl.UTF-8):	Biblioteka do operowania urządzeniami korzystająca z udev
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eeze
Requires:	ecore-file = %{version}-%{release}
Requires:	eet = %{version}-%{release}
Requires:	libmount >= 2.18.0
Requires:	udev-libs >= 1:148
Obsoletes:	enlightenment-utils-eeze < 1.7

%description -n eeze
Eeze is a library for manipulating devices through udev with a simple
and fast API. It interfaces directly with libudev, avoiding such
middleman daemons as udisks/upower or hal, to immediately gather
device information the instant it becomes known to the system. This
can be used to determine such things as:
 - If a CD-ROM has a disk inserted
 - The temperature of a cpu core
 - The remaining power left in a battery
 - The current power consumption of various parts
 - Monitor in realtime the status of peripheral devices.
  
Each of the above examples can be performed by using only a single
eeze function, as one of the primary focuses of the library is to
reduce the complexity of managing devices.

%description -n eeze -l pl.UTF-8
Eeze to bibliotek do operowania urządzeniami poprzez udev z prostym i
szybkim API. Działa bezpośrednio z libudev, bez pośrednich demonów,
takich jak udisks, upower czy hal, aby zebrać informacje z urządzeń
natychmiast, kiedy staną się znane w systemie. Może to służyć do
określania rzeczy takich jak:
 - włożenie płyty CD
 - termperatura rdzenia procesora
 - pozostała pojemność baterii
 - aktualne zużycie energii przez różne elementy
 - monitorowanie stanu urządzeń peryferyjnych w czasie rzeczywistym.

Każde z tych zapytań może być wykonane przy użyciu jedynie pojedynczej
funkcji eeze, jako że jedną z głównych idei biblioteki jest
ograniczenie skomplikowania zarządzania urządzeniami.

%package -n eeze-devel
Summary:	Eeze header files
Summary(pl.UTF-8):	Pliki nagłówkowe Eeze
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eeze
Requires:	eeze = %{version}-%{release}
Requires:	ecore-file-devel = %{version}-%{release}
Requires:	libmount-devel >= 2.18.0
Requires:	udev-devel >= 1:148

%description -n eeze-devel
Header files for Eeze.

%description -n eeze-devel -l pl.UTF-8
Pliki nagłówkowe Eeze.

%package -n eeze-static
Summary:	Static Eeze library
Summary(pl.UTF-8):	Statyczna biblioteka Eeze
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eeze
Requires:	eeze-devel = %{version}-%{release}

%description -n eeze-static
Static Eeze library.

%description -n eeze-static -l pl.UTF-8
Statyczna biblioteka Eeze.

%package -n efreet
Summary:	freedesktop.org standards implementation for the EFL
Summary(pl.UTF-8):	Implementacja standardów freedesktop.org dla EFL
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Efreet
Requires:	dbus
Requires:	efreet-libs = %{version}-%{release}

%description -n efreet
Efreet is an implementation of the following specifications from
freedesktop.org:
 - Base Directory - Locations for system and user specific desktop
   configuration files,
 - Desktop Entries - The metadata associated with the applications
   installed on a system,
 - Application Menus - The arrangement of available applications into
   a hierarchical menu,
 - Icon Themes - A means of associating icons with various objects on
   the desktop in a themable fashion.

By following these specifications, Enlightenment 0.17 uses the same
format for describing application launchers, menus and icon themes as
the GNOME, KDE and XFCE Desktop Environments. A system must only
provide a single set of this data for use with any of these desktops.

%description -n efreet -l pl.UTF-8
Efreet to implementacja następujących specyfikacji z freedesktop.org:
 - Base Directory - położenie plików konfiguracyjnych środowiska dla
   systemu i użytkownika,
 - Desktop Entries - metadane związane z aplikacjami zainstalowanymi w
   systemie,
 - Application Menus - uporządkowanie dostępnych aplikacji w menu
   hierarchiczne,
 - Icon Themes - sposób wiązania ikon z różnymi obiektami w środowisku
   w sposób pozwalający na ustawianie motywów.

%package -n efreet-libs
Summary:	Efreet shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Efreet
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Efreet
Requires:	ecore-file = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}
Requires:	eet = %{version}-%{release}

%description -n efreet-libs
Efreet shared libraries.

%description -n efreet-libs -l pl.UTF-8
Biblioteki współdzielone Efreet.

%package -n efreet-devel
Summary:	Efreet header files
Summary(pl.UTF-8):	Pliki nagłówkowe Efreet
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Efreet
Requires:	ecore-file-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	efreet-libs = %{version}-%{release}
Requires:	eldbus-devel = %{version}-%{release}

%description -n efreet-devel
Header files for Efreet.

%description -n efreet-devel -l pl.UTF-8
Pliki nagłówkowe Efreet.

%package -n efreet-static
Summary:	Static Efreet library
Summary(pl.UTF-8):	Statyczna biblioteka Efreet
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Efreet
Requires:	efreet-devel = %{version}-%{release}

%description -n efreet-static
Static Efreet library.

%description -n efreet-static -l pl.UTF-8
Statyczna biblioteka Efreet.

%package -n eina
Summary:	Data types library (list, hash, etc.)
Summary(pl.UTF-8):	Biblioteka struktur danych (lista, hasz, itp.)
License:	LGPL v2.1+
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eina
%{?with_systemd:Requires:	systemd-libs >= 1:192}

%description -n eina
Data types library (list, hash, etc.)

%description -n eina -l pl.UTF-8
Bilblioteka struktur danych (lista, hasz, itp.).

%package -n eina-devel
Summary:	Eina header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Eina
License:	LGPL v2.1+
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eina
Requires:	eina = %{version}-%{release}
%{?with_systemd:Requires:	systemd-devel >= 1:192}

%description -n eina-devel
Header files for Eina.

%description -n eina-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Eina.

%package -n eina-static
Summary:	Static Eina library
Summary(pl.UTF-8):	Statyczna biblioteka Eina
License:	LGPL v2.1+
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eina
Requires:	eina-devel = %{version}-%{release}

%description -n eina-static
Static Eina library.

%description -n eina-static -l pl.UTF-8
Statyczna biblioteka Eina.

%package -n eina-cxx-devel
Summary:	C++ API for Eina library
Summary(pl.UTF-8):	API języka C++ do biblioteki Eina
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eina
Requires:	eina-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description -n eina-cxx-devel
C++ API for Eina library.

%description -n eina-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Eina.

%package -n eio
Summary:	Enlightenment Input Output Library
Summary(pl.UTF-8):	Enlightenment Input Output - biblioteka wejścia/wyjścia z projektu Enlightenment
License:	LGPL v2.1+
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Eio
Requires:	ecore = %{version}-%{release}
Requires:	eet = %{version}-%{release}

%description -n eio
This library is intended to provide non blocking I/O by using thread
for all operation that may block. It depends only on eina and ecore
right now. It should integrate all the features/functions of
Ecore_File that could block.

%description -n eio -l pl.UTF-8
Ta biblioteka na za zadanie zapewniać nieblokujące operacje we/wy
poprzez użycie wątków dla wszystkich operacji, które mogę być
blokujące. Na razie wymaga tylko bibliotek eina i ecore. Powinna
zawierać wszystkie funkcje Ecore_File, które mogą być blokujące.

%package -n eio-devel
Summary:	Header files for Eio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Eio
Group:		Development/Libraries
Requires:	ecore-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	eio = %{version}-%{release}
Conflicts:	libeio-devel

%description -n eio-devel
Header files for Eio library.

%description -n eio-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Eio.

%package -n eio-static
Summary:	Static Eio library
Summary(pl.UTF-8):	Statyczna biblioteka Eio
Group:		Development/Libraries
Requires:	eio-devel = %{version}-%{release}

%description -n eio-static
Static Eio library.

%description -n eio-static -l pl.UTF-8
Statyczna biblioteka Eio.

%package -n eldbus
Summary:	Easy access to D-Bus from EFL applications
Summary(pl.UTF-8):	Łatwy dostęp do usługi D-Bus z aplikacji EFL
License:	LGPL v2.1+
Group:		Libraries
Requires:	ecore = %{version}-%{release}
Requires:	eina = %{version}-%{release}

%description -n eldbus
Eldbus provides easy access to D-Bus from EFL applications.

Eldbus allows connecting to both system and session buses acting as
both client and service roles.

%description -n eldbus -l pl.UTF-8
Eldbus zapewnia łatwy dostęp do usługi D-Bus z aplikacji EFL.

Eldbus pozwala na łączenie się z szyną systemową lub sesyjną, zarówno
w roli klienta, jak i usługi.

%package -n eldbus-devel
Summary:	Header files for eldbus library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki eldbus
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	dbus-devel
Requires:	ecore-devel = %{version}-%{release}
Requires:	eina-devel = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}

%description -n eldbus-devel
Header files for eldbus library.

%description -n eldbus-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki eldbus.

%package -n eldbus-static
Summary:	Static eldbus library
Summary(pl.UTF-8):	Statyczna biblioteka eldbus
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	eldbus-devel = %{version}-%{release}

%description -n eldbus-static
Static eldbus library.

%description -n eldbus-static -l pl.UTF-8
Statyczna biblioteka eldbus.

%package -n embryo
Summary:	Enlightenment Fundation Libraries - Embryo
Summary(pl.UTF-8):	Podstawowe biblioteki Enlightenmenta - Embryo
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Embryo
Requires:	eina = %{version}-%{release}

%description -n embryo
Embryo is a tiny library designed as a virtual machine to interpret a
limited set of small compiled programs.

%description -n embryo -l pl.UTF-8
Embryo to mała biblioteka zaprojektowana jako maszyna wirtualna do
interpretowania ograniczonego zbioru małych skompilowanych programów.

%package -n embryo-devel
Summary:	Embryo header files
Summary(pl.UTF-8):	Pliki nagłówkowe Embryo
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Embryo
Requires:	eina-devel = %{version}-%{release}
Requires:	embryo = %{version}-%{release}

%description -n embryo-devel
Header files for Embryo.

%description -n embryo-devel -l pl.UTF-8
Pliki nagłówkowe Embryo.

%package -n embryo-static
Summary:	Static Embryo library
Summary(pl.UTF-8):	Statyczna biblioteka Embryo
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Embryo
Requires:	embryo-devel = %{version}-%{release}

%description -n embryo-static
Static Embryo library.

%description -n embryo-static -l pl.UTF-8
Statyczna biblioteka Embryo.

%package -n emotion
Summary:	Emotion - EFL media playback library
Summary(pl.UTF-8):	Emotion - biblioteka EFL do odtwarzania multimediów
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	ecore = %{version}-%{release}
Requires:	eet = %{version}-%{release}
Requires:	eeze = %{version}-%{release}
Requires:	eio = %{version}-%{release}
Requires:	evas = %{version}-%{release}
# for edje module
Requires:	edje-libs = %{version}-%{release}
Obsoletes:	emotion-decoder-vlc < 1.8

%description -n emotion
Emotion is a library to easily integrate media playback into EFL
applications, it will take care of using Ecore's main loop and video
display is done using Evas.

%description -n emotion -l pl.UTF-8
Emotion to biblioteka pozwalająca na łatwą integrację odtwarzania
multimediów w aplikacjach EFL. Współpracuje z główną pętlą Ecore, a do
wyświetlania wykorzystuje bibliotekę Evas.

%package -n emotion-devel
Summary:	Emotion header files
Summary(pl.UTF-8):	Pliki nagłówkowe Emotion
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	ecore-devel = %{version}-%{release}
Requires:	eio-devel = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	eeze-devel = %{version}-%{release}
Requires:	emotion = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n emotion-devel
Header files for Emotion.

%description -n emotion-devel -l pl.UTF-8
Pliki nagłówkowe Emotion.

%package -n emotion-static
Summary:	Static Emotion library
Summary(pl.UTF-8):	Statyczna biblioteka Emotion
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	emotion-devel = %{version}-%{release}

%description -n emotion-static
Static Emotion library.

%description -n emotion-static -l pl.UTF-8
Statyczna biblioteka Emotion.

%package -n emotion-decoder-gstreamer
Summary:	Emotion decoder using gstreamer
Summary(pl.UTF-8):	Dekoder Emotion używający gstreamera
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	emotion = %{version}-%{release}
Requires:	gstreamer >= 1.0
Requires:	gstreamer-plugins-base >= 1.0

%description -n emotion-decoder-gstreamer
Emotion decoder using gstreamer.

%description -n emotion-decoder-gstreamer -l pl.UTF-8
Dekoder Emotion używający gstreamera.

%package -n emotion-decoder-xine
Summary:	Emotion decoder using xine
Summary(pl.UTF-8):	Dekoder Emotion używający xine
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Emotion
Requires:	emotion = %{version}-%{release}
Requires:	xine-lib >= 2:1.1.1

%description -n emotion-decoder-xine
Emotion decoder using xine.

%description -n emotion-decoder-xine -l pl.UTF-8
Dekoder Emotion używający xine.

%package -n eo
Summary:	Object type library
Summary(pl.UTF-8):	Biblioteka typów obiektów
License:	BSD
Group:		Libraries
Requires:	eina = %{version}-%{release}

%description -n eo
Eo is an object type library.

%description -n eo -l pl.UTF-8
Eo to biblioteka typów obiektów.

%package -n eo-devel
Summary:	Header file for Eo library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki Eo
License:	BSD
Group:		Development/Libraries
Requires:	eina-devel = %{version}-%{release}
Requires:	eo = %{version}-%{release}

%description -n eo-devel
Header file for Eo library.

%description -n eo-devel -l pl.UTF-8
Plik nagłówkowy biblioteki Eo.

%package -n eo-static
Summary:	Static Eo library
Summary(pl.UTF-8):	Statyczna biblioteka Eo
License:	BSD
Group:		Development/Libraries
Requires:	eo-devel = %{version}-%{release}

%description -n eo-static
Static Eo library.

%description -n eo-static -l pl.UTF-8
Statyczna biblioteka Eo.

%package -n eo-cxx-devel
Summary:	C++ API for Eo library
Summary(pl.UTF-8):	API języka C++ do biblioteki Eo
Group:		Development/Libraries
Requires:	eina-cxx-devel = %{version}-%{release}
Requires:	eo-devel = %{version}-%{release}

%description -n eo-cxx-devel
C++ API for Eo library.

%description -n eo-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Eo.

%package -n eo-gdb
Summary:	GDB Python support scripts for Eo types
Summary(pl.UTF-8):	Skrypty Pythona do obsługi typów Eo w GDB
Group:		Development/Debuggers
Requires:	eo = %{version}-%{release}
Requires:	gdb

%description -n eo-gdb
GDB Python support scripts for Eo types.

%description -n eo-gdb -l pl.UTF-8
Skrypty Pythona do obsługi typów Eo w GDB.

%package -n eolian
Summary:	EFL .eo parser and code generator library
Summary(pl.UTF-8):	Biblioteka EFL do analizy .eo i generowania kodu
License:	BSD
Group:		Libraries
Requires:	eina = %{version}-%{release}

%description -n eolian
Eolian is an EFL's .eo parser and code generator.

%description -n eolian -l pl.UTF-8
Eolian to analizator .eo i generator kodu EFL.

%package -n eolian-devel
Summary:	Header files for Eolian library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Eolian
License:	BSD
Group:		Development/Libraries
Requires:	eina-devel = %{version}-%{release}
Requires:	eolian = %{version}-%{release}

%description -n eolian-devel
Header files for Eolian library.

%description -n eolian-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Eolian.

%package -n eolian-static
Summary:	Static Eolian library
Summary(pl.UTF-8):	Statyczna biblioteka Eolian
License:	BSD
Group:		Development/Libraries
Requires:	eolian-devel = %{version}-%{release}

%description -n eolian-static
Static Eolian library.

%description -n eolian-static -l pl.UTF-8
Statyczna biblioteka Eolian.

%package -n eolian-cxx-devel
Summary:	C++ API for Eolian library
Summary(pl.UTF-8):	API języka C++ do biblioteki Eolian
Group:		Development/Libraries
Requires:	eo-devel = %{version}-%{release}
Requires:	eolian-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description -n eolian-cxx-devel
C++ API for Eolian library.

%description -n eolian-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Eolian.

%package -n ephysics
Summary:	EPhysics - wrapper for physics engine
Summary(pl.UTF-8):	EPhysics - interfejs do silnika fizyki
Group:		Libraries
Requires:	bullet >= 2.80
Requires:	ecore = %{version}-%{release}
Requires:	evas = %{version}-%{release}

%description -n ephysics
EPhysics is a wrapper for physics engine.

%description -n ephysics -l pl.UTF-8
EPhysics to interfejs do silnika fizyki.

%package -n ephysics-devel
Summary:	Header file for EPhysics library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki EPhysics
Group:		Development/Libraries
Requires:	bullet-devel >= 2.80
Requires:	ecore-devel = %{version}-%{release}
Requires:	ephysics = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n ephysics-devel
Header file for EPhysics library.

%description -n ephysics-devel -l pl.UTF-8
Plik nagłówkowy biblioteki EPhysics.

%package -n ephysics-static
Summary:	Static EPhysics library
Summary(pl.UTF-8):	Statyczna biblioteka EPhysics
Group:		Development/Libraries
Requires:	ephysics-devel = %{version}-%{release}

%description -n ephysics-static
Static EPhysics library.

%description -n ephysics-static -l pl.UTF-8
Statyczna biblioteka EPhysics.

%package -n ethumb
Summary:	Ethumb - thumbnail generation service and utilities
Summary(pl.UTF-8):	Ethumb - usługa i narzędzia generujące miniaturki
License:	LGPL v2.1
Group:		Applications/Graphics
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	dbus
Requires:	ethumb-libs = %{version}-%{release}
Obsoletes:	ethumb-plugin-epdf < 1.8

%description -n ethumb
Ethumb is a thumbnail generation library. Features:
- create thumbnails with a predefined frame (possibly an edje frame);
- have an option to create fdo-like thumbnails;
- have a client/server utility.

%description -n ethumb -l pl.UTF-8
Ethumb to biblioteka do generowania miniaturek. Możliwości:
- tworzenie miniaturek z predefiniowaną ramką (w tym ramką edje);
- opcja tworzenia miniaturek w stylu fdo;
- narzędzia klient-serwer.

%package -n ethumb-libs
Summary:	Ethumb shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Ethumb
License:	LGPL v2.1
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	ecore-evas = %{version}-%{release}
Requires:	ecore-file = %{version}-%{release}
Requires:	edje-libs = %{version}-%{release}
Requires:	eldbus = %{version}-%{release}

%description -n ethumb-libs
Ethumb shared libraries.

%description -n ethumb-libs -l pl.UTF-8
Biblioteki współdzielone Ethumb.

%package -n ethumb-devel
Summary:	Header files for Ethumb libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Ethumb
License:	LGPL v2.1
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	ethumb-libs = %{version}-%{release}
Requires:	ecore-evas-devel = %{version}-%{release}
Requires:	ecore-file-devel = %{version}-%{release}
Requires:	edje-devel = %{version}-%{release}
Requires:	eldbus-devel = %{version}-%{release}

%description -n ethumb-devel
Header files for Ethumb libraries.

%description -n ethumb-devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Ethumb.

%package -n ethumb-static
Summary:	Static Ethumb libraries
Summary(pl.UTF-8):	Statyczne biblioteki Ethumb
License:	LGPL v2.1
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	ethumb-devel = %{version}-%{release}

%description -n ethumb-static
Static Ethumb libraries.

%description -n ethumb-static -l pl.UTF-8
Statyczne biblioteki Ethumb.

%package -n ethumb-plugin-emotion
Summary:	Emotion plugin for Ethumb library
Summary(pl.UTF-8):	Wtyczka Emotion dla biblioteki Ethumb
License:	LGPL v2.1
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Ethumb
Requires:	edje-libs = %{version}-%{release}
Requires:	emotion = %{version}-%{release}
Requires:	ethumb-libs = %{version}-%{release}

%description -n ethumb-plugin-emotion
Emotion plugin for Ethumb library. It creates thumbnails from movies
using Emotion library.

%description -n ethumb-plugin-emotion -l pl.UTF-8
Wtyczka Emotion dla biblioteki Ethumb. Potrafi tworzyć miniaturki z
filmów przy użyciu biblioteki Emotion.

%package -n evas
Summary:	Multi-platform Canvas Library
Summary(pl.UTF-8):	Wieloplatformowa biblioteka do rysowania
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	eet = %{version}-%{release}
Requires:	eo = %{version}-%{release}
Requires:	fontconfig-libs >= 2.5.0
Requires:	freetype >= 1:2.2
Requires:	fribidi >= 0.19.2
Requires:	harfbuzz >= 0.9.0
# Provides for statically linked modules
Provides:	evas-engine-buffer = %{version}-%{release}
Provides:	evas-engine-software_generic = %{version}-%{release}
Provides:	evas-loader-eet = %{version}-%{release}
Provides:	evas-loader-pmaps = %{version}-%{release}
Provides:	evas-loader-xpm = %{version}-%{release}
Provides:	evas-saver-eet = %{version}-%{release}
# packages merged in
Obsoletes:	evas-engine-buffer < %{version}-%{release}
Obsoletes:	evas-engine-software_generic < %{version}-%{release}
Obsoletes:	evas-libs < 0.9.9.036
Obsoletes:	evas-loader-eet < %{version}-%{release}
Obsoletes:	evas-loader-pmaps < %{version}-%{release}
Obsoletes:	evas-loader-xpm < %{version}-%{release}
Obsoletes:	evas-saver-eet < %{version}-%{release}
# obsolete packages
Obsoletes:	evas-engine-directfb < 1.8
Obsoletes:	evas-engine-software_8 < 1.8
Obsoletes:	evas-engine-software_8_x11 < 1.8
Obsoletes:	evas-engine-software_16 < 1.8
Obsoletes:	evas-engine-software_16_sdl < 1.8
Obsoletes:	evas-engine-software_16_x11 < 1.8
Obsoletes:	evas-engine-software_qtopia < 1.1
Obsoletes:	evas-engine-xrender_x11 < 1.1
Obsoletes:	evas-engine-xrender_xcb < 1.0.0-1
Obsoletes:	evas-loader-edb < 1.8
Obsoletes:	evas-loader-svg < 1.8
Obsoletes:	evas-saver-edb < 1.8

%description -n evas
Evas is a clean display canvas API for several target display systems
that can draw anti-aliased text, smooth super and sub-sampled scaled
images, alpha-blend objects much and more.

%description -n evas -l pl.UTF-8
Evas to czyste API "płótna obrazu" dla różnych systemów wyświetlania,
będące w stanie rysować tekst z antyaliasingiem, wygładzane, skalowane
obrazy, obiekty z alpha-blendingiem i inne elementy.

%package -n evas-devel
Summary:	Evas header files
Summary(pl.UTF-8):	Pliki nagłówkowe Evas
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	eet-devel = %{version}-%{release}
Requires:	eo-devel = %{version}-%{release}
Requires:	fontconfig-devel >= 2.5.0
Requires:	freetype-devel >= 1:2.2
Requires:	fribidi-devel >= 0.19.2
Requires:	harfbuzz-devel >= 0.9.0
%if %{with wayland_egl}
Requires:	EGL-devel
Requires:	pkgconfig(egl) >= 7.10
Requires:	wayland-egl-devel >= 9.2.0
%endif

%description -n evas-devel
Header files for Evas.

%description -n evas-devel -l pl.UTF-8
Pliki nagłówkowe Evas.

%package -n evas-static
Summary:	Static Evas library
Summary(pl.UTF-8):	Statyczna biblioteka Evas
License:	BSD
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas-devel = %{version}-%{release}

%description -n evas-static
Static Evas library.

%description -n evas-static -l pl.UTF-8
Statyczna biblioteka Evas.

%package -n evas-cxx-devel
Summary:	C++ API for Evas library
Summary(pl.UTF-8):	API języka C++ do biblioteki Evas
Group:		Development/Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	eo-cxx-devel = %{version}-%{release}
Requires:	evas-devel = %{version}-%{release}

%description -n evas-cxx-devel
C++ API for Evas library.

%description -n evas-cxx-devel -l pl.UTF-8
API języka C++ do biblioteki Evas.

## EVAS MODULES
# engines:
%package -n evas-engine-drm
Summary:	DRM rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego DRM dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-engine-drm
DRM rendering engine module for Evas.

%description -n evas-engine-drm -l pl.UTF-8
Moduł silnika renderującego DRM dla Evas.

%package -n evas-engine-fb
Summary:	Framebuffer rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego na framebuffer dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-engine-fb
Framebuffer rendering engine module for Evas.

%description -n evas-engine-fb -l pl.UTF-8
Moduł silnika renderującego na framebuffer dla Evas.

%package -n evas-engine-gl_sdl
Summary:	SDL OpenGL rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego na SDL OpenGL dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	SDL >= 1.2.0

%description -n evas-engine-gl_sdl
SDL OpenGL rendering engine module for Evas.

%description -n evas-engine-gl_sdl -l pl.UTF-8
Moduł silnika renderującego na SDL OpenGL dla Evas.

%package -n evas-engine-gl_x11
Summary:	OpenGL under X11 rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego na OpenGL pod X11 dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-engine-gl_x11
OpenGL under X11 rendering engine module for Evas.

%description -n evas-engine-gl_x11 -l pl.UTF-8
Moduł silnika renderującego na OpenGL pod X11 dla Evas.

%package -n evas-engine-software_x11
Summary:	Software X11 rendering engine module for Evas
Summary(pl.UTF-8):	Moduł programowego silnika renderującego X11 dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Obsoletes:	evas-engine-software_xcb < 1.0.0-1

%description -n evas-engine-software_x11
Software X11 rendering engine module for Evas.

%description -n evas-engine-software_x11 -l pl.UTF-8
Moduł programowego silnika renderującego X11 dla Evas.

%package -n evas-engine-wayland_egl
Summary:	Wayland EGL rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego Wayland EGL dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	wayland-egl >= 9.2.0

%description -n evas-engine-wayland_egl
Wayland EGL rendering engine module for Evas.

%description -n evas-engine-wayland_egl -l pl.UTF-8
Moduł silnika renderującego Wayland EGL dla Evas.

%package -n evas-engine-wayland_shm
Summary:	Wayland SHM rendering engine module for Evas
Summary(pl.UTF-8):	Moduł silnika renderującego Wayland SHM dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-engine-wayland_shm
Wayland SHM rendering engine module for Evas.

%description -n evas-engine-wayland_shm -l pl.UTF-8
Moduł silnika renderującego Wayland SHM dla Evas.

# loaders:
%package -n evas-loader-gif
Summary:	GIF Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów GIF dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-gif
GIF Image loader module for Evas.

%description -n evas-loader-gif -l pl.UTF-8
Moduł wczytywania obrazów GIF dla Evas.

%package -n evas-loader-jp2k
Summary:	JPEG2000 Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów JPEG2000 dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-jp2k
JPEG2000 Image loader module for Evas.

%description -n evas-loader-jp2k -l pl.UTF-8
Moduł wczytywania obrazów JPEG2000 dla Evas.

%package -n evas-loader-jpeg
Summary:	JPEG Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów JPEG dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-jpeg
JPEG Image loader module for Evas.

%description -n evas-loader-jpeg -l pl.UTF-8
Moduł wczytywania obrazów JPEG dla Evas.

%package -n evas-loader-png
Summary:	PNG Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów PNG dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	libpng >= 1.2.10

%description -n evas-loader-png
PNG Image loader module for Evas.

%description -n evas-loader-png -l pl.UTF-8
Moduł wczytywania obrazów PNG dla Evas.

%package -n evas-loader-tiff
Summary:	TIFF Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów TIFF dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-tiff
TIFF Image loader module for Evas.

%description -n evas-loader-tiff -l pl.UTF-8
Moduł wczytywania obrazów TIFF dla Evas.

%package -n evas-loader-webp
Summary:	WebP Image loader module for Evas
Summary(pl.UTF-8):	Moduł wczytywania obrazów WebP dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-loader-webp
WebP Image loader module for Evas.

%description -n evas-loader-webp -l pl.UTF-8
Moduł wczytywania obrazów WebP dla Evas.

# savers:
%package -n evas-saver-jpeg
Summary:	JPEG Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów JPEG dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-saver-jpeg
JPEG Image saver module for Evas.

%description -n evas-saver-jpeg -l pl.UTF-8
Moduł zapisywania obrazów JPEG dla Evas.

%package -n evas-saver-png
Summary:	PNG Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów PNG dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}
Requires:	libpng >= 1.2.10

%description -n evas-saver-png
PNG Image saver module for Evas.

%description -n evas-saver-png -l pl.UTF-8
Moduł zapisywania obrazów PNG dla Evas.

%package -n evas-saver-tiff
Summary:	TIFF Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów TIFF dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-saver-tiff
TIFF Image saver module for Evas.

%description -n evas-saver-tiff -l pl.UTF-8
Moduł zapisywania obrazów TIFF dla Evas.

%package -n evas-saver-webp
Summary:	WebP Image saver module for Evas
Summary(pl.UTF-8):	Moduł zapisywania obrazów WebP dla Evas
License:	BSD
Group:		Libraries
URL:		http://trac.enlightenment.org/e/wiki/Evas
Requires:	evas = %{version}-%{release}

%description -n evas-saver-webp
WebP Image saver module for Evas.

%description -n evas-saver-webp -l pl.UTF-8
Moduł zapisywania obrazów WebP dla Evas.

%package -n vim-addon-efl
Summary:	EDC syntax support for Vim
Summary(pl.UTF-8):	Obsługa składni EDC dla Vima
Group:		Applications/Editors/Vim
Requires:	vim-rt
Obsoletes:	vim-syntax-edc < 1.8

%description -n vim-addon-efl
EDC syntax support for Vim.

%description -n vim-addon-efl -l pl.UTF-8
Obsługa składni EDC dla Vima.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_drm:--enable-drm} \
	%{?with_egl:--enable-egl} \
	%{?with_fb:--enable-fb} \
	%{?with_gesture:--enable-gesture} \
	%{!?with_gstreamer:--disable-gstreamer1} \
	%{?with_harfbuzz:--enable-harfbuzz} \
	%{!?with_ibus:--disable-ibus} \
	--enable-image-loader-gif \
	--enable-image-loader-jpeg \
	--enable-image-loader-jp2k \
	--enable-image-loader-png \
	--enable-image-loader-tiff \
	--enable-image-loader-webp \
	%{!?with_luajit:--enable-lua-old} \
	--enable-multisense \
	%{?with_pixman:--enable-pixman} \
	%{!?with_scim:--disable-scim} \
	%{?with_sdl:--enable-sdl} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	%{?with_systemd:--enable-systemd} \
	%{?with_wayland:--enable-wayland} \
	%{?with_xine:--enable-xine} \
	--enable-xinput22 \
	--with-crypto=%{?with_gnutls:gnutls}%{!?with_gnutls:openssl} \
	--with-x11=%{?with_xcb:xcb}%{!?with_xcb:xlib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles
cp -pr data/edje/vim/autoload $RPM_BUILD_ROOT%{_datadir}/vim
cp -pr data/edje/vim/{ftdetect,ftplugin,indent,snippets,syntax} $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la
# loadable modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ecore/system/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ecore_evas/engines/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ecore_imf/modules/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/edje/modules/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/eeze/modules/sensor/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/emotion/modules/*/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ethumb/modules/emotion/*/module.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/evas/modules/*/*/*/module.la
# benchmarking script, requires expedite and python - should be in expedite?
%{__rm} $RPM_BUILD_ROOT%{_bindir}/eina-bench-cmp

# contains ecore+efreet messages; efreet R: ecore, so package it with ecore
%find_lang efl

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n ecore -p /sbin/ldconfig
%postun	-n ecore -p /sbin/ldconfig

%post	-n ecore-audio -p /sbin/ldconfig
%postun	-n ecore-audio -p /sbin/ldconfig

%post	-n ecore-avahi -p /sbin/ldconfig
%postun	-n ecore-avahi -p /sbin/ldconfig

%post	-n ecore-con -p /sbin/ldconfig
%postun	-n ecore-con -p /sbin/ldconfig

%post	-n ecore-drm -p /sbin/ldconfig
%postun	-n ecore-drm -p /sbin/ldconfig

%post	-n ecore-evas -p /sbin/ldconfig
%postun	-n ecore-evas -p /sbin/ldconfig

%post	-n ecore-fb -p /sbin/ldconfig
%postun	-n ecore-fb -p /sbin/ldconfig

%post	-n ecore-file -p /sbin/ldconfig
%postun	-n ecore-file -p /sbin/ldconfig

%post	-n ecore-imf -p /sbin/ldconfig
%postun	-n ecore-imf -p /sbin/ldconfig

%post	-n ecore-imf-evas -p /sbin/ldconfig
%postun	-n ecore-imf-evas -p /sbin/ldconfig

%post	-n ecore-input -p /sbin/ldconfig
%postun	-n ecore-input -p /sbin/ldconfig

%post	-n ecore-input-evas -p /sbin/ldconfig
%postun	-n ecore-input-evas -p /sbin/ldconfig

%post	-n ecore-ipc -p /sbin/ldconfig
%postun	-n ecore-ipc -p /sbin/ldconfig

%post	-n ecore-sdl -p /sbin/ldconfig
%postun	-n ecore-sdl -p /sbin/ldconfig

%post	-n ecore-wayland -p /sbin/ldconfig
%postun	-n ecore-wayland -p /sbin/ldconfig

%post	-n ecore-x -p /sbin/ldconfig
%postun	-n ecore-x -p /sbin/ldconfig

%post	-n edje-libs -p /sbin/ldconfig
%postun	-n edje-libs -p /sbin/ldconfig

%post	-n eet -p /sbin/ldconfig
%postun	-n eet -p /sbin/ldconfig

%post	-n eeze -p /sbin/ldconfig
%postun	-n eeze -p /sbin/ldconfig

%post	-n efreet-libs -p /sbin/ldconfig
%postun	-n efreet-libs -p /sbin/ldconfig

%post	-n eina -p /sbin/ldconfig
%postun	-n eina -p /sbin/ldconfig

%post	-n eio -p /sbin/ldconfig
%postun	-n eio -p /sbin/ldconfig

%post	-n eldbus -p /sbin/ldconfig
%postun	-n eldbus -p /sbin/ldconfig

%post	-n embryo -p /sbin/ldconfig
%postun	-n embryo -p /sbin/ldconfig

%post	-n emotion -p /sbin/ldconfig
%postun	-n emotion -p /sbin/ldconfig

%post	-n eo -p /sbin/ldconfig
%postun	-n eo -p /sbin/ldconfig

%post	-n eolian -p /sbin/ldconfig
%postun	-n eolian -p /sbin/ldconfig

%post	-n ephysics -p /sbin/ldconfig
%postun	-n ephysics -p /sbin/ldconfig

%post	-n ethumb-libs -p /sbin/ldconfig
%postun	-n ethumb-libs -p /sbin/ldconfig

%post	-n evas -p /sbin/ldconfig
%postun	-n evas -p /sbin/ldconfig

%files -n ecore -f efl.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore.so.1
%dir %{_libdir}/ecore
%dir %{_libdir}/ecore/system
%{_datadir}/ecore

%files -n ecore-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore.so
%{_includedir}/ecore-1
%{_pkgconfigdir}/ecore.pc
%{_libdir}/cmake/Ecore

%if %{with static_libs}
%files -n ecore-static
%defattr(644,root,root,755)
%{_libdir}/libecore.a
%endif

%files -n ecore-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/ecore-cxx-1
%{_pkgconfigdir}/ecore-cxx.pc
%{_libdir}/cmake/EcoreCxx

%if %{with systemd}
%files -n ecore-system-systemd
%defattr(644,root,root,755)
%dir %{_libdir}/ecore/system/systemd
%dir %{_libdir}/ecore/system/systemd/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore/system/systemd/%{arch_tag}/module.so
%endif

%files -n ecore-system-upower
%defattr(644,root,root,755)
%dir %{_libdir}/ecore/system/upower
%dir %{_libdir}/ecore/system/upower/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore/system/upower/%{arch_tag}/module.so

%files -n ecore-audio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_audio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_audio.so.1

%files -n ecore-audio-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_audio.so
%{_includedir}/ecore-audio-1
%{_pkgconfigdir}/ecore-audio.pc

%if %{with static_libs}
%files -n ecore-audio-static
%defattr(644,root,root,755)
%{_libdir}/libecore_audio.a
%endif

%files -n ecore-audio-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/ecore-audio-cxx-1
%{_pkgconfigdir}/ecore-audio-cxx.pc

%files -n ecore-avahi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_avahi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_avahi.so.1

%files -n ecore-avahi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_avahi.so
%{_includedir}/ecore-avahi-1
%{_pkgconfigdir}/ecore-avahi.pc

%if %{with static_libs}
%files -n ecore-avahi-static
%defattr(644,root,root,755)
%{_libdir}/libecore_avahi.a
%endif

%files -n ecore-con
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_con.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_con.so.1

%files -n ecore-con-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_con.so
%{_includedir}/ecore-con-1
%{_pkgconfigdir}/ecore-con.pc

%if %{with static_libs}
%files -n ecore-con-static
%defattr(644,root,root,755)
%{_libdir}/libecore_con.a
%endif

%files -n ecore-drm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_drm.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_drm.so.1
%dir %{_libdir}/ecore_drm
%dir %{_libdir}/ecore_drm/bin
%dir %{_libdir}/ecore_drm/bin/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_drm/bin/%{arch_tag}/ecore_drm_launch

%files -n ecore-drm-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_drm.so
%{_includedir}/ecore-drm-1
%{_pkgconfigdir}/ecore-drm.pc

%if %{with static_libs}
%files -n ecore-drm-static
%defattr(644,root,root,755)
%{_libdir}/libecore_drm.a
%endif

%files -n ecore-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ecore_evas_convert
%attr(755,root,root) %{_libdir}/libecore_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_evas.so.1
%dir %{_libdir}/ecore_evas
%dir %{_libdir}/ecore_evas/engines

%files -n ecore-evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_evas.so
%{_includedir}/ecore-evas-1
%{_pkgconfigdir}/ecore-evas.pc

%if %{with static_libs}
%files -n ecore-evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_evas.a
%endif

%files -n ecore-evas-engine-drm
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/drm
%dir %{_libdir}/ecore_evas/engines/drm/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/drm/%{arch_tag}/module.so

%files -n ecore-evas-engine-extn
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/extn
%dir %{_libdir}/ecore_evas/engines/extn/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/extn/%{arch_tag}/module.so

%if %{with fb}
%files -n ecore-evas-engine-fb
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/fb
%dir %{_libdir}/ecore_evas/engines/fb/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/fb/%{arch_tag}/module.so
%endif

%if %{with sdl}
%files -n ecore-evas-engine-sdl
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/sdl
%dir %{_libdir}/ecore_evas/engines/sdl/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/sdl/%{arch_tag}/module.so
%endif

%if %{with wayland}
%files -n ecore-evas-engine-wayland
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/wayland
%dir %{_libdir}/ecore_evas/engines/wayland/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/wayland/%{arch_tag}/module.so
%endif

%files -n ecore-evas-engine-x
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_evas/engines/x
%dir %{_libdir}/ecore_evas/engines/x/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/x/%{arch_tag}/module.so

%if %{with fb}
%files -n ecore-fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_fb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_fb.so.1

%files -n ecore-fb-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_fb.so
%{_includedir}/ecore-fb-1
%{_pkgconfigdir}/ecore-fb.pc

%if %{with static_libs}
%files -n ecore-fb-static
%defattr(644,root,root,755)
%{_libdir}/libecore_fb.a
%endif
%endif

%files -n ecore-file
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_file.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_file.so.1

%files -n ecore-file-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_file.so
%{_includedir}/ecore-file-1
%{_pkgconfigdir}/ecore-file.pc

%if %{with static_libs}
%files -n ecore-file-static
%defattr(644,root,root,755)
%{_libdir}/libecore_file.a
%endif

%files -n ecore-imf
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_imf.so.1
%dir %{_libdir}/ecore_imf
%dir %{_libdir}/ecore_imf/modules
%{_datadir}/ecore_imf

%files -n ecore-imf-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf.so
%{_includedir}/ecore-imf-1
%{_pkgconfigdir}/ecore-imf.pc

%if %{with static_libs}
%files -n ecore-imf-static
%defattr(644,root,root,755)
%{_libdir}/libecore_imf.a
%endif

%if %{with ibus}
%files -n ecore-imf-module-ibus
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_imf/modules/ibus
%dir %{_libdir}/ecore_imf/modules/ibus/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/ibus/%{arch_tag}/module.so
%endif

%if %{with scim}
%files -n ecore-imf-module-scim
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_imf/modules/scim
%dir %{_libdir}/ecore_imf/modules/scim/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/scim/%{arch_tag}/module.so
%endif

%if %{with wayland}
%files -n ecore-imf-module-wayland
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_imf/modules/wayland
%dir %{_libdir}/ecore_imf/modules/wayland/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/wayland/%{arch_tag}/module.so
%endif

%if %{without xcb_api}
%files -n ecore-imf-module-xim
%defattr(644,root,root,755)
%dir %{_libdir}/ecore_imf/modules/xim
%dir %{_libdir}/ecore_imf/modules/xim/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/xim/%{arch_tag}/module.so
%endif

%files -n ecore-imf-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_imf_evas.so.1

%files -n ecore-imf-evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so
%{_includedir}/ecore-imf-evas-1
%{_pkgconfigdir}/ecore-imf-evas.pc

%if %{with static_libs}
%files -n ecore-imf-evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_imf_evas.a
%endif

%files -n ecore-input
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_input.so.1

%files -n ecore-input-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input.so
%{_includedir}/ecore-input-1
%{_pkgconfigdir}/ecore-input.pc

%if %{with static_libs}
%files -n ecore-input-static
%defattr(644,root,root,755)
%{_libdir}/libecore_input.a
%endif

%files -n ecore-input-evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_input_evas.so.1

%files -n ecore-input-evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_input_evas.so
%{_includedir}/ecore-input-evas-1
%{_pkgconfigdir}/ecore-input-evas.pc

%if %{with static_libs}
%files -n ecore-input-evas-static
%defattr(644,root,root,755)
%{_libdir}/libecore_input_evas.a
%endif

%files -n ecore-ipc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_ipc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_ipc.so.1

%files -n ecore-ipc-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_ipc.so
%{_includedir}/ecore-ipc-1
%{_pkgconfigdir}/ecore-ipc.pc

%if %{with static_libs}
%files -n ecore-ipc-static
%defattr(644,root,root,755)
%{_libdir}/libecore_ipc.a
%endif

%if %{with sdl}
%files -n ecore-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_sdl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_sdl.so.1

%files -n ecore-sdl-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_sdl.so
%{_includedir}/ecore-sdl-1
%{_pkgconfigdir}/ecore-sdl.pc

%if %{with static_libs}
%files -n ecore-sdl-static
%defattr(644,root,root,755)
%{_libdir}/libecore_sdl.a
%endif
%endif

%if %{with wayland}
%files -n ecore-wayland
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_wayland.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_wayland.so.1

%files -n ecore-wayland-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_wayland.so
%{_includedir}/ecore-wayland-1
%{_pkgconfigdir}/ecore-wayland.pc

%if %{with static_libs}
%files -n ecore-wayland-static
%defattr(644,root,root,755)
%{_libdir}/libecore_wayland.a
%endif
%endif

%files -n ecore-x
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_x.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_x.so.1

%files -n ecore-x-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libecore_x.so
%{_includedir}/ecore-x-1
%{_pkgconfigdir}/ecore-x.pc

%if %{with static_libs}
%files -n ecore-x-static
%defattr(644,root,root,755)
%{_libdir}/libecore_x.a
%endif

%files -n edje
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/edje_cc
%attr(755,root,root) %{_bindir}/edje_codegen
%attr(755,root,root) %{_bindir}/edje_decc
%attr(755,root,root) %{_bindir}/edje_external_inspector
%attr(755,root,root) %{_bindir}/edje_inspector
%attr(755,root,root) %{_bindir}/edje_pick
%attr(755,root,root) %{_bindir}/edje_player
%attr(755,root,root) %{_bindir}/edje_recc
%attr(755,root,root) %{_bindir}/edje_watch
%dir %{_libdir}/edje/utils
%dir %{_libdir}/edje/utils/%{arch_tag}
%attr(755,root,root) %dir %{_libdir}/edje/utils/%{arch_tag}/epp
%{_datadir}/edje
%{_datadir}/mime/packages/edje.xml

%files -n edje-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libedje.so.1
%dir %{_libdir}/edje
%dir %{_libdir}/edje/modules

%files -n edje-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libedje.so
%{_includedir}/edje-1
%{_pkgconfigdir}/edje.pc
%{_libdir}/cmake/Edje

%if %{with static_libs}
%files -n edje-static
%defattr(644,root,root,755)
%{_libdir}/libedje.a
%endif

%files -n edje-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/edje-cxx-1
%{_pkgconfigdir}/edje-cxx.pc

%files -n edje-module-emotion
%defattr(644,root,root,755)
%dir %{_libdir}/edje/modules/emotion
%dir %{_libdir}/edje/modules/emotion/%{arch_tag}
%attr(755,root,root) %{_libdir}/edje/modules/emotion/%{arch_tag}/module.so

%files -n eet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eet
%attr(755,root,root) %{_bindir}/vieet
%attr(755,root,root) %{_libdir}/libeet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeet.so.1

%files -n eet-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeet.so
%{_includedir}/eet-1
%{_pkgconfigdir}/eet.pc
%{_libdir}/cmake/Eet

%if %{with static_libs}
%files -n eet-static
%defattr(644,root,root,755)
%{_libdir}/libeet.a
%endif

%files -n eet-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/eet-cxx-1
%{_pkgconfigdir}/eet-cxx.pc
%{_libdir}/cmake/EetCxx

%files -n eeze
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eeze_disk_ls
%attr(755,root,root) %{_bindir}/eeze_mount
%attr(755,root,root) %{_bindir}/eeze_scanner
%attr(755,root,root) %{_bindir}/eeze_umount
%attr(755,root,root) %{_libdir}/libeeze.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeeze.so.1
%dir %{_libdir}/eeze
%dir %{_libdir}/eeze/modules
%dir %{_libdir}/eeze/modules/sensor
%dir %{_libdir}/eeze/modules/sensor/fake
%dir %{_libdir}/eeze/modules/sensor/fake/%{arch_tag}
%attr(755,root,root) %{_libdir}/eeze/modules/sensor/fake/%{arch_tag}/module.so
%dir %{_libdir}/eeze/modules/sensor/udev
%dir %{_libdir}/eeze/modules/sensor/udev/%{arch_tag}
%attr(755,root,root) %{_libdir}/eeze/modules/sensor/udev/%{arch_tag}/module.so
%{_datadir}/eeze

%files -n eeze-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeeze.so
%{_includedir}/eeze-1
%{_pkgconfigdir}/eeze.pc
%{_libdir}/cmake/Eeze

%if %{with static_libs}
%files -n eeze-static
%defattr(644,root,root,755)
%{_libdir}/libeeze.a
%endif

%files -n efreet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/efreetd
%dir %{_libdir}/efreet
%dir %{_libdir}/efreet/%{arch_tag}
%attr(755,root,root) %{_libdir}/efreet/%{arch_tag}/efreet_desktop_cache_create
%attr(755,root,root) %{_libdir}/efreet/%{arch_tag}/efreet_icon_cache_create
%if %{with systemd}
%{systemduserunitdir}/efreet.service
%endif
%{_datadir}/dbus-1/services/org.enlightenment.Efreet.service
%{_datadir}/efreet

%files -n efreet-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libefreet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libefreet.so.1
%attr(755,root,root) %{_libdir}/libefreet_mime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libefreet_mime.so.1
%attr(755,root,root) %{_libdir}/libefreet_trash.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libefreet_trash.so.1

%files -n efreet-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libefreet.so
%attr(755,root,root) %{_libdir}/libefreet_mime.so
%attr(755,root,root) %{_libdir}/libefreet_trash.so
%{_includedir}/efreet-1
%{_pkgconfigdir}/efreet.pc
%{_pkgconfigdir}/efreet-mime.pc
%{_pkgconfigdir}/efreet-trash.pc
%{_libdir}/cmake/Efreet

%if %{with static_libs}
%files -n efreet-static
%defattr(644,root,root,755)
%{_libdir}/libefreet.a
%{_libdir}/libefreet_mime.a
%{_libdir}/libefreet_trash.a
%endif

%files -n eina
%defattr(644,root,root,755)
%doc AUTHORS COMPLIANCE COPYING ChangeLog NEWS README licenses/COPYING.{BSD,SMALL}
%attr(755,root,root) %{_libdir}/libeina.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeina.so.1

%files -n eina-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeina.so
# efl-1 is common for EFL - packaged here as eina is all-common EFL dependency
%{_includedir}/efl-1
%{_includedir}/eina-1
%{_pkgconfigdir}/eina.pc
%{_libdir}/cmake/Eina

%if %{with static_libs}
%files -n eina-static
%defattr(644,root,root,755)
%{_libdir}/libeina.a
%endif

%files -n eina-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/eina-cxx-1
%{_pkgconfigdir}/eina-cxx.pc
%{_libdir}/cmake/EinaCxx

%files -n eio
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeio.so.1

%files -n eio-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeio.so
%{_includedir}/eio-1
%{_pkgconfigdir}/eio.pc

%if %{with static_libs}
%files -n eio-static
%defattr(644,root,root,755)
%{_libdir}/libeio.a
%endif

%files -n eldbus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeldbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeldbus.so.1

%files -n eldbus-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eldbus-codegen
%attr(755,root,root) %{_libdir}/libeldbus.so
%{_includedir}/eldbus-1
%{_pkgconfigdir}/eldbus.pc
%{_libdir}/cmake/Eldbus

%if %{with static_libs}
%files -n eldbus-static
%defattr(644,root,root,755)
%{_libdir}/libeldbus.a
%endif

%files -n embryo
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/embryo_cc
%attr(755,root,root) %{_libdir}/libembryo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libembryo.so.1
# for embryo_cc
%{_datadir}/embryo

%files -n embryo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libembryo.so
%{_includedir}/embryo-1
%{_pkgconfigdir}/embryo.pc

%if %{with static_libs}
%files -n embryo-static
%defattr(644,root,root,755)
%{_libdir}/libembryo.a
%endif

%files -n emotion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libemotion.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libemotion.so.1
%dir %{_libdir}/emotion
%dir %{_libdir}/emotion/modules
%{_datadir}/emotion

%files -n emotion-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libemotion.so
%{_includedir}/emotion-1
%{_pkgconfigdir}/emotion.pc
%{_libdir}/cmake/Emotion

%if %{with static_libs}
%files -n emotion-static
%defattr(644,root,root,755)
%{_libdir}/libemotion.a
%endif

%if %{with gstreamer}
%files -n emotion-decoder-gstreamer
%defattr(644,root,root,755)
%dir %{_libdir}/emotion/modules/gstreamer1
%dir %{_libdir}/emotion/modules/gstreamer1/%{arch_tag}
%attr(755,root,root) %{_libdir}/emotion/modules/gstreamer1/%{arch_tag}/module.so
%endif

%if %{with xine}
%files -n emotion-decoder-xine
%defattr(644,root,root,755)
%dir %{_libdir}/emotion/modules/xine
%dir %{_libdir}/emotion/modules/xine/%{arch_tag}
%attr(755,root,root) %{_libdir}/emotion/modules/xine/%{arch_tag}/module.so
%endif

%files -n eo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeo.so.1

%files -n eo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeo.so
%{_includedir}/eo-1
%{_pkgconfigdir}/eo.pc
%{_libdir}/cmake/Eo

%if %{with static_libs}
%files -n eo-static
%defattr(644,root,root,755)
%{_libdir}/libeo.a
%endif

%files -n eo-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/eo-cxx-1
%{_pkgconfigdir}/eo-cxx.pc
%{_libdir}/cmake/EoCxx

%files -n eo-gdb
%defattr(644,root,root,755)
%dir %{_datadir}/eo
%{_datadir}/eo/gdb
%{_datadir}/gdb/auto-load/usr/%{_lib}/libeo.so.%{version}-gdb.py

%files -n eolian
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eolian_cxx
%attr(755,root,root) %{_bindir}/eolian_gen
%attr(755,root,root) %{_libdir}/libeolian.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeolian.so.1
%dir %{_datadir}/eolian
%dir %{_datadir}/eolian/include
# package everything here or per-library split?
%{_datadir}/eolian/include/ecore-1
%{_datadir}/eolian/include/edje-1
%{_datadir}/eolian/include/eo-1
%{_datadir}/eolian/include/evas-1

%files -n eolian-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libeolian.so
%{_includedir}/eolian-1
%{_pkgconfigdir}/eolian.pc
%{_libdir}/cmake/Eolian

%files -n eolian-static
%defattr(644,root,root,755)
%{_libdir}/libeolian.a

%files -n eolian-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/eolian-cxx-1
%{_pkgconfigdir}/eolian-cxx.pc
%{_libdir}/cmake/EolianCxx

%files -n ephysics
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libephysics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libephysics.so.1

%files -n ephysics-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libephysics.so
%{_includedir}/ephysics-1
%{_pkgconfigdir}/ephysics.pc

%if %{with static_libs}
%files -n ephysics-static
%defattr(644,root,root,755)
%{_libdir}/libephysics.a
%endif

%files -n ethumb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ethumb
%attr(755,root,root) %{_bindir}/ethumbd
%attr(755,root,root) %{_bindir}/ethumbd_client
%dir %{_libdir}/ethumb_client
%dir %{_libdir}/ethumb_client/utils
%dir %{_libdir}/ethumb_client/utils/%{arch_tag}
%attr(755,root,root) %{_libdir}/ethumb_client/utils/%{arch_tag}/ethumbd_slave
%if %{with systemd}
%{systemduserunitdir}/ethumb.service
%endif
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ethumb
%{_datadir}/ethumb_client

%files -n ethumb-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libethumb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libethumb.so.1
%attr(755,root,root) %{_libdir}/libethumb_client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libethumb_client.so.1
%dir %{_libdir}/ethumb
%dir %{_libdir}/ethumb/modules

%files -n ethumb-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libethumb.so
%attr(755,root,root) %{_libdir}/libethumb_client.so
%{_includedir}/ethumb-1
%{_includedir}/ethumb-client-1
%{_pkgconfigdir}/ethumb.pc
%{_pkgconfigdir}/ethumb_client.pc
%{_libdir}/cmake/Ethumb
%{_libdir}/cmake/EthumbClient

%if %{with static_libs}
%files -n ethumb-static
%defattr(644,root,root,755)
%{_libdir}/libethumb.a
%{_libdir}/libethumb_client.a
%endif

%files -n ethumb-plugin-emotion
%defattr(644,root,root,755)
%dir %{_libdir}/ethumb/modules/emotion
%dir %{_libdir}/ethumb/modules/emotion/%{arch_tag}
%attr(755,root,root) %{_libdir}/ethumb/modules/emotion/%{arch_tag}/module.so
%{_libdir}/ethumb/modules/emotion/%{arch_tag}/template.edj

%files -n evas
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/evas_cserve2_client
%attr(755,root,root) %{_bindir}/evas_cserve2_debug
%attr(755,root,root) %{_bindir}/evas_cserve2_shm_debug
%attr(755,root,root) %{_bindir}/evas_cserve2_usage
%attr(755,root,root) %{_libdir}/libevas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevas.so.1
%dir %{_libdir}/evas
%dir %{_libdir}/evas/cserve2
%dir %{_libdir}/evas/cserve2/bin
%dir %{_libdir}/evas/cserve2/bin/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/cserve2/bin/%{arch_tag}/evas_cserve2
%attr(755,root,root) %{_libdir}/evas/cserve2/bin/%{arch_tag}/evas_cserve2_slave
%dir %{_libdir}/evas/modules
%dir %{_libdir}/evas/modules/engines
%dir %{_libdir}/evas/modules/loaders
%dir %{_libdir}/evas/modules/savers
%{_datadir}/evas

%files -n evas-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libevas.so
%{_includedir}/evas-1
%{_pkgconfigdir}/evas.pc
# engine private structures
%{?with_drm:%{_pkgconfigdir}/evas-drm.pc}
%{?with_fb:%{_pkgconfigdir}/evas-fb.pc}
%{?with_sdl:%{_pkgconfigdir}/evas-opengl-sdl.pc}
%{_pkgconfigdir}/evas-opengl-x11.pc
%{_pkgconfigdir}/evas-software-buffer.pc
%{_pkgconfigdir}/evas-software-x11.pc
%if %{with wayland}
%{?with_wayland_egl:%{_pkgconfigdir}/evas-wayland-egl.pc}
%{_pkgconfigdir}/evas-wayland-shm.pc
%endif
%{_libdir}/cmake/Evas

%if %{with static_libs}
%files -n evas-static
%defattr(644,root,root,755)
%{_libdir}/libevas.a
%endif

%files -n evas-cxx-devel
%defattr(644,root,root,755)
%{_includedir}/evas-cxx-1
%{_pkgconfigdir}/evas-cxx.pc
%{_libdir}/cmake/EvasCxx

%if %{with drm}
%files -n evas-engine-drm
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/drm
%dir %{_libdir}/evas/modules/engines/drm/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/drm/%{arch_tag}/module.so
%endif

%if %{with fb}
%files -n evas-engine-fb
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/fb
%dir %{_libdir}/evas/modules/engines/fb/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/fb/%{arch_tag}/module.so
%endif

%if %{with sdl}
%files -n evas-engine-gl_sdl
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/gl_sdl
%dir %{_libdir}/evas/modules/engines/gl_sdl/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/gl_sdl/%{arch_tag}/module.so
%endif

%files -n evas-engine-gl_x11
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/gl_x11
%dir %{_libdir}/evas/modules/engines/gl_x11/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/gl_x11/%{arch_tag}/module.so

%files -n evas-engine-software_x11
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/software_x11
%dir %{_libdir}/evas/modules/engines/software_x11/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/software_x11/%{arch_tag}/module.so

%if %{with wayland}
%if %{with wayland_egl}
%files -n evas-engine-wayland_egl
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/wayland_egl
%dir %{_libdir}/evas/modules/engines/wayland_egl/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/wayland_egl/%{arch_tag}/module.so
%endif

%files -n evas-engine-wayland_shm
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/engines/wayland_shm
%dir %{_libdir}/evas/modules/engines/wayland_shm/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/wayland_shm/%{arch_tag}/module.so
%endif

%files -n evas-loader-gif
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/gif
%dir %{_libdir}/evas/modules/loaders/gif/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/gif/%{arch_tag}/module.so

%files -n evas-loader-jp2k
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/jp2k
%dir %{_libdir}/evas/modules/loaders/jp2k/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/jp2k/%{arch_tag}/module.so

%files -n evas-loader-jpeg
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/jpeg
%dir %{_libdir}/evas/modules/loaders/jpeg/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/jpeg/%{arch_tag}/module.so

%files -n evas-loader-png
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/png
%dir %{_libdir}/evas/modules/loaders/png/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/png/%{arch_tag}/module.so

%files -n evas-loader-tiff
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/tiff
%dir %{_libdir}/evas/modules/loaders/tiff/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/tiff/%{arch_tag}/module.so

%files -n evas-loader-webp
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/loaders/webp
%dir %{_libdir}/evas/modules/loaders/webp/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/loaders/webp/%{arch_tag}/module.so

%files -n evas-saver-jpeg
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/savers/jpeg
%dir %{_libdir}/evas/modules/savers/jpeg/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/savers/jpeg/%{arch_tag}/module.so

%files -n evas-saver-png
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/savers/png
%dir %{_libdir}/evas/modules/savers/png/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/savers/png/%{arch_tag}/module.so

%files -n evas-saver-tiff
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/savers/tiff
%dir %{_libdir}/evas/modules/savers/tiff/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/savers/tiff/%{arch_tag}/module.so

%files -n evas-saver-webp
%defattr(644,root,root,755)
%dir %{_libdir}/evas/modules/savers/webp
%dir %{_libdir}/evas/modules/savers/webp/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/savers/webp/%{arch_tag}/module.so

%files -n vim-addon-efl
%defattr(644,root,root,755)
%doc data/edje/vim/plugin-info.txt
%{_datadir}/vim/autoload/edccomplete.vim
%{_datadir}/vim/vimfiles/ftdetect/edc.vim
%{_datadir}/vim/vimfiles/ftplugin/edc.vim
%{_datadir}/vim/vimfiles/indent/edc.vim
# owner?
%dir %{_datadir}/vim/vimfiles/snippets
%{_datadir}/vim/vimfiles/snippets/edc.snippets
%{_datadir}/vim/vimfiles/syntax/edc.vim
%{_datadir}/vim/vimfiles/syntax/embryo.vim
