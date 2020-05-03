### RPM external tensorflow-serving 2.1.0

Source: git+https://github.com/tensorflow/serving.git?obj=master/%{realversion}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz

BuildRequires: bazel java-env autotools swig
Requires: protobuf grpc tensorflow eigen python py2-numpy py2-future py2-six python3 py3-numpy

%prep

%setup -q -n %{n}-%{realversion}

%build

%define python_cmd python
export PYTHON_BIN_PATH="$(which %{python_cmd})"

# clear the build dir
ls
rm -rf ../build

ldd `which swig`

# define bazel options
BAZEL_OPTS="--batch --output_user_root ../build build -s --verbose_failures %{makeprocesses}"
BAZEL_OPTS="$BAZEL_OPTS --action_env=PYTHON_BIN_PATH=$PYTHON_BIN_PATH --action_env=PYTHONPATH=$%{python_env}"
BAZEL_OPTS="$BAZEL_OPTS --action_env=SWIG_LIB=${SWIG_LIB} --action_env=LD_LIBRARY_PATH"

bazel $BAZEL_OPTS //tensorflow_serving/...

%install

# define and create empty target directories
outdir="$PWD/out"
incdir="$outdir/include"
libdir="$outdir/lib"
rm -rf $incdir $libdir
mkdir -p $incdir $libdir

# copy targets
srcdir="$PWD/bazel-bin/tensorflow_serving"
ls $srcdir/

cp -p $srcdir/libtfserving.so* $libdir/
