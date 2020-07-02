#!/bin/bash

DEFAULT_DIR="$HOME/Desktop/test"
HOST_MOUNT_DIR=${1:-$DEFAULT_DIR}
CONTAINER_MOUNT_DIR=/app/data

docker run --name docker-watchdog-1 -e "INPUT_DIR=$CONTAINER_MOUNT_DIR" -v "$HOST_MOUNT_DIR":"$CONTAINER_MOUNT_DIR" -it docker-watchdog-1:latest