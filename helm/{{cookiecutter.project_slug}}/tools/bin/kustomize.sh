#!/bin/bash
#
# Post rendered script to kustomize the chart.
#
# Usage: helm template -g . --post-renderer tools/bin/kustomize.sh
#

cat <&0 > all.yaml

SCRIPT_DIR=$(dirname "$0")
ROOT_DIR=$(realpath "$SCRIPT_DIR/../..")

kustomize build "$ROOT_DIR" && rm all.yaml
