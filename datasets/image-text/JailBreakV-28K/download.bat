@echo off
set OUTPUT=JailBreakV-28K-data

hf download JailbreakV-28K/JailBreakV-28k ^
  --repo-type dataset ^
  --include "JailBreakV_28K/**" ^
  --local-dir "%OUTPUT%"

echo.
echo JailBreakV-28K download completed.
pause