#!/usr/bin/env bash

set -e


OUTPUT="./JALMBench-data"


hf download AnonymousUser000/JALMBench \
 --repo-type dataset \
 --local-dir "$OUTPUT"


echo "JALMBench download completed."