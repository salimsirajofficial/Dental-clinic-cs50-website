# BrightSmile Dental Clinic - Run Script
# This script bypasses PowerShell execution policy issues

Write-Host "Starting BrightSmile Dental Clinic Website..." -ForegroundColor Green
Write-Host ""

Write-Host "Installing/Updating dependencies..." -ForegroundColor Yellow
& .\venv\Scripts\python.exe -m pip install -r requirements.txt --quiet

Write-Host ""
Write-Host "Starting Flask server..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Server running at: http://localhost:5000" -ForegroundColor White
Write-Host "  Admin Login: http://localhost:5000/login" -ForegroundColor White
Write-Host "  Press Ctrl+C to stop the server" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

& .\venv\Scripts\python.exe app.py

