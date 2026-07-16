@echo off

set OUTPUT=Video-SafetyBench-data


hf download BAAI/Video-SafetyBench ^
 --repo-type dataset ^
 --local-dir "%OUTPUT%"


echo Download completed.

pause