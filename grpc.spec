### RPM external grpc 1.27.3

Source: git+https://github.com/grpc/grpc.git?obj=master/v%{realversion}&export=%{n}-%{realversion}&submodules=1&output=/%{n}-%{realversion}.tgz

BuildRequires: cmake ninja
Requires: protobuf zlib libunwind

%prep

%setup -n %{n}-%{realversion}

%build

rm -rf ../build
mkdir ../build
cd ../build

pwd

cmake ../%{n}-%{realversion} \
    -G Ninja \
    -DgRPC_INSTALL=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DgRPC_ABSL_PROVIDER=module \
    -DgRPC_CARES_PROVIDER=module \
    -DgRPC_PROTOBUF_PROVIDER=package \
    -DProtobuf_LIBRARIES=${PROTOBUF_ROOT}/lib \
    -DProtobuf_INCLUDE_DIR=${PROTOBUF_ROOT}/include \
    -DProtobuf_LIBRARY=${PROTOBUF_ROOT}/lib/libprotobuf.so \
    -DProtobuf_PROTOC_LIBRARY=${PROTOBUF_ROOT}/lib/libprotoc.so \
    -DgRPC_SSL_PROVIDER=module \
    -DgRPC_ZLIB_PROVIDER=package \
    -DZLIB_ROOT=${ZLIB_ROOT} \
    -DCMAKE_INSTALL_PREFIX=%{i} \
    -DCMAKE_PREFIX_PATH="${LIBUNWIND_ROOT};${PROTOBUF_ROOT};${ZLIB_ROOT}"

ninja -v %{makeprocesses} -l $(getconf _NPROCESSORS_ONLN)

%install
cd ../build
ninja install
