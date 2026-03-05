@echo off
chcp 65001 > nul
title Macro Player - Setup

echo ==================================================
echo    MACRO PLAYER - CAI DAT TU DONG
echo ==================================================
echo.

REM === KIEM TRA PYTHON ===
python --version > nul 2>&1
if %errorlevel% == 0 (
    echo [OK] Da tim thay Python:
    python --version
    goto :InstallDeps
)

REM === PYTHON CHUA CO - TU DONG CAI ===
echo [!] Khong tim thay Python. Dang tai Python 3.12...
echo.

set PYTHON_URL=https://www.python.org/ftp/python/3.12.9/python-3.12.9-amd64.exe
set PYTHON_INSTALLER=%TEMP%\python_installer.exe

REM Tai Python
powershell -Command "& { Write-Host 'Dang tai Python...'; Invoke-WebRequest -Uri '%PYTHON_URL%' -OutFile '%PYTHON_INSTALLER%' -UseBasicParsing; Write-Host 'Tai xong!' }"

if not exist "%PYTHON_INSTALLER%" (
    echo [LOI] Khong the tai Python. Vui long kiem tra ket noi mang.
    pause
    exit /b 1
)

echo [OK] Da tai xong. Dang cai Python (vui long doi)...
"%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1

REM Xoa file cai dat tam
del "%PYTHON_INSTALLER%" > nul 2>&1

REM Xac nhan lai
python --version > nul 2>&1
if %errorlevel% NEQ 0 (
    echo [LOI] Cai Python that bai! Vui long cai thu cong: https://www.python.org
    pause
    exit /b 1
)
echo [OK] Da cai Python thanh cong!

:InstallDeps
echo.
echo [*] Dang kiem tra/cai thu vien (pynput)...

pip install -r requirements.txt --quiet
if %errorlevel% NEQ 0 (
    echo [LOI] Khong the cai pynput!
    pause
    exit /b 1
)

echo [OK] Da cai xong tat ca thu vien!
echo.
echo ==================================================
echo    CAI DAT HOAN TAT! Dang khoi dong...
echo ==================================================
echo.

REM === CHAY APP ===
start "" wscript.exe "%~dp0start.vbs"
exit /b 0
