#!/usr/bin/env bash
set -e

OUTPUT="./RTVLM-data"

hf download MMInstruction/RedTeamingVLM \
  --repo-type dataset \
  --local-dir "$OUTPUT"

echo "RTVLM download completed."