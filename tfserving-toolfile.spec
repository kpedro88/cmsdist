### RPM external tfserving-toolfile 1.0
Requires: tfserving

%prep

%build

%install
mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/tfserving.xml
<tool name="tensorflow-serving" version="2.1.0">
  <lib name="tfserving"/>
  <client>
    <environment name="TFSERVING_BASE" default="@TOOL_ROOT@"/>
    <environment name="INCLUDE" default="$TFSERVING_BASE/include"/>
    <environment name="LIBDIR" default="$TFSERVING_BASE/lib"/>
  </client>
  <use name="protobuf"/>
  <use name="grpc"/>
  <use name="eigen"/>
  <use name="tensorflow-cc"/>
  <use name="tensorflow-framework"/>
</tool>

