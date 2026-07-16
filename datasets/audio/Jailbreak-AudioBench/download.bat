@echo off

set OUTPUT=Jailbreak-AudioBench-data


hf download researchtopic/Jailbreak-AudioBench ^
 --repo-type dataset ^
 --local-dir "%OUTPUT%"


echo.
echo Jailbreak-AudioBench download completed.

pause