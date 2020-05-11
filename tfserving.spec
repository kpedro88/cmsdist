### RPM external tfserving 2.1.0

Source: git+https://github.com/hls-fpga-machine-learning/inception_cmake?obj=%{realversion}&submodules=1&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz

BuildRequires: cmake
Requires: protobuf grpc tensorflow eigen

%prep

%setup -q -n %{n}-%{realversion}

%build

rm -rf ../build
mkdir ../build
cd ../build

cmake ../%{n}-%{realversion} \
    -DPROTOBUF_LIBRARY=$PROTOBUF_ROOT/lib/libprotobuf.so \
    -DPROTOBUF_INCLUDE_DIR=$PROTOBUF_ROOT/include \
    -DGRPC_LIBRARY=$GRPC_ROOT/lib/libgrpc.so \
    -DGRPC_GRPC++_LIBRARY=$GRPC_ROOT/lib/libgrpc++.so \
    -DGRPC_INCLUDE_DIR=$GRPC_ROOT/include \
    -DGRPC_GRPC++_REFLECTION_LIBRARY=$GRPC_ROOT/lib/libgrpc++_reflection.so \
    -DGRPC_CPP_PLUGIN=$GRPC_ROOT/bin/grpc_cpp_plugin \
    -DTENSORFLOW_CC_LIBRARY=$TENSORFLOW_ROOT/lib/libtensorflow_cc.so \
    -DTENSORFLOW_INCLUDE_DIR=$TENSORFLOW_ROOT/include \
    -DEIGEN_INCLUDE_DIR=$TENSORFLOW_ROOT/include/third_party/eigen3 \
    -DTENSORFLOW_FWK_LIBRARY=$TENSORFLOW_ROOT/lib/libtensorflow_framework.so

make %{makeprocesses}

%install

cd ../build

mkdir %{i}/lib
cp libtfserving.so %{i}/lib
mkdir %{i}/include
cp -r proto-src/tensorflow_serving %{i}/include

