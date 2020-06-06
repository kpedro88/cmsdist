### RPM external pytorch 1.5.0
%define branch master
%define github_user pytorch

Source: git+https://github.com/%{github_user}/pytorch.git?obj=%{branch}/v%{realversion}&export=%{n}-%{realversion}&submodules=1&output=/%{n}-%{realversion}.tgz
BuildRequires: cmake ninja
Requires: OpenBLAS tbb python python3 py2-setuptools opencv py3-numpy py2-PyYAML py2-cffi py2-typing protobuf py2-pybind11 onnxruntime

%prep

%setup -n %{n}-%{realversion}

%build

OPENSSLROOT=""
if [[ ! -z "$OPENSSL_ROOT" ]]; then OPENSSLROOT=";${OPENSSL_ROOT}" ; fi

cd ../%{n}-%{realversion}
MAX_JOBS=%compiling_processes \
USE_CUDA=0 \
USE_CUDNN=0 \
USE_FBGEMM=0 \
USE_NUMA=0 \
BUILD_TEST=0 \
USE_MKLDNN=0 \
USE_DISTRIBUTED=0 \
USE_OPENCV=1 \
USE_OPENMP=0 \
USE_NCCL=0 \
BLAS=OpenBLAS \
OpenBLAS_HOME=${OPENBLAS_ROOT} \
USE_ZSTD=1 \
USE_TBB=1 \
ATEN_THREADING=TBB \
BUILD_CUSTOM_PROTOBUF=OFF \
BUILD_CAFFE2_OPS=0 \
pybind11_INCLUDE_DIR=${PY2_PYBIND11_ROOT}/include/python2.7 \
CMAKE_PREFIX_PATH="${ZLIB_ROOT};${PY2_PYBIND11_ROOT}${OPENSSLROOT}" \
python setup.py install

%install

# installs in "torch" folder by default
for product in lib64 lib bin include share version.py; do
  mv ../%{n}-%{realversion}/torch/$product %{i}/
done

