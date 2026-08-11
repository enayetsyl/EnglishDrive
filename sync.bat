@echo off
setlocal
title English Drive - Sync
cd /d "%~dp0"

set "STAMP=%DATE% %TIME%"
set "CONFLICTS=0"

echo.
echo ==================================================
echo    ENGLISH DRIVE  -  SYNC WITH GITHUB
echo ==================================================
echo.
echo  This gets everyone's latest work, saves yours,
echo  and sends it to GitHub. Just wait for DONE.
echo.

REM ---------- Check 1: is Git installed ----------
where git >nul 2>&1
if errorlevel 1 (
  echo  [X] STOP - Git is not installed on this computer.
  echo.
  echo      Send a photo of this window to the Principal.
  echo.
  pause
  exit /b 1
)

REM ---------- Check 2: are we in the right folder ----------
if not exist ".git" (
  echo  [X] STOP - this is not the English Drive folder.
  echo.
  echo      sync.bat must stay inside E:\EnglishDrive.
  echo      Send a photo of this window to the Principal.
  echo.
  pause
  exit /b 1
)

REM ---------- Check 3: who is saving ----------
git config user.name >nul 2>&1
if errorlevel 1 git config user.name "SCD"
git config user.email >nul 2>&1
if errorlevel 1 git config user.email "almajhudbd@gmail.com"

REM ---------- Check 4: clear a leftover lock (only if Git is idle) ----------
tasklist /fi "imagename eq git.exe" 2>nul | find /i "git.exe" >nul
if errorlevel 1 (
  if exist ".git\index.lock" (
    echo  [!] Clearing a leftover lock file...
    ren ".git\index.lock" "index.lock.stale" >nul 2>&1
  )
)

REM ---------- Step 1: pull ----------
echo  [1 of 3] Getting the latest work from GitHub...
echo.
git pull --no-rebase
if errorlevel 1 (
  echo.
  echo  [X] STOP - could not get the latest work.
  echo.
  echo      Do NOT keep working in this folder.
  echo      Send a photo of this window to the Principal.
  echo.
  pause
  exit /b 1
)

REM ---------- Step 1b: conflict guard ----------
for /f %%c in ('git ls-files -u 2^>nul ^| find /c /v ""') do set "CONFLICTS=%%c"
if not "%CONFLICTS%"=="0" (
  echo.
  echo  [X] STOP - two people changed the same file.
  echo.
  echo      Nothing has been sent. Do NOT keep working.
  echo      Send a photo of this window to the Principal.
  echo.
  pause
  exit /b 1
)

REM ---------- Step 2: save ----------
echo.
echo  [2 of 3] Saving your changes...
echo.
git add -A
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "sync: %STAMP%"
) else (
  echo  Nothing new to save on this computer.
)

REM ---------- Step 3: push ----------
echo.
echo  [3 of 3] Sending to GitHub...
echo.
git push
if errorlevel 1 (
  echo.
  echo  [X] STOP - could not send to GitHub.
  echo.
  echo      Your work IS saved on this computer - nothing is lost.
  echo      Check the internet connection and run sync again.
  echo      If it fails twice, send a photo of this window
  echo      to the Principal - the access token may have expired.
  echo.
  echo %STAMP%  PUSH FAILED>> "sync-log.txt"
  pause
  exit /b 1
)

echo %STAMP%  OK>> "sync-log.txt"
echo.
echo ==================================================
echo    DONE - everything is safely on GitHub.
echo ==================================================
echo.
echo  You can close this window.
echo.
pause
exit /b 0
