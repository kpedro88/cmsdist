### RPM external rapidjson-toolfile 1.0
Requires: rapidjson
%prep

%build

%install

mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/rapidjson.xml
<tool name="rapidjson" version="@TOOL_VERSION@">
  <lib name="rapidjson"/>
  <client>
    <environment name="RAPIDJSON_BASE" default="@TOOL_ROOT@"/>
    <environment name="INCLUDE" default="$PROTOBUF_BASE/include"/>
    <environment name="LIBDIR" default="$PROTOBUF_BASE/lib"/>
  </client>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post
