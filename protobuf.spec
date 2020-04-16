### RPM external protobuf 3.8.0
## INITENV SETV PROTOBUF_SOURCE %{source0}
## INITENV SETV PROTOBUF_STRIP_PREFIX %{source_prefix}
#============= IMPORTANT NOTE ========================#
# When changing the version of protobuf, remember to regenerate protobuf objects in CMSSW
# current recipe for this is:
# cmsenv
# git cms-addpkg DQMServices/Core
# cd $CMSSW_BASE/src
# protoc --cpp_out=. DQMServices/Core/src/ROOTFilePB.proto
#######################################################

#These are needed by Tensorflow sources
#NOTE: Never apply any patch in the spec file, this way tensorflow gets the exact same sources
%define source0 https://github.com/google/protobuf/archive/v%{realversion}.tar.gz
%define source_prefix %{n}-%{realversion}

Source: %{source0}
Requires: zlib
BuildRequires: cmake

%prep
%setup -n %{source_prefix}

%build
cd cmake
rm -rf build
mkdir build
cd build
pwd

cmake ../ \
  -DCMAKE_BUILD_TYPE=Release \
  -DZLIB_ROOT=${ZLIB_ROOT} \
  -DBUILD_SHARED_LIBS=ON \
  -Dprotobuf_BUILD_TESTS=OFF \
  -DCMAKE_INSTALL_PREFIX=%{i}

make %{makeprocesses}

%install
make install
