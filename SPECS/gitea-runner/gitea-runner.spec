# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gitea-runner
Version:        1.0.3
Release:        %autorelease
Summary:        A runner for Gitea based on act
License:        MIT
ExclusiveArch:  riscv64
URL:            https://gitea.com/gitea/runner
#!RemoteAsset:  sha256:b9d995ee8ecacf5bff0720e49a61735760ca1ede879dbfbdbe87889b58113b99
Source0:        https://gitea.com/gitea/runner/releases/download/v%{version}/gitea-runner-%{version}-linux-riscv64.xz
Source1:        gitea-runner.service
Source2:        LICENSE

%description
Act runner is a runner for Gitea based on Gitea fork of act..

%prep
xz -dc %{SOURCE0} > gitea-runner
cp %{SOURCE2} ./

%conf
# No conf.

%build
# No build.

%install
mkdir -p %{buildroot}/var/lib/gitea-runner
install -m755 gitea-runner %{buildroot}%{_sharedstatedir}/gitea-runner/

mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}/

%check
# No tests.

%files
%license LICENSE
%{_unitdir}/gitea-runner.service
%{_sharedstatedir}/gitea-runner

%changelog
%autochangelog
