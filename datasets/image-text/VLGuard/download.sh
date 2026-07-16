#!/usr/bin/env bash
set -e

OUTPUT="./VLGuard-data"

echo "Please make sure you have logged in to Hugging Face:"
echo "hf auth login"

hf download ys-zong/VLGuard \
  --repo-type dataset \
  --local-dir "$OUTPUT"

echo "VLGuard download completed."