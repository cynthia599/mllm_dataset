#!/usr/bin/env bash
set -e

OUTPUT="./JailBreakV-28K-data"

hf download JailbreakV-28K/JailBreakV-28k \
  --repo-type dataset \
  --include "JailBreakV_28K/**" \
  --local-dir "$OUTPUT"

echo "JailBreakV-28K download completed."