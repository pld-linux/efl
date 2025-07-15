# TODO:
# - use system liblinebreak?
# - efl-devel conflicts with libeio-devel
#	file /usr/lib64/libeio.so from install of eio-devel-0.1.0.65643-1.x86_64 conflicts with file from package libeio-devel-1.0-1.x86_64
#
# Conditional build:
%bcond_without	drm		# DRM engine
%bcond_with	fb		# Linux FrameBuffer support
%bcond_without	gstreamer	# GStreamer support
%bcond_without	harfbuzz	# HarfBuzz complex text shaping and layouting support
%bcond_without	luajit		# LuaJIT as Lua engine (Lua 5.1 interpreter if disabled)
%bcond_with	pixman		# pixman for software rendering
%bcond_with	scim		# SCIM input module
%bcond_without	sdl		# SDL support
%bcond_without	systemd		# systemd journal support in Eina, daemon support in Ecore
%bcond_without	wayland		# Wayland display server support
%bcond_without	static_libs	# static libraries build
#
%ifnarch %{ix86} %{x8664} %{arm} mips ppc
%undefine	with_luajit
%endif
Summary:	EFL - The Enlightenment Foundation Libraries
Summary(pl.UTF-8):	EFL (Enlightenment Foundation Libraries) - biblioteki tworzące Enlightment
Name:		efl
Version:	1.27.0
Release:	4
License:	LGPL v2.1+, BSD (depends on component)
Group:		Libraries
Source0:	https://download.enlightenment.org/rel/libs/efl/%{name}-%{version}.tar.xz
# Source0-md5:	0efa0cbdb915752c99861eb91933f59f
Patch0:		lua.patch
URL:		https://www.enlightenment.org/docs/efl/start
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLX-devel
%{?with_sdl:BuildRequires:	SDL2-devel >= 2.0.0}
BuildRequires:	avahi-devel
BuildRequires:	bullet-devel >= 2.80
BuildRequires:	dbus-devel
BuildRequires:	doxygen
BuildRequires:	fontconfig-devel >= 2.5.0
# pkgconfig(freetype2) >= 9.3.0
BuildRequires:	freetype-devel >= 1:2.2
BuildRequires:	fribidi-devel >= 0.19.2
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 2.0
%if %{with gstreamer}
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
%endif
%{?with_harfbuzz:BuildRequires:	harfbuzz-devel >= 0.9.0}
BuildRequires:	ibus-devel >= 1.4
%{?with_drm:BuildRequires:	libdrm-devel >= 2.4}
BuildRequires:	libjpeg-devel
BuildRequires:	libmount-devel >= 2.19.1
BuildRequires:	libpng-devel >= 1.2.10
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libwebp-devel
%{!?with_luajit:BuildRequires:	lua51 >= 5.1.0}
%{?with_luajit:BuildRequires:	luajit >= 2.0.0}
BuildRequires:	openjpeg2-devel >= 2
BuildRequires:	openssl-devel
%if %{with pixman}
BuildRequires:	pixman-devel
%endif
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	pulseaudio-devel
%{?with_scim:BuildRequires:	scim-devel}
BuildRequires:	sed >= 4.0
%{?with_systemd:BuildRequires:	systemd-devel >= 1:209}
BuildRequires:	tslib-devel
BuildRequires:	udev-devel >= 1:148
%if %{with drm} || %{with wayland}
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.3.0
%endif
BuildRequires:	zlib-devel >= 1.2.3
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
%if %{with wayland}
BuildRequires:	wayland-devel >= 1.3.0
BuildRequires:	EGL-devel
BuildRequires:	pkgconfig(egl)
BuildRequires:	wayland-egl-devel >= 1.3.0
%endif
Requires:	SDL2 >= 2.0.0
Requires:	bullet >= 2.80
Requires:	dbus
Requires:	fontconfig-libs >= 2.5.0
Requires:	freetype >= 1:2.2
Requires:	fribidi >= 0.19.2
Requires:	gstreamer >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	harfbuzz >= 0.9.0
Requires:	ibus >= 1.4
Requires:	libdrm >= 2.4
Requires:	libmount >= 2.19.1
Requires:	libpng >= 1.2.10
%{!?with_luajit:Requires:	lua51 >= 5.1.0}
%{?with_luajit:Requires:	luajit >= 2.0.0}
%{?with_scim:Requires:	scim}
%{?with_systemd:Requires:	systemd-libs >= 1:192}
Requires:	udev-libs >= 1:148
Requires:	wayland >= 1.3.0
Requires:	wayland-egl >= 1.3.0
Requires:	xorg-lib-libXi >= 1.6
Requires:	xorg-lib-libXrandr >= 1.3.3
Requires:	xorg-lib-libxkbcommon >= 0.3.0
Requires:	zlib >= 1.2.3
Obsoletes:	ecore < 1.27.0
Obsoletes:	ecore-audio < 1.27.0
Obsoletes:	ecore-con < 1.27.0
Obsoletes:	ecore-config < 1.8
Obsoletes:	ecore-desktop < 1
Obsoletes:	ecore-directfb < 1.8
Obsoletes:	ecore-drm < 1.27.0
Obsoletes:	ecore-evas < 1.27.0
Obsoletes:	ecore-evas-engine-drm < 1.27.0
Obsoletes:	ecore-evas-engine-extn < 1.27.0
Obsoletes:	ecore-evas-engine-fb < 1.27.0
Obsoletes:	ecore-evas-engine-sdl < 1.27.0
Obsoletes:	ecore-evas-engine-wayland < 1.27.0
Obsoletes:	ecore-evas-engine-x < 1.27.0
Obsoletes:	ecore-fb < 1.27.0
Obsoletes:	ecore-file < 1.27.0
Obsoletes:	ecore-imf < 1.27.0
Obsoletes:	ecore-imf-evas < 1.27.0
Obsoletes:	ecore-imf-module-ibus < 1.27.0
Obsoletes:	ecore-imf-module-scim < 1.27.0
Obsoletes:	ecore-imf-module-wayland < 1.27.0
Obsoletes:	ecore-imf-module-xim < 1.27.0
Obsoletes:	ecore-input < 1.27.0
Obsoletes:	ecore-input-evas < 1.27.0
Obsoletes:	ecore-ipc < 1.27.0
Obsoletes:	ecore-job < 1
Obsoletes:	ecore-libs < 0.9.9.036-2
Obsoletes:	ecore-module-ibus < 1.8
Obsoletes:	ecore-module-scim < 1.8
Obsoletes:	ecore-module-xim < 1.8
Obsoletes:	ecore-sdl < 1.27.0
Obsoletes:	ecore-system-systemd < 1.27.0
Obsoletes:	ecore-system-upower < 1.27.0
Obsoletes:	ecore-txt < 1
Obsoletes:	ecore-wayland < 1.27.0
Obsoletes:	ecore-x < 1.27.0
Obsoletes:	edje < 1.27.0
Obsoletes:	edje-libs < 1.27.0
Obsoletes:	edje-module-emotion < 1.27.0
Obsoletes:	eet < 1.27.0
Obsoletes:	eeze < 1.27.0
Obsoletes:	efreet < 1.27.0
Obsoletes:	efreet-libs < 1.27.0
Obsoletes:	eina < 1.27.0
Obsoletes:	eio < 1.27.0
Obsoletes:	eldbus < 1.27.0
Obsoletes:	elua < 1.27.0
Obsoletes:	embryo < 1.27.0
Obsoletes:	emotion < 1.27.0
Obsoletes:	emotion-decoder-gstreamer < 1.27.0
Obsoletes:	enlightenment-utils-eeze < 1.7
Obsoletes:	eo < 1.27.0
Obsoletes:	eolian < 1.27.0
Obsoletes:	ephysics < 1.27.0
Obsoletes:	ethumb < 1.27.0
Obsoletes:	ethumb-libs < 1.27.0
Obsoletes:	ethumb-plugin-emotion < 1.27.0
Obsoletes:	evas < 1.27.0
Obsoletes:	evas-engine-buffer < 1.27.0
Obsoletes:	evas-engine-directfb < 1.8
Obsoletes:	evas-engine-drm < 1.27.0
Obsoletes:	evas-engine-fb < 1.27.0
Obsoletes:	evas-engine-gl_generic < 1.27.0
Obsoletes:	evas-engine-gl_sdl < 1.27.0
Obsoletes:	evas-engine-gl_x11 < 1.27.0
Obsoletes:	evas-engine-software_16 < 1.8
Obsoletes:	evas-engine-software_16_sdl < 1.8
Obsoletes:	evas-engine-software_16_x11 < 1.8
Obsoletes:	evas-engine-software_8 < 1.8
Obsoletes:	evas-engine-software_8_x11 < 1.8
Obsoletes:	evas-engine-software_generic < 1.27.0
Obsoletes:	evas-engine-software_qtopia < 1.1
Obsoletes:	evas-engine-software_x11 < 1.27.0
Obsoletes:	evas-engine-software_xcb < 1.0.0-1
Obsoletes:	evas-engine-wayland_egl < 1.27.0
Obsoletes:	evas-engine-wayland_shm < 1.27.0
Obsoletes:	evas-engine-xrender_x11 < 1.1
Obsoletes:	evas-engine-xrender_xcb < 1.0.0-1
Obsoletes:	evas-libs < 0.9.9.036
Obsoletes:	evas-loader-edb < 1.8
Obsoletes:	evas-loader-eet < 1.27.0
Obsoletes:	evas-loader-gif < 1.27.0
Obsoletes:	evas-loader-jp2k < 1.27.0
Obsoletes:	evas-loader-jpeg < 1.27.0
Obsoletes:	evas-loader-pmaps < 1.27.0
Obsoletes:	evas-loader-png < 1.27.0
Obsoletes:	evas-loader-svg < 1.8
Obsoletes:	evas-loader-tiff < 1.27.0
Obsoletes:	evas-loader-webp < 1.27.0
Obsoletes:	evas-loader-xpm < 1.27.0
Obsoletes:	evas-saver-edb < 1.8
Obsoletes:	evas-saver-eet < 1.27.0
Obsoletes:	evas-saver-jpeg < 1.27.0
Obsoletes:	evas-saver-png < 1.27.0
Obsoletes:	evas-saver-tiff < 1.27.0
Obsoletes:	evas-saver-webp < 1.27.0

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# it used to be linux-gnu-ARCH before...
%define		arch_tag	v-1.27

