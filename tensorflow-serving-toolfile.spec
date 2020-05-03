### RPM external tensorflow-serving-toolfile 1.0
Requires: tensorflow-serving

%prep

%build

%install
mkdir -p %i/etc/scram.d
cat << \EOF_TOOLFILE >%i/etc/scram.d/tensorflow-serving.xml
<tool name="tensorflow-serving" version="2.1.0">
  <info url="https://github.com/tensorflow/serving"/>
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

