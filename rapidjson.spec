### RPM external rapidjson 1.1.1
%define branch master
%define github_user Tencent

# rapidjson has not tagged a release since 2016, so just use latest commit hash
Source: git+https://github.com/%{github_user}/rapidjson.git?obj=%{branch}/ce81bc9edfe773667a7a4454ba81dac72ed4364c&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz
BuildRequires: cmake

%prep

%setup -n %{n}-%{realversion}

%build

rm -rf ../build
mkdir ../build
cd ../build

cmake ../%{n}-%{realversion} \
    -DCMAKE_INSTALL_PREFIX="%{i}" \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_BUILD_TYPE=Release \
    -DRAPIDJSON_BUILD_DOC=OFF \
    -DRAPIDJSON_BUILD_EXAMPLES=OFF \
    -DRAPIDJSON_BUILD_TESTS=OFF \
    -DRAPIDJSON_BUILD_THIRDPARTY_GTEST=OFF \
    -DRAPIDJSON_ENABLE_INSTRUMENTATION_OPT=OFF

make %{makeprocesses}

%install

cd ../build

make install
