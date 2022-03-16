#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imlib2
Version  : 1.8.1
Release  : 21
URL      : https://sourceforge.net/projects/enlightenment/files/imlib2-src/1.8.1/imlib2-1.8.1.tar.xz
Source0  : https://sourceforge.net/projects/enlightenment/files/imlib2-src/1.8.1/imlib2-1.8.1.tar.xz
Summary  : Powerful image loading and rendering library
Group    : Development/Tools
License  : Imlib2
Requires: imlib2-bin = %{version}-%{release}
Requires: imlib2-data = %{version}-%{release}
Requires: imlib2-lib = %{version}-%{release}
Requires: imlib2-license = %{version}-%{release}
BuildRequires : giflib-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : librsvg-dev
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-shm)

%description
Imlib2 1.8.1
This is the Imlib 2 library - a library that does image file loading and
saving as well as rendering, manipulation, arbitrary polygon support, etc.

%package bin
Summary: bin components for the imlib2 package.
Group: Binaries
Requires: imlib2-data = %{version}-%{release}
Requires: imlib2-license = %{version}-%{release}

%description bin
bin components for the imlib2 package.


%package data
Summary: data components for the imlib2 package.
Group: Data

%description data
data components for the imlib2 package.


%package dev
Summary: dev components for the imlib2 package.
Group: Development
Requires: imlib2-lib = %{version}-%{release}
Requires: imlib2-bin = %{version}-%{release}
Requires: imlib2-data = %{version}-%{release}
Provides: imlib2-devel = %{version}-%{release}
Requires: imlib2 = %{version}-%{release}

%description dev
dev components for the imlib2 package.


%package lib
Summary: lib components for the imlib2 package.
Group: Libraries
Requires: imlib2-data = %{version}-%{release}
Requires: imlib2-license = %{version}-%{release}

%description lib
lib components for the imlib2 package.


%package license
Summary: license components for the imlib2 package.
Group: Default

%description license
license components for the imlib2 package.


%prep
%setup -q -n imlib2-1.8.1
cd %{_builddir}/imlib2-1.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647440432
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1647440432
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/imlib2
cp %{_builddir}/imlib2-1.8.1/COPYING %{buildroot}/usr/share/package-licenses/imlib2/4bb00a078e16718ff6547e7ec70b558a8dd3680a
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/imlib2_bumpmap
/usr/bin/imlib2_colorspace
/usr/bin/imlib2_conv
/usr/bin/imlib2_grab
/usr/bin/imlib2_load
/usr/bin/imlib2_poly
/usr/bin/imlib2_show
/usr/bin/imlib2_test
/usr/bin/imlib2_view

%files data
%defattr(-,root,root,-)
/usr/share/imlib2/data/fonts/cinema.ttf
/usr/share/imlib2/data/fonts/grunge.ttf
/usr/share/imlib2/data/fonts/morpheus.ttf
/usr/share/imlib2/data/fonts/notepad.ttf
/usr/share/imlib2/data/images/audio.png
/usr/share/imlib2/data/images/bg.png
/usr/share/imlib2/data/images/bulb.png
/usr/share/imlib2/data/images/cal.png
/usr/share/imlib2/data/images/calc.png
/usr/share/imlib2/data/images/folder.png
/usr/share/imlib2/data/images/globe.png
/usr/share/imlib2/data/images/imlib2.png
/usr/share/imlib2/data/images/lock.png
/usr/share/imlib2/data/images/mail.png
/usr/share/imlib2/data/images/menu.png
/usr/share/imlib2/data/images/mush.png
/usr/share/imlib2/data/images/paper.png
/usr/share/imlib2/data/images/sh1.png
/usr/share/imlib2/data/images/sh2.png
/usr/share/imlib2/data/images/sh3.png
/usr/share/imlib2/data/images/stop.png
/usr/share/imlib2/data/images/tnt.png

%files dev
%defattr(-,root,root,-)
/usr/include/Imlib2.h
/usr/lib64/libImlib2.so
/usr/lib64/pkgconfig/imlib2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/imlib2/filters/bumpmap.so
/usr/lib64/imlib2/filters/colormod.so
/usr/lib64/imlib2/filters/testfilter.so
/usr/lib64/imlib2/loaders/argb.so
/usr/lib64/imlib2/loaders/bmp.so
/usr/lib64/imlib2/loaders/bz2.so
/usr/lib64/imlib2/loaders/ff.so
/usr/lib64/imlib2/loaders/gif.so
/usr/lib64/imlib2/loaders/ico.so
/usr/lib64/imlib2/loaders/jpeg.so
/usr/lib64/imlib2/loaders/lbm.so
/usr/lib64/imlib2/loaders/png.so
/usr/lib64/imlib2/loaders/pnm.so
/usr/lib64/imlib2/loaders/svg.so
/usr/lib64/imlib2/loaders/tga.so
/usr/lib64/imlib2/loaders/xbm.so
/usr/lib64/imlib2/loaders/xpm.so
/usr/lib64/imlib2/loaders/zlib.so
/usr/lib64/libImlib2.so.1
/usr/lib64/libImlib2.so.1.8.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/imlib2/4bb00a078e16718ff6547e7ec70b558a8dd3680a
