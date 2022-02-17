#!/bin/bash

export AGENT_HELPER_VERSION=$(pip show asistagenthelper-pkg-rcarff-ihmc | grep Version | sed 's/Version: //')
source settings.env
export AGENT_NAME=$AGENT_NAME
cd src
python3 $AGENT_MAIN_RUN_FILE