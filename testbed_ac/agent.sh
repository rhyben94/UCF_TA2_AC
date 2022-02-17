#!/bin/bash
source ./settings.env

if [ "$1" = "up" ]; then
    echo "Bring up Agent: $AGENT_NAME"
    docker-compose --env-file settings.env up
    docker ps
elif [ "$1" = "upd" ]; then
    echo "Bring up Agent: $AGENT_NAME"
    docker-compose --env-file settings.env up -d
    docker ps
elif [ "$1" = "down" ]; then
    echo "Bring down Agent: $AGENT_NAME"
    docker-compose --env-file settings.env down --remove-orphans
    docker ps
elif [ "$1" = "build" ]; then
    echo "Updating the docker image for $AGENT_NAME"
    cp -R ../../Tools/ihmc-python-agent-helper-package ./ihmc-python-agent-helper-package
    docker build -t $DOCKER_IMAGE_NAME_LOWERCASE --build-arg CACHE_BREAKER=$(date +%s) .
    rm -rf ./ihmc-python-agent-helper-package
elif [ "$1" = "build_clean" ]; then
    echo "Rebuilding the docker image for $AGENT_NAME"
    cp -R ../../Tools/ihmc-python-agent-helper-package ./ihmc-python-agent-helper-package
    docker build --no-cache -t $DOCKER_IMAGE_NAME_LOWERCASE .
    rm -rf ./ihmc-python-agent-helper-package
elif [ "$1" = "export" ]; then
    echo "exporting the docker image for $AGENT_NAME"
    docker save -o $DOCKER_IMAGE_NAME_LOWERCASE.tar $DOCKER_IMAGE_NAME_LOWERCASE
else
    echo "Usage: ./agent.sh [up|upd|down|build|export]"
fi
