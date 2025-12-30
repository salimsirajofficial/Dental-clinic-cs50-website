@echo off
echo Starting BrightSmile Dental Clinic Website...
echo.
echo Installing/Updating dependencies...
venv\Scripts\python.exe -m pip install -r requirements.txt --quiet
echo.
echo Starting Flask server...
echo.
echo ========================================
echo   Server running at: http://localhost:5000
echo   Admin Login: http://localhost:5000/login
echo   Press Ctrl+C to stop the server
echo ========================================
echo.
venv\Scripts\python.exe app.py
pause

