#!/usr/bin/env bash
set -e

OUTPUT="./SafeBench-data"

hf download Zonghao2025/safebench \
  --repo-type dataset \
  --include "minibench.tar.gz" \
  --include "category.csv" \
  --include "sample.csv" \
  --include "README.md" \
  --local-dir "$OUTPUT"

tar -xzf "$OUTPUT/minibench.tar.gz" -C "$OUTPUT"

echo "SafeBench MiniBench download and extraction completed."