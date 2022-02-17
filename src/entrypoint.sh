#!/bin/bash

export AGENT_HELPER_VERSION=$(pip show asistagenthelper-pkg-rcarff-ihmc | grep Version | sed 's/Version: //')

until python3 $AGENT_MAIN_RUN_FILE; do
    echo "Agent $AGENT_MAIN_RUN_FILE crashed with exit code $?. Restarting.." >&2
    sleep 1
done