#!/usr/bin/env bash

set -e


OUTPUT="./Jailbreak-AudioBench-data"


hf download researchtopic/Jailbreak-AudioBench \
 --repo-type dataset \
 --local-dir "$OUTPUT"


echo "Download completed."