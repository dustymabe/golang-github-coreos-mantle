# https://github.com/coreos/mantle
%global provider_tld    com
%global provider        github
%global project         coreos
%global repo            mantle
%global import_path     github.com/coreos/mantle
%global goipath         {%provider_prefix}
%global commit          490b74e13080d984385ccc2daec22d995a483d3f
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%gometa

Name:           golang-github-coreos-mantle
Version:        0
Release:        0.1%{?dist}
Summary:        Collection of tools for developing Container Linux
License:        ASL2.0
URL:            %{gourl}
Source0:        %{gosource}

# Remaining dependencies not included in main packages
BuildRequires: golang(github.com/kballard/go-shellquote)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires: golang(github.com/coreos/container-linux-config-transpiler/config)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/vhdcore/diskstream)
BuildRequires: golang(github.com/coreos/go-omaha/omaha)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/vhdcore/common)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/client)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(github.com/vmware/govmomi/object)
BuildRequires: golang(github.com/coreos/ignition/config/v2_1/types)
BuildRequires: golang(github.com/vishvananda/netns)
BuildRequires: golang(github.com/vishvananda/netlink)
BuildRequires: golang(github.com/pborman/uuid)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(github.com/coreos/ignition/config/shared/errors)
BuildRequires: golang(github.com/coreos/container-linux-config-transpiler/config/platform)
BuildRequires: golang(github.com/coreos/pkg/multierror)
BuildRequires: golang(github.com/vmware/govmomi/find)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/storage)
BuildRequires: golang(github.com/vmware/govmomi/vim25)
BuildRequires: golang(github.com/vmware/govmomi/vim25/soap)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/endpoints)
BuildRequires: golang(github.com/coreos/ignition/config/v2_0)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires: golang(github.com/coreos/ignition/config/v1/types)
BuildRequires: golang(github.com/coreos/ignition/config/v2_3)
BuildRequires: golang(github.com/coreos/ignition/config/v2_2/types)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires: golang(github.com/vmware/govmomi/vim25/types)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/godbus/dbus)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(github.com/vincent-petithory/dataurl)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/management)
BuildRequires: golang(github.com/coreos/ignition/config/v2_1)
BuildRequires: golang(github.com/coreos/ioprogress)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/sts)
BuildRequires: golang(github.com/coreos/ignition/config/v2_0/types)
BuildRequires: golang(github.com/coreos/etcd/pkg/types)
BuildRequires: golang(github.com/coreos/ignition/config/v1)
BuildRequires: golang(github.com/coreos/coreos-cloudinit/config)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/upload)
BuildRequires: golang(github.com/coreos/etcd/etcdserver/api/v2http)
BuildRequires: golang(github.com/coreos/etcd/etcdserver)
BuildRequires: golang(github.com/vmware/govmomi/vim25/mo)
BuildRequires: golang(github.com/coreos/ignition/config/v2_2)
BuildRequires: golang(github.com/vmware/govmomi/vim25/progress)
BuildRequires: golang(github.com/coreos/ignition/config/v2_3/types)
BuildRequires: golang(github.com/pin/tftp)
BuildRequires: golang(github.com/vmware/govmomi)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/upload/metadata)
BuildRequires: golang(golang.org/x/crypto/openpgp)
BuildRequires: golang(github.com/packethost/packngo)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/management/location)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/iam)
BuildRequires: golang(github.com/vmware/govmomi/ovf)
BuildRequires: golang(github.com/digitalocean/godo)

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/Azure/azure-sdk-for-go/management)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/management/location)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/management/storageservice)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/storage)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/upload)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/upload/metadata)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/vhdcore/common)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/vhdcore/diskstream)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/vhdcore/validator)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/awserr)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/client)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/credentials)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/endpoints)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/request)
BuildRequires: golang(github.com/aws/aws-sdk-go/aws/session)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/ec2)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/iam)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/s3/s3manager)
BuildRequires: golang(github.com/aws/aws-sdk-go/service/sts)
BuildRequires: golang(github.com/coreos/container-linux-config-transpiler/config)
BuildRequires: golang(github.com/coreos/container-linux-config-transpiler/config/platform)
BuildRequires: golang(github.com/coreos/coreos-cloudinit/config)
BuildRequires: golang(github.com/coreos/etcd/etcdserver)
BuildRequires: golang(github.com/coreos/etcd/etcdserver/api/v2http)
BuildRequires: golang(github.com/coreos/etcd/pkg/types)
BuildRequires: golang(github.com/coreos/go-omaha/omaha)
BuildRequires: golang(github.com/coreos/go-semver/semver)
BuildRequires: golang(github.com/coreos/ignition/config/shared/errors)
BuildRequires: golang(github.com/coreos/ignition/config/v1)
BuildRequires: golang(github.com/coreos/ignition/config/v1/types)
BuildRequires: golang(github.com/coreos/ignition/config/v2_0)
BuildRequires: golang(github.com/coreos/ignition/config/v2_0/types)
BuildRequires: golang(github.com/coreos/ignition/config/v2_1)
BuildRequires: golang(github.com/coreos/ignition/config/v2_1/types)
BuildRequires: golang(github.com/coreos/ignition/config/v2_2)
BuildRequires: golang(github.com/coreos/ignition/config/v2_2/types)
BuildRequires: golang(github.com/coreos/ignition/config/v2_3)
BuildRequires: golang(github.com/coreos/ignition/config/v2_3/types)
BuildRequires: golang(github.com/coreos/ioprogress)
BuildRequires: golang(github.com/coreos/pkg/capnslog)
BuildRequires: golang(github.com/coreos/pkg/multierror)
BuildRequires: golang(github.com/digitalocean/godo)
BuildRequires: golang(github.com/godbus/dbus)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/kballard/go-shellquote)
BuildRequires: golang(github.com/packethost/packngo)
BuildRequires: golang(github.com/pborman/uuid)
BuildRequires: golang(github.com/pin/tftp)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/vincent-petithory/dataurl)
BuildRequires: golang(github.com/vishvananda/netlink)
BuildRequires: golang(github.com/vishvananda/netns)
BuildRequires: golang(github.com/vmware/govmomi)
BuildRequires: golang(github.com/vmware/govmomi/find)
BuildRequires: golang(github.com/vmware/govmomi/object)
BuildRequires: golang(github.com/vmware/govmomi/ovf)
BuildRequires: golang(github.com/vmware/govmomi/vim25)
BuildRequires: golang(github.com/vmware/govmomi/vim25/mo)
BuildRequires: golang(github.com/vmware/govmomi/vim25/progress)
BuildRequires: golang(github.com/vmware/govmomi/vim25/soap)
BuildRequires: golang(github.com/vmware/govmomi/vim25/types)
BuildRequires: golang(golang.org/x/crypto/openpgp)
BuildRequires: golang(golang.org/x/crypto/ssh)
BuildRequires: golang(golang.org/x/crypto/ssh/agent)
BuildRequires: golang(golang.org/x/crypto/ssh/terminal)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(golang.org/x/oauth2/google)
BuildRequires: golang(golang.org/x/sys/unix)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(google.golang.org/api/googleapi)
BuildRequires: golang(google.golang.org/api/storage/v1)

