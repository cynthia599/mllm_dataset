@echo off
set OUTPUT=VLSBench-data

hf download Foreshhh/vlsbench ^
  --repo-type dataset ^
  --include "data.json" ^
  --include "imgs.tar" ^
  --include "README.md" ^
  --local-dir "%OUTPUT%"

echo.
echo Download completed.
echo Extracting imgs.tar...

cd /d "%OUTPUT%"
tar -xf imgs.tar

echo.
echo VLSBench extraction completed.
pause