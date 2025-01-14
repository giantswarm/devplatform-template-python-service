# demo-album-catalog-python

![validation and test result](https://github.com/giantswarm/demo-album-catalog-python/actions/workflows/validate-test.yaml/badge.svg?event=push)

## Intro

This repo is meant as a template base for a python flask based web service projects, that are deployed to a Kubernetes cluster
using a Helm Chart. The repo follows the rule of fast local builds and developer feedback: tools configured for the CI
process are also installable on local dev machines, allowing for rapid feedback loops, without waiting for
the CI.

## Features included

- automatically build a container image and a Helm chart
  - use Cloud Native Buildpacks to build the container image
- upload build artifacts to GitHub: create a release for the binaries, upload the container image and the Helm chart
  to GitHub's OCI registry
- included security: vulnerability scans for go sources, generation of SBoM, singing artifacts with `cosign`
- included automated dependency updates based on [renovate](renovatebot.com)
- included linting and validation for multiple types of artifacts, including python, markdown, Kubernetes objects, ...
