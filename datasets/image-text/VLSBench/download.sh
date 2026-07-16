#!/usr/bin/env bash
set -e

OUTPUT="./VLSBench-data"

hf download Foreshhh/vlsbench \
  --repo-type dataset \
  --include "data.json" \
  --include "imgs.tar" \
  --include "README.md" \
  --local-dir "$OUTPUT"

tar -xf "$OUTPUT/imgs.tar" -C "$OUTPUT"

echo "VLSBench download and extraction completed."