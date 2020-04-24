### RPM external triton-inference-server 1.12.0
%define branch master
%define github_user NVIDIA

Source: git+https://github.com/%{github_user}/triton-inference-server.git?obj=%{branch}/v%{realversion}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz
BuildRequires: cmake
Requires: opencv protobuf grpc python py2-wheel py2-setuptools py2-grpcio-tools

%prep

%setup -n %{n}-%{realversion}

%build

cd build
cmake ../%{n}-%{realversion} \
    -DCMAKE_INSTALL_PREFIX="%{i}" \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_BUILD_TYPE=Release \
    -DTRTIS_ENABLE_GPU=OFF \
make %{makeprocesses} trtis-clients

%install

make install