%description
EFL - The Enlightenment Foundation Libraries.

%description -l pl.UTF-8
EFL (Enlightenment Foundation Libraries) - biblioteki tworzące
Enlightment.

%package devel
Summary:	EFL - The Enlightenment Foundation Libraries
Summary(pl.UTF-8):	EFL (Enlightenment Foundation Libraries) - biblioteki tworzące Enlightment
Requires:	EGL-devel
Requires:	SDL2-devel >= 2.0.0
Requires:	avahi-devel
Requires:	bullet-devel >= 2.80
Requires:	dbus-devel
Requires:	fontconfig-devel >= 2.5.0
Requires:	freetype-devel >= 1:2.2
Requires:	fribidi-devel >= 0.19.2
Requires:	glib2-devel >= 2.0
Requires:	harfbuzz-devel >= 0.9.0
Requires:	libdrm-devel >= 2.4
Requires:	libjpeg-devel
Requires:	libmount-devel >= 2.19.1
Requires:	libsndfile-devel
Requires:	libstdc++-devel
%{!?with_luajit:Requires:	lua51-devel >= 5.1.0}
%{?with_luajit:Requires:	luajit-devel >= 2.0.0}
Requires:	openssl-devel
Requires:	pkgconfig(egl)
Requires:	pulseaudio-devel
%{?with_systemd:Requires:	systemd-devel >= 1:209}
Requires:	tslib-devel
Requires:	udev-devel >= 1:148
Requires:	wayland-devel >= 1.3.0
Requires:	wayland-egl-devel >= 1.3.0
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
Requires:	xorg-lib-libxkbcommon-devel >= 0.3.0
Requires:	zlib-devel >= 1.2.3
Obsoletes:	ecore-audio-cxx-devel < 1.27.0
Obsoletes:	ecore-audio-devel < 1.27.0
Obsoletes:	ecore-avahi-devel < 1.27.0
Obsoletes:	ecore-con-devel < 1.27.0
Obsoletes:	ecore-config-devel < 1.8
Obsoletes:	ecore-cxx-devel < 1.27.0
Obsoletes:	ecore-devel < 1.27.0
Obsoletes:	ecore-directfb-devel < 1.8
Obsoletes:	ecore-drm-devel < 1.27.0
Obsoletes:	ecore-evas-devel < 1.27.0
Obsoletes:	ecore-fb-devel < 1.27.0
Obsoletes:	ecore-file-devel < 1.27.0
Obsoletes:	ecore-imf-devel < 1.27.0
Obsoletes:	ecore-imf-evas-devel < 1.27.0
Obsoletes:	ecore-input-devel < 1.27.0
Obsoletes:	ecore-input-evas-devel < 1.27.0
Obsoletes:	ecore-ipc-devel < 1.27.0
Obsoletes:	ecore-sdl-devel < 1.27.0
Obsoletes:	ecore-wayland-devel < 1.27.0
Obsoletes:	ecore-x-devel < 1.27.0
Obsoletes:	edje-cxx-devel < 1.27.0
Obsoletes:	edje-devel < 1.27.0
Obsoletes:	eet-cxx-devel < 1.27.0
Obsoletes:	eet-devel < 1.27.0
Obsoletes:	eeze-devel < 1.27.0
Obsoletes:	efreet-devel < 1.27.0
Obsoletes:	eina-cxx-devel < 1.27.0
Obsoletes:	eina-devel < 1.27.0
Obsoletes:	eio-devel < 1.27.0
Obsoletes:	eldbus-cxx-devel < 1.27.0
Obsoletes:	eldbus-devel < 1.27.0
Obsoletes:	embryo-devel < 1.27.0
Obsoletes:	emotion-devel < 1.27.0
Obsoletes:	eo-cxx-devel < 1.27.0
Obsoletes:	eo-devel < 1.27.0
Obsoletes:	eo-gdb < 1.27.0
Obsoletes:	eolian-cxx-devel < 1.27.0
Obsoletes:	eolian-devel < 1.27.0
Obsoletes:	ephysics-devel < 1.27.0
Obsoletes:	ethumb-devel < 1.27.0
Obsoletes:	evas-cxx-devel < 1.27.0
Obsoletes:	evas-devel < 1.27.0