%description
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

############## kola subpackage ##############
%package kola
Summary:   A tool for launching instances and running tests
BuildRequires: golang(github.com/coreos/pkg/capnslog)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(golang.org/x/crypto/ssh)
BuildRequires: golang(golang.org/x/crypto/ssh/agent)

%description kola
%{summary}

############## kolet subpackage ##############
%package kolet
Summary:  A kola agent that runs on instances
BuildRequires: golang(github.com/coreos/pkg/capnslog)
BuildRequires: golang(github.com/spf13/cobra)

%description kolet
%{summary}

############### ore subpackage ###############
%package ore
Summary:  A tool for interfacing with cloud providers
BuildRequires: golang(github.com/spf13/cobra)

%description ore
%{summary}

################ plume subpackage #############
%package plume
Summary: A tool for releasing cloud images
BuildRequires: golang(github.com/coreos/pkg/capnslog)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/Azure/azure-sdk-for-go/management/storageservice)
BuildRequires: golang(github.com/Microsoft/azure-vhd-utils/vhdcore/validator)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/api/compute/v1)
BuildRequires: golang(google.golang.org/api/storage/v1)

%description plume
%{summary}

################ gangue subpackage #############
%package gangue
Summary: A tool for downloading from Google Storage
BuildRequires: golang(github.com/spf13/cobra)

%description gangue
%{summary}

%prep
%gosetup -q


%build
%gobuildroot

%gobuild -o _bin/cmd/gangue %{import_path}/cmd/gangue
%gobuild -o _bin/cmd/kola %{import_path}/cmd/kola
%gobuild -o _bin/cmd/kolet %{import_path}/cmd/kolet
%gobuild -o _bin/cmd/ore %{import_path}/cmd/ore
%gobuild -o _bin/cmd/plume %{import_path}/cmd/plume

%install
# main package
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 _bin/cmd/gangue %{buildroot}%{_bindir}
install -p -m 0755 _bin/cmd/kola %{buildroot}%{_bindir}
install -p -m 0755 _bin/cmd/kolet %{buildroot}%{_bindir}
install -p -m 0755 _bin/cmd/ore %{buildroot}%{_bindir}
install -p -m 0755 _bin/cmd/plume %{buildroot}%{_bindir}

%goinstall

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files
%license LICENSE
%doc README.md platforms.md code-of-conduct.md runner-readme.md CONTRIBUTING.md

%files kola
%{_bindir}/cmd/kola

%files kolet
%{_bindir}/cmd/kolet

%files ore
%{_bindir}/cmd/ore

%files plume
%{_bindir}/cmd/plume

%files devel -f devel.file-list
%license LICENSE
%doc README.md platforms.md code-of-conduct.md runner-readme.md CONTRIBUTING.md

%changelog
* Mon Dec 17 2018 Sayan Chowdhury <sayanchowdhury@fedoraproject.org>
- First package for Fedora

