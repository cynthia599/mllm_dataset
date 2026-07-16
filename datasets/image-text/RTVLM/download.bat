@echo off
set OUTPUT=RTVLM-data

hf download MMInstruction/RedTeamingVLM ^
  --repo-type dataset ^
  --local-dir "%OUTPUT%"

echo.
echo RTVLM download completed.
pause