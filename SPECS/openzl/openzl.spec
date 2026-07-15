# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openzl
Version:        0.2.0
Release:        %autorelease
Summary:        A specialized compressor optimized for specific data formats
License:        BSD-3-Clause
URL:            https://github.com/facebook/openzl
#!RemoteAsset:  sha256:2ad14ed9af63d4a70cb05df5d5629871d052371ad017cf5559dc76c41ae3865f
Source0:        https://github.com/facebook/openzl/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

Patch2000:      2000-fix-install-missing-libs.patch
Patch2001:      2001-feat-prefer-system-installed-zstd-and-lz4-over-bundl.patch
Patch2002:      2002-fix-disable-ml_selector.patch

BuildOption(conf):  -DCMAKE_EXE_LINKER_FLAGS="%{build_ldflags} -Wl,--as-needed"
BuildOption(conf):  -DCMAKE_MODULE_LINKER_FLAGS="%{build_ldflags} -Wl,--as-needed"
BuildOption(conf):  -DCMAKE_SHARED_LINKER_FLAGS="%{build_ldflags} -Wl,--as-needed"
BuildOption(conf):  -DOPENZL_BUILD_TESTS:BOOL=OFF
BuildOption(conf):  -DOPENZL_BUILD_BENCHMARKS:BOOL=OFF
BuildOption(conf):  -DBUILD_SHARED_LIBS:BOOL=ON
BuildOption(conf):  -DOPENZL_BUILD_CPP:BOOL=ON
BuildOption(conf):  -DOPENZL_CPP_INSTALL:BOOL=ON
BuildOption(conf):  -DOPENZL_BUILD_TOOLS:BOOL=OFF
BuildOption(conf):  -DOPENZL_BUILD_CLI:BOOL=ON
BuildOption(conf):  -DOPENZL_BUILD_EXAMPLES:BOOL=OFF
BuildOption(conf):  -DOPENZL_ALLOW_INTROSPECTION:BOOL=OFF
BuildOption(conf):  -DCMAKE_POSITION_INDEPENDENT_CODE=ON
BuildOption(conf):  -DZSTD_BUILD_STATIC:BOOL=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(liblz4)

%description
OpenZL delivers high compression ratios while preserving high speed. It takes a
description of your data and builds from it a specialized compressor optimized
for your specific format. This package provides the runtime libraries and tools.

%package        devel
Summary:        Development files for the OpenZL library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, pkg-config files, and other
files needed to develop applications that use the OpenZL library.

%install -a
# remove files belong to zstd
rm -f %{buildroot}%{_libdir}/pkgconfig/libzstd.pc
rm -rf %{buildroot}%{_libdir}/cmake/zstd/
rm -f %{buildroot}%{_includedir}/zstd.h
rm -f %{buildroot}%{_includedir}/zdict.h
rm -f %{buildroot}%{_includedir}/zstd_errors.h
rm -f %{buildroot}%{_libdir}/libzstd*

%files
%license LICENSE
%doc README.md
%{_libdir}/lib*.so.*
%{_bindir}/zli

%files devel
%{_includedir}/openzl/
%{_libdir}/lib*.so
%{_libdir}/cmake/openzl/*.cmake

%changelog
%autochangelog
