### RPM external triton-inference-server 2.2.0
%define branch master
%define github_user triton-inference-server

Source: git+https://github.com/%{github_user}/server.git?obj=%{branch}/v%{realversion}&export=%{n}-%{realversion}&output=/%{n}-%{realversion}.tgz
BuildRequires: cmake
Requires: openssl opencv protobuf grpc curl python py2-wheel py2-setuptools py2-grpcio-tools rapidjson

%prep

%setup -n %{n}-%{realversion}

%build

# remove config required in cmake (a future triton version will support cmake flag TRITON_CURL_WITHOUT_CONFIG for this)
sed -i 's/find_package(CURL CONFIG REQUIRED)/find_package(CURL REQUIRED)/' ../%{n}-%{realversion}/src/clients/c++/library/CMakeLists.txt
# pick up rapidjson headers
#sed -i '/  # libhttpclient_static.a/i \ \ target_include_directories(http-client-library PUBLIC ${RapidJSON_INCLUDE_DIRS})\n' ../%{n}-%{realversion}/src/clients/c++/library/CMakeLists.txt
sed -i '/  # libhttpclient_static.a/i \ \ target_link_libraries(http-client-library rapidjson)\n' ../%{n}-%{realversion}/src/clients/c++/library/CMakeLists.txt
#change flag due to bug in gcc10 https://gcc.gnu.org/bugzilla/show_bug.cgi?id=95148
if [[ `gcc --version | head -1 | cut -d' ' -f3 | cut -d. -f1,2,3 | tr -d .` -gt 1000 ]] ; then 
    sed -i -e "s|Werror|Wtype-limits|g" ../%{n}-%{realversion}/build/client/CMakeLists.txt
fi

rm -rf ../build
mkdir ../build
cd ../build

cmake ../%{n}-%{realversion}/build/client \
    -DCMAKE_INSTALL_PREFIX="%{i}" \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_BUILD_TYPE=Release \
    -DTRITON_ENABLE_GPU=OFF \
    -DTRITON_CLIENT_SKIP_EXAMPLES=ON \
    -DRapidJSON_DIR=${RAPIDJSON_ROOT}/lib/cmake/RapidJSON \
    -DCURL_LIBRARY=${CURL_ROOT}/lib/libcurl.so \
    -DCURL_INCLUDE_DIR=${CURL_ROOT}/include \
    -DTRITON_ENABLE_HTTP=ON \
    -DTRITON_ENABLE_GRPC=ON \
    -DTRITON_VERSION=%{realversion} \
    -DZLIB_ROOT=${ZLIB_ROOT} \
    -DOPENSSL_ROOT_DIR=${OPENSSL_ROOT} \
    -DCMAKE_CXX_FLAGS="-Wno-error" \
    -DCMAKE_PREFIX_PATH="${ZLIB_ROOT}"

make VERBOSE=1 %{makeprocesses}

%install
cd ../build
make install

