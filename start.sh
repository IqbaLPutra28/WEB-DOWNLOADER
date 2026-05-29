#!/bin/bash

# Video Downloader - Unix/Mac Startup Script

echo "========================================"
echo "  Video Downloader - Startup Script"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Install Python from https://www.python.org"
    exit 1
fi

echo "[1/4] Checking Python installation..."
python3 --version
echo ""

echo "[2/4] Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo ""

echo "[3/4] Starting backend server..."
echo "Backend will start at: http://localhost:8000"
echo "API Docs at: http://localhost:8000/docs"
echo ""

cd backend
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
