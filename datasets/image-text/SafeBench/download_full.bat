@echo off
set OUTPUT=SafeBench-full

hf download Zonghao2025/safebench ^
  --repo-type dataset ^
  --include "part_*" ^
  --include "category.csv" ^
  --include "sample.csv" ^
  --include "README.md" ^
  --local-dir "%OUTPUT%"

cd /d "%OUTPUT%"

echo.
echo Combining split files...

copy /b part_aa+part_ab+part_ac+part_ad+part_ae+part_af+part_ag+part_ah+part_ai+part_aj safebench.tar.gz

echo.
echo Extracting full SafeBench...

tar -xzf safebench.tar.gz

echo.
echo Full SafeBench extraction completed.
pause