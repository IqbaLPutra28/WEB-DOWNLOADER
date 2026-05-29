@echo off
REM Video Downloader - Windows Startup Script

echo ========================================
echo   Video Downloader - Startup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Checking Python installation...
python --version
echo.

echo [2/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo [3/4] Starting backend server...
echo Backend will start at: http://localhost:8000
echo API Docs at: http://localhost:8000/docs
echo.

cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

pause
