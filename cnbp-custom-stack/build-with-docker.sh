#!/bin/bash -e

VER=0.0.1
NAME="python-mysql-jammy"
BUILDER_NAME="$NAME-builder"
RUNNER_NAME="$NAME-runner"

docker build --file build.Dockerfile . -t "$BUILDER_NAME:$VER"
docker build --file run.Dockerfile . -t "$RUNNER_NAME:$VER"

sed -i "s/build-image = .*/build-image = \"$BUILDER_NAME:$VER\"/" builder.toml
sed -i "s/run-image = .*/run-image = \"$RUNNER_NAME:$VER\"/" builder.toml

pack builder create "$NAME:$VER" --config builder.toml
