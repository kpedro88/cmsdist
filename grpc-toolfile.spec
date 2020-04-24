### RPM external grpc-toolfile 1.0
requires: grpc

%prep

%build

%install
mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/grpc.xml
<tool name="grpc" version="@TOOL_VERSION@">
  <info url="https://github.com/grpc/grpc"/>
  <lib name="grpc"/>
  <lib name="grpc++"/>
  <lib name="grpc++_reflection"/>
  <lib name="absl_bad_optional_access"/>
  <lib name="absl_base"/>
  <lib name="absl_dynamic_annotations"/>
  <lib name="absl_int128"/>
  <lib name="absl_log_severity"/>
  <lib name="absl_raw_logging_internal"/>
  <lib name="absl_spinlock_wait"/>
  <lib name="absl_strings"/>
  <lib name="absl_strings_internal"/>
  <lib name="absl_throw_delegate"/>
  <lib name="cares"/>
  <lib name="ssl"/>
  <lib name="crypto"/>
  <lib name="address_sorting"/>
  <client>
    <environment name="GRPC_BASE" default="@TOOL_ROOT@"/>
    <environment name="INCLUDE" default="$GRPC_BASE/include"/>
    <environment name="LIBDIR" default="$GRPC_BASE/lib"/>
  </client>
  <use name="protobuf"/>
</tool>
EOF_TOOLFILE

## IMPORT scram-tools-post
