@echo off
set OUTPUT=VLGuard-data

echo Please make sure you have logged in to Hugging Face.
echo Run: hf auth login
echo.

hf download ys-zong/VLGuard ^
  --repo-type dataset ^
  --local-dir "%OUTPUT%"

echo.
echo VLGuard download completed.
pause