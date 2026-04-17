# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           act_runner
Version:        0.4.0
Release:        %autorelease
Summary:        A runner for Gitea based on act
License:        MIT
ExclusiveArch:  riscv64
URL:            https://gitea.com/gitea/act_runner
#!RemoteAsset:  sha256:6d830c16afb15fb2924ab4a8981727aa2f11fed637413e12041e650c9b737d4b
Source0:        https://gitea.com/gitea/act_runner/releases/download/v%{version}/act_runner-%{version}-linux-riscv64.xz
Source1:        act_runner.service
Source2:        LICENSE

%description
Act runner is a runner for Gitea based on Gitea fork of act..

%prep
%setup -q -T
mv act_runner-%{version}-linux- act_runner

%conf

%build

%install
mkdir %{buildroot}/var/lib/gitea-runner
cp act_runner-%{version}-linux-riscv64 %{buildroot}/var/lib/gitea-runner/
cp %{SOURCE1} %{buildroot}/var/lib/gitea-runner/
chmod +x cp act_runner-%{version}-linux-riscv64 %{buildroot}/var/lib/gitea-runner/act_runner-%{version}-linux-riscv64
cd %{buildroot}/var/lib/gitea-runner
ln -sf act_runner-%{version}-linux-riscv64 act_runner

mkdir -p %{buildroot}%{_datadir}/licenses/%{name}
cp %{SOURCE2} %{buildroot}%{_datadir}/licenses/%{name}/

%check

%files
%license %{_datadir}/licenses/gitea-runner/LICENSE
%{_unitdir}/act_runner.service
%{_sharedstatedir}/gitea-runner

%changelog
%autochangelog
