@echo off
set OUTPUT=SafeBench-data

hf download Zonghao2025/safebench ^
  --repo-type dataset ^
  --include "minibench.tar.gz" ^
  --include "category.csv" ^
  --include "sample.csv" ^
  --include "README.md" ^
  --local-dir "%OUTPUT%"

echo.
echo Download completed.
echo Extracting MiniBench...

cd /d "%OUTPUT%"
tar -xzf minibench.tar.gz

echo.
echo MiniBench extraction completed.
pause