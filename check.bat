@echo off
setlocal
title English Drive - Check (read only)
cd /d "%~dp0"

echo.
echo ==================================================
echo    ENGLISH DRIVE  -  CHECK  (reads only, changes nothing)
echo ==================================================
echo.

where git >nul 2>&1
if errorlevel 1 (
  echo  [X] Git is not installed on this computer.
  pause
  exit /b 1
)

if not exist ".git" (
  echo  [X] This is not the English Drive folder.
  pause
  exit /b 1
)

echo  Folder git is actually using:
git rev-parse --show-toplevel
echo.

echo  Branch and remote:
git rev-parse --abbrev-ref HEAD
git config --get remote.origin.url
echo.

echo  --- CHANGED BUT NOT YET SAVED (should be empty if sync worked) ---
git status --short
echo  --- end of list ---
echo.

echo  --- LAST 5 SAVES ---
git log --oneline -5
echo.

echo  --- FILES IN THE LAST SAVE ---
git log -1 --stat --oneline
echo.

echo  --- IS PD-058 IN THE SAVED COPY? ---
git grep -c "PD-058" HEAD -- governance/Curriculum_Design_Decision_Log_Working.md
echo  (a number means yes; "exit code 1" or nothing means NO)
echo.

echo ==================================================
echo    Send a photo of this whole window to the Principal.
echo ==================================================
pause
exit /b 0