%description devel
EFL - The Enlightenment Foundation Libraries.

%description devel -l pl.UTF-8
EFL (Enlightenment Foundation Libraries) - biblioteki tworzące
Enlightment.

%package static
Summary:	EFL - The Enlightenment Foundation Libraries
Summary(pl.UTF-8):	EFL (Enlightenment Foundation Libraries) - biblioteki tworzące Enlightment
Obsoletes:	ecore-audio-static < 1.27.0
Obsoletes:	ecore-avahi-static < 1.27.0
Obsoletes:	ecore-con-static < 1.27.0
Obsoletes:	ecore-config-static < 1.8
Obsoletes:	ecore-directfb-static < 1.8
Obsoletes:	ecore-drm-static < 1.27.0
Obsoletes:	ecore-evas-static < 1.27.0
Obsoletes:	ecore-fb-static < 1.27.0
Obsoletes:	ecore-file-static < 1.27.0
Obsoletes:	ecore-imf-evas-static < 1.27.0
Obsoletes:	ecore-imf-static < 1.27.0
Obsoletes:	ecore-input-evas-static < 1.27.0
Obsoletes:	ecore-input-static < 1.27.0
Obsoletes:	ecore-ipc-static < 1.27.0
Obsoletes:	ecore-sdl-static < 1.27.0
Obsoletes:	ecore-static < 1.27.0
Obsoletes:	ecore-wayland-static < 1.27.0
Obsoletes:	ecore-x-static < 1.27.0
Obsoletes:	edje-static < 1.27.0
Obsoletes:	eet-static < 1.27.0
Obsoletes:	eeze-static < 1.27.0
Obsoletes:	efreet-static < 1.27.0
Obsoletes:	eina-static < 1.27.0
Obsoletes:	eio-static < 1.27.0
Obsoletes:	eldbus-static < 1.27.0
Obsoletes:	embryo-static < 1.27.0
Obsoletes:	emotion-static < 1.27.0
Obsoletes:	eo-static < 1.27.0
Obsoletes:	eolian-static < 1.27.0
Obsoletes:	ephysics-static < 1.27.0
Obsoletes:	ethumb-static < 1.27.0
Obsoletes:	evas-static < 1.27.0

