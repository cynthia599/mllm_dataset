@echo off

set OUTPUT=JALMBench-data


hf download AnonymousUser000/JALMBench ^
 --repo-type dataset ^
 --local-dir "%OUTPUT%"


echo.
echo JALMBench download completed.

pause