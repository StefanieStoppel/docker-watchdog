#!/bin/bash

HOST_MOUNT_DIR=$1

docker run -v "$HOST_MOUNT_DIR":/app/data -it docker-watchdog-2:latest