%description static
EFL - The Enlightenment Foundation Libraries.

%description static -l pl.UTF-8
EFL (Enlightenment Foundation Libraries) - biblioteki tworzące
Enlightment.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
      src/bin/exactness/exactness_play.in \
      src/bin/exactness/exactness_record.in

%build
%meson \
	-Decore-imf-loaders-disabler=%{!?with_scim:scim} \
	-Dglib=true \
	-Dphysics=true \
	-Delua=true \
	-Dbuffer=true \
	-Davahi=true \
	%{?with_drm:-Ddrm=true} \
	%{?with_fb:-Dfbtrue} \
	%{!?with_gstreamer:-Dgstreamer=false} \
	%{!?with_harfbuzz:-Dharfbuzz=false} \
	%{!?with_luajit:-Dlua-interpreter=lua} \
	%{?with_pixman:-Dpixman=true} \
	%{?with_sdl:-Dsdl=true} \
	%{!?with_systemd:-Dsystemd=false} \
	%{?with_wayland:-Dwl=true}

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ko_KR

%find_lang efl

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f efl.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/diffeet
%attr(755,root,root) %{_bindir}/ecore_evas_convert
%attr(755,root,root) %{_bindir}/edje_*
%attr(755,root,root) %{_bindir}/eet
%attr(755,root,root) %{_bindir}/eetpack
%attr(755,root,root) %{_bindir}/eeze_*
%attr(755,root,root) %{_bindir}/efl_debug
%attr(755,root,root) %{_bindir}/efl_debugd
%attr(755,root,root) %{_bindir}/efreetd
%attr(755,root,root) %{_bindir}/eina_btlog
%attr(755,root,root) %{_bindir}/eina_modinfo
%attr(755,root,root) %{_bindir}/elementary_codegen
%attr(755,root,root) %{_bindir}/elementary_config
%attr(755,root,root) %{_bindir}/elementary_perf
%attr(755,root,root) %{_bindir}/elementary_quicklaunch
%attr(755,root,root) %{_bindir}/elementary_run
%attr(755,root,root) %{_bindir}/elementary_test
%attr(755,root,root) %{_bindir}/elm_prefs_cc
%attr(755,root,root) %{_bindir}/elua
%attr(755,root,root) %{_bindir}/embryo_cc
%attr(755,root,root) %{_bindir}/emotion_test
%attr(755,root,root) %{_bindir}/emotion_test-eo
%attr(755,root,root) %{_bindir}/eo_debug
%attr(755,root,root) %{_bindir}/eolian_cxx
%attr(755,root,root) %{_bindir}/eolian_gen
%attr(755,root,root) %{_bindir}/ethumb
%attr(755,root,root) %{_bindir}/ethumbd
%attr(755,root,root) %{_bindir}/ethumbd_client
%attr(755,root,root) %{_bindir}/exactness
%attr(755,root,root) %{_bindir}/exactness_inject
%attr(755,root,root) %{_bindir}/exactness_inspect
%attr(755,root,root) %{_bindir}/exactness_play
%attr(755,root,root) %{_bindir}/exactness_record
%attr(755,root,root) %{_bindir}/vieet
%attr(755,root,root) %ghost %{_libdir}/libecore.so.1
%attr(755,root,root) %{_libdir}/libecore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_audio.so.1
%attr(755,root,root) %{_libdir}/libecore_audio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_avahi.so.1
%attr(755,root,root) %{_libdir}/libecore_avahi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_buffer.so.1
%attr(755,root,root) %{_libdir}/libecore_buffer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_con.so.1
%attr(755,root,root) %{_libdir}/libecore_con.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_evas.so.1
%attr(755,root,root) %{_libdir}/libecore_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_file.so.1
%attr(755,root,root) %{_libdir}/libecore_file.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_imf.so.1
%attr(755,root,root) %{_libdir}/libecore_imf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_imf_evas.so.1
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_input.so.1
%attr(755,root,root) %{_libdir}/libecore_input.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_input_evas.so.1
%attr(755,root,root) %{_libdir}/libecore_input_evas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_ipc.so.1
%attr(755,root,root) %{_libdir}/libecore_ipc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_x.so.1
%attr(755,root,root) %{_libdir}/libecore_x.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libedje.so.1
%attr(755,root,root) %{_libdir}/libedje.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeet.so.1
%attr(755,root,root) %{_libdir}/libeet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeeze.so.1
%attr(755,root,root) %{_libdir}/libeeze.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libefreet.so.1
%attr(755,root,root) %{_libdir}/libefreet.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libefreet_mime.so.1
%attr(755,root,root) %{_libdir}/libefreet_mime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libefreet_trash.so.1
%attr(755,root,root) %{_libdir}/libefreet_trash.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeina.so.1
%attr(755,root,root) %{_libdir}/libeina.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeio.so.1
%attr(755,root,root) %{_libdir}/libeio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeldbus.so.1
%attr(755,root,root) %{_libdir}/libeldbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libelua.so.1
%attr(755,root,root) %{_libdir}/libelua.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libembryo.so.1
%attr(755,root,root) %{_libdir}/libembryo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libemotion.so.1
%attr(755,root,root) %{_libdir}/libemotion.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeolian.so.1
%attr(755,root,root) %{_libdir}/libeolian.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeo.so.1
%attr(755,root,root) %{_libdir}/libeo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libethumb.so.1
%attr(755,root,root) %{_libdir}/libethumb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libethumb_client.so.1
%attr(755,root,root) %{_libdir}/libethumb_client.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libevas.so.1
%attr(755,root,root) %{_libdir}/libevas.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_drm2.so.1
%attr(755,root,root) %{_libdir}/libecore_drm2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libector.so.1
%attr(755,root,root) %{_libdir}/libector.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libefl.so.1
%attr(755,root,root) %{_libdir}/libefl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libelementary.so.1
%attr(755,root,root) %{_libdir}/libelementary.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libelput.so.1
%attr(755,root,root) %{_libdir}/libelput.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libemile.so.1
%attr(755,root,root) %{_libdir}/libemile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libeo_dbg.so.1
%attr(755,root,root) %{_libdir}/libeo_dbg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libephysics.so.1
%attr(755,root,root) %{_libdir}/libephysics.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexactness_play.so.1
%attr(755,root,root) %{_libdir}/libexactness_play.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexactness_record.so.1
%attr(755,root,root) %{_libdir}/libexactness_record.so.*.*.*

%dir %{_libdir}/ecore
%dir %{_libdir}/ecore/system
%dir %{_libdir}/ecore/system/upower
%dir %{_libdir}/ecore/system/upower/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore/system/upower/%{arch_tag}/module.so
%dir %{_libdir}/ecore_buffer
%dir %{_libdir}/ecore_buffer/bin
%attr(755,root,root) %{_libdir}/ecore_buffer/bin/bqmgr
%dir %{_libdir}/ecore_buffer/modules
%dir %{_libdir}/ecore_buffer/modules/shm
%dir %{_libdir}/ecore_buffer/modules/shm/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_buffer/modules/shm/v-1.27/module.so
%dir %{_libdir}/ecore_con
%dir %{_libdir}/ecore_con/utils
%dir %{_libdir}/ecore_con/utils/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_con/utils/%{arch_tag}/efl_net_proxy_helper
%dir %{_libdir}/ecore_evas
%dir %{_libdir}/ecore_evas/engines
%dir %{_libdir}/ecore_evas/engines/drm
%dir %{_libdir}/ecore_evas/engines/drm/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/drm/%{arch_tag}/module.so
%dir %{_libdir}/ecore_evas/engines/extn
%dir %{_libdir}/ecore_evas/engines/extn/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/extn/%{arch_tag}/module.so
%if %{with fb}
%attr(755,root,root) %{_libdir}/libecore_fb.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libecore_fb.so.1
%dir %{_libdir}/ecore_evas/engines/fb
%dir %{_libdir}/ecore_evas/engines/fb/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/fb/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/engines/fb
%dir %{_libdir}/evas/modules/engines/fb/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/fb/%{arch_tag}/module.so
%endif
%if %{with sdl}
%attr(755,root,root) %{_libdir}/libecore_sdl.so
%dir %{_libdir}/ecore_evas/engines/sdl
%dir %{_libdir}/ecore_evas/engines/sdl/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/sdl/%{arch_tag}/module.so
%endif
%if %{with wayland}
%attr(755,root,root) %{_libdir}/libecore_wl2.so.1
%attr(755,root,root) %{_libdir}/libecore_wl2.so.*.*.*
%attr(755,root,root) %{_libdir}/libefl_canvas_wl.so.1
%attr(755,root,root) %{_libdir}/libefl_canvas_wl.so.*.*.*
%dir %{_libdir}/ecore_evas/engines/wayland
%dir %{_libdir}/ecore_evas/engines/wayland/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/wayland/%{arch_tag}/module.so
%dir %{_libdir}/ecore_imf/modules/wayland
%dir %{_libdir}/ecore_imf/modules/wayland/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/wayland/%{arch_tag}/module.so
%dir %{_libdir}/ecore_wl2
%dir %{_libdir}/ecore_wl2/engines
%dir %{_libdir}/ecore_wl2/engines/dmabuf
%dir %{_libdir}/ecore_wl2/engines/dmabuf/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_wl2/engines/dmabuf/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/engines/wayland_egl
%dir %{_libdir}/evas/modules/engines/wayland_egl/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/wayland_egl/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/engines/wayland_shm
%dir %{_libdir}/evas/modules/engines/wayland_shm/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/wayland_shm/%{arch_tag}/module.so
%endif
%dir %{_libdir}/ecore_evas/engines/x
%dir %{_libdir}/ecore_evas/engines/x/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_evas/engines/x/%{arch_tag}/module.so
%dir %{_libdir}/ecore_imf
%dir %{_libdir}/ecore_imf/modules
%dir %{_libdir}/ecore_imf/modules/ibus
%dir %{_libdir}/ecore_imf/modules/ibus/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/ibus/%{arch_tag}/module.so
%if %{with scim}
%dir %{_libdir}/ecore_imf/modules/scim
%dir %{_libdir}/ecore_imf/modules/scim/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/scim/%{arch_tag}/module.so
%endif
%dir %{_libdir}/ecore_imf/modules/xim
%dir %{_libdir}/ecore_imf/modules/xim/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore_imf/modules/xim/%{arch_tag}/module.so
%dir %{_libdir}/edje
%dir %{_libdir}/edje/modules
%dir %{_libdir}/edje/modules/elm
%dir %{_libdir}/edje/modules/elm/%{arch_tag}
%attr(755,root,root) %{_libdir}/edje/modules/elm/%{arch_tag}/module.so
%dir %{_libdir}/edje/modules/emotion
%dir %{_libdir}/edje/modules/emotion/%{arch_tag}
%attr(755,root,root) %{_libdir}/edje/modules/emotion/%{arch_tag}/module.so
%dir %{_libdir}/edje/utils
%dir %{_libdir}/edje/utils/%{arch_tag}
%attr(755,root,root) %{_libdir}/edje/utils/%{arch_tag}/epp
%dir %{_libdir}/eeze
%dir %{_libdir}/eeze/modules
%dir %{_libdir}/eeze/modules/sensor
%dir %{_libdir}/eeze/modules/sensor/fake
%dir %{_libdir}/eeze/modules/sensor/fake/%{arch_tag}
%attr(755,root,root) %{_libdir}/eeze/modules/sensor/fake/%{arch_tag}/module.so
%dir %{_libdir}/eeze/modules/sensor/udev
%dir %{_libdir}/eeze/modules/sensor/udev/%{arch_tag}
%attr(755,root,root) %{_libdir}/eeze/modules/sensor/udev/%{arch_tag}/module.so
%dir %{_libdir}/efreet
%dir %{_libdir}/efreet/%{arch_tag}
%attr(755,root,root) %{_libdir}/efreet/%{arch_tag}/efreet_desktop_cache_create
%attr(755,root,root) %{_libdir}/efreet/%{arch_tag}/efreet_icon_cache_create
%attr(755,root,root) %{_libdir}/efreet/%{arch_tag}/efreet_mime_cache_create
%dir %{_libdir}/elementary
%dir %{_libdir}/elementary/modules
%dir %{_libdir}/elementary/modules/access_output
%dir %{_libdir}/elementary/modules/access_output/%{arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/access_output/%{arch_tag}/module.so
%dir %{_libdir}/elementary/modules/prefs
%dir %{_libdir}/elementary/modules/prefs/%{arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/prefs/%{arch_tag}/module.so
%dir %{_libdir}/elementary/modules/test_entry
%dir %{_libdir}/elementary/modules/test_entry/%{arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/test_entry/%{arch_tag}/module.so
%dir %{_libdir}/elementary/modules/test_map
%dir %{_libdir}/elementary/modules/test_map/%{arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/test_map/%{arch_tag}/module.so
%dir %{_libdir}/elementary/modules/web
%dir %{_libdir}/elementary/modules/web/none
%dir %{_libdir}/elementary/modules/web/none/%{arch_tag}
%attr(755,root,root) %{_libdir}/elementary/modules/web/none/%{arch_tag}/module.so
%dir %{_libdir}/emotion
%dir %{_libdir}/emotion/modules
%if %{with gstreamer}
%dir %{_libdir}/emotion/modules/gstreamer1
%dir %{_libdir}/emotion/modules/gstreamer1/%{arch_tag}
%attr(755,root,root) %{_libdir}/emotion/modules/gstreamer1/%{arch_tag}/module.so
%endif
%dir %{_libdir}/ethumb
%dir %{_libdir}/ethumb/modules
%dir %{_libdir}/ethumb/modules/emotion
%dir %{_libdir}/ethumb/modules/emotion/%{arch_tag}
%attr(755,root,root) %{_libdir}/ethumb/modules/emotion/%{arch_tag}/module.so
%dir %{_libdir}/ethumb_client
%dir %{_libdir}/ethumb_client/utils
%dir %{_libdir}/ethumb_client/utils/%{arch_tag}
%attr(755,root,root) %{_libdir}/ethumb_client/utils/%{arch_tag}/ethumbd_slave
%dir %{_libdir}/evas
%dir %{_libdir}/evas/modules
%dir %{_libdir}/evas/modules/engines
%if %{with drm}
%dir %{_libdir}/evas/modules/engines/drm
%dir %{_libdir}/evas/modules/engines/drm/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/drm/%{arch_tag}/module.so
%endif
%dir %{_libdir}/evas/modules/image_loaders
%dir %{_libdir}/evas/modules/engines/buffer
%dir %{_libdir}/evas/modules/engines/buffer/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/buffer/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/engines/gl_drm
%dir %{_libdir}/evas/modules/engines/gl_drm/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/gl_drm/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/engines/gl_generic
%dir %{_libdir}/evas/modules/engines/gl_generic/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/gl_generic/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/engines/gl_x11
%dir %{_libdir}/evas/modules/engines/gl_x11/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/gl_x11/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/engines/software_x11
%dir %{_libdir}/evas/modules/engines/software_x11/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/engines/software_x11/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/bmp
%dir %{_libdir}/evas/modules/image_loaders/bmp/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/bmp/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/generic
%dir %{_libdir}/evas/modules/image_loaders/generic/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/generic/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/gif
%dir %{_libdir}/evas/modules/image_loaders/gif/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/gif/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/ico
%dir %{_libdir}/evas/modules/image_loaders/ico/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/ico/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/jp2k
%dir %{_libdir}/evas/modules/image_loaders/jp2k/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/jp2k/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/pmaps
%dir %{_libdir}/evas/modules/image_loaders/pmaps/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/pmaps/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/psd
%dir %{_libdir}/evas/modules/image_loaders/psd/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/psd/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/qoi
%dir %{_libdir}/evas/modules/image_loaders/qoi/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/qoi/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/tga
%dir %{_libdir}/evas/modules/image_loaders/tga/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/tga/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/tgv
%dir %{_libdir}/evas/modules/image_loaders/tgv/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/tgv/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/tiff
%dir %{_libdir}/evas/modules/image_loaders/tiff/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/tiff/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/wbmp
%dir %{_libdir}/evas/modules/image_loaders/wbmp/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/wbmp/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/webp
%dir %{_libdir}/evas/modules/image_loaders/webp/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/webp/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_loaders/xpm
%dir %{_libdir}/evas/modules/image_loaders/xpm/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_loaders/xpm/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_savers
%dir %{_libdir}/evas/modules/image_savers/qoi
%dir %{_libdir}/evas/modules/image_savers/qoi/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_savers/qoi/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_savers/tgv
%dir %{_libdir}/evas/modules/image_savers/tgv/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_savers/tgv/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_savers/tiff
%dir %{_libdir}/evas/modules/image_savers/tiff/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_savers/tiff/%{arch_tag}/module.so
%dir %{_libdir}/evas/modules/image_savers/webp
%dir %{_libdir}/evas/modules/image_savers/webp/%{arch_tag}
%attr(755,root,root) %{_libdir}/evas/modules/image_savers/webp/%{arch_tag}/module.so
%dir %{_libdir}/evas/utils
%attr(755,root,root) %{_libdir}/evas/utils/*
%if %{with systemd}
%dir %{_libdir}/ecore/system/systemd
%dir %{_libdir}/ecore/system/systemd/%{arch_tag}
%attr(755,root,root) %{_libdir}/ecore/system/systemd/%{arch_tag}/module.so
%{systemduserunitdir}/ethumb.service
%endif
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ecore
%{_datadir}/ecore_imf
%{_datadir}/ecore_x
%{_datadir}/edje
%{_datadir}/eeze
%{_datadir}/efreet
%{_datadir}/elementary
%{_datadir}/elua
%{_datadir}/embryo
%{_datadir}/emotion
%{_datadir}/eolian
%{_datadir}/ethumb
%{_datadir}/ethumb_client
%{_datadir}/evas
%{_datadir}/exactness
%{_datadir}/mime/packages/edje.xml
%{_datadir}/mime/packages/evas.xml
%{_desktopdir}/elementary_config.desktop
%{_desktopdir}/elementary_perf.desktop
%{_desktopdir}/elementary_test.desktop
%{_iconsdir}/Enlightenment-X
%{_iconsdir}/hicolor/128x128/apps/elementary.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/efl_canvas_wl_test*
%attr(755,root,root) %{_bindir}/eldbus-codegen
%attr(755,root,root) %{_libdir}/libector.so
%attr(755,root,root) %{_libdir}/libefl.so
%attr(755,root,root) %{_libdir}/libelementary.so
%attr(755,root,root) %{_libdir}/libelput.so
%attr(755,root,root) %{_libdir}/libemile.so
%attr(755,root,root) %{_libdir}/libeo_dbg.so
%attr(755,root,root) %{_libdir}/libexactness_play.so
%attr(755,root,root) %{_libdir}/libexactness_record.so
%attr(755,root,root) %{_libdir}/libecore_audio.so
%attr(755,root,root) %{_libdir}/libecore_avahi.so
%attr(755,root,root) %{_libdir}/libecore_buffer.so
%attr(755,root,root) %{_libdir}/libecore_con.so
%attr(755,root,root) %{_libdir}/libecore_drm2.so
%attr(755,root,root) %{_libdir}/libecore_evas.so
%attr(755,root,root) %{_libdir}/libecore_file.so
%attr(755,root,root) %{_libdir}/libecore_imf_evas.so
%attr(755,root,root) %{_libdir}/libecore_imf.so
%attr(755,root,root) %{_libdir}/libecore_input_evas.so
%attr(755,root,root) %{_libdir}/libecore_input.so
%attr(755,root,root) %{_libdir}/libecore_ipc.so
%attr(755,root,root) %{_libdir}/libecore.so
%attr(755,root,root) %{_libdir}/libecore_x.so
%attr(755,root,root) %{_libdir}/libedje.so
%attr(755,root,root) %{_libdir}/libeet.so
%attr(755,root,root) %{_libdir}/libeeze.so
%attr(755,root,root) %{_libdir}/libefreet_mime.so
%attr(755,root,root) %{_libdir}/libefreet.so
%attr(755,root,root) %{_libdir}/libefreet_trash.so
%attr(755,root,root) %{_libdir}/libeina.so
%attr(755,root,root) %{_libdir}/libeio.so
%attr(755,root,root) %{_libdir}/libeldbus.so
%attr(755,root,root) %{_libdir}/libelua.so
%attr(755,root,root) %{_libdir}/libembryo.so
%attr(755,root,root) %{_libdir}/libemotion.so
%attr(755,root,root) %{_libdir}/libeolian.so
%attr(755,root,root) %{_libdir}/libeo.so
%attr(755,root,root) %{_libdir}/libephysics.so
%attr(755,root,root) %{_libdir}/libethumb_client.so
%attr(755,root,root) %{_libdir}/libethumb.so
%attr(755,root,root) %{_libdir}/libevas.so
%{_includedir}/ecore-1
%{_includedir}/ecore-audio-1
%{_includedir}/ecore-avahi-1
%{_includedir}/ecore-buffer-1
%{_includedir}/ecore-con-1
%{_includedir}/ecore-cxx-1
%{_includedir}/ecore-evas-1
%{_includedir}/ecore-file-1
%{_includedir}/ecore-imf-1
%{_includedir}/ecore-imf-evas-1
%{_includedir}/ecore-input-1
%{_includedir}/ecore-input-evas-1
%{_includedir}/ecore-ipc-1
%{_includedir}/ecore-drm2-1
%{_includedir}/elput-1
%{_includedir}/emile-1
%{_includedir}/ecore-x-1
%{_includedir}/edje-1
%{_includedir}/edje-cxx-1
%{_includedir}/eet-1
%{_includedir}/eet-cxx-1
%{_includedir}/eeze-1
%{_includedir}/efl-1
%{_includedir}/efl-cxx-1
%{_includedir}/efreet-1
%{_includedir}/eina-1
%{_includedir}/eina-cxx-1
%{_includedir}/eio-1
%{_includedir}/eio-cxx-1
%{_includedir}/eldbus-1
%{_includedir}/eldbus-cxx-1
%{_includedir}/elementary-1
%{_includedir}/elementary-cxx-1
%{_includedir}/elua-1
%{_includedir}/embryo-1
%{_includedir}/emotion-1
%{_includedir}/eo-1
%{_includedir}/eo-cxx-1
%{_includedir}/eolian-1
%{_includedir}/eolian-cxx-1
%{_includedir}/ephysics-1
%{_includedir}/ethumb-1
%{_includedir}/ethumb-client-1
%{_includedir}/evas-1
%{_includedir}/evas-cxx-1
%{_libdir}/cmake/Efl
%{_libdir}/cmake/Eio
%{_libdir}/cmake/Elementary
%{_libdir}/cmake/Elua
%{_libdir}/cmake/Emile
%{_libdir}/cmake/Ecore
%{_libdir}/cmake/EcoreCxx
%{_libdir}/cmake/Edje
%{_libdir}/cmake/Eet
%{_libdir}/cmake/EetCxx
%{_libdir}/cmake/Eeze
%{_libdir}/cmake/Efreet
%{_libdir}/cmake/Eina
%{_libdir}/cmake/EinaCxx
%{_libdir}/cmake/Eldbus
%{_libdir}/cmake/Emotion
%{_libdir}/cmake/Eo
%{_libdir}/cmake/EoCxx
%{_libdir}/cmake/Eolian
%{_libdir}/cmake/EolianCxx
%{_libdir}/cmake/Ethumb
%{_libdir}/cmake/EthumbClient
%{_libdir}/cmake/Evas
%{_libdir}/cmake/EvasCxx
%{_pkgconfigdir}/*.pc
%dir %{_datadir}/eo
%{_datadir}/eo/gdb
%{_datadir}/gdb/auto-load/usr/lib/libeo.so.1.27.0-gdb.py
%if %{with fb}
%attr(755,root,root) %{_libdir}/libecore_fb.so
%{_includedir}/ecore-fb-1
%endif
%if %{with sdl}
%{_includedir}/ecore-sdl-1
%endif
%if %{with wayland}
%attr(755,root,root) %{_libdir}/libecore_wl2.so
%attr(755,root,root) %{_libdir}/libefl_canvas_wl.so
%{_includedir}/ecore-wl2-1
%{_includedir}/efl-canvas-wl-1
%endif

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
