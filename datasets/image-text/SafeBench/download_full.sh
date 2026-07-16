#!/usr/bin/env bash
set -e

OUTPUT="./SafeBench-full"

hf download Zonghao2025/safebench \
  --repo-type dataset \
  --include "part_*" \
  --include "category.csv" \
  --include "sample.csv" \
  --include "README.md" \
  --local-dir "$OUTPUT"

cat "$OUTPUT"/part_* > "$OUTPUT/safebench.tar.gz"

tar -xzf "$OUTPUT/safebench.tar.gz" -C "$OUTPUT"

echo "Full SafeBench download and extraction completed."