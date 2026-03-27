@echo off
echo 🌸 Starting OntoMiko development environment...

echo 📦 Starting backend...
start "OntoMiko Backend" cmd /k "cd backend && python -m venv venv 2>nul && venv\Scripts\activate && pip install -r requirements.txt -q && uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"

timeout /t 2 /nobreak >nul

echo 🎨 Starting frontend...
start "OntoMiko Frontend" cmd /k "cd frontend && npm install && npm run dev"

echo.
echo 🚀 OntoMiko is running!
echo    Backend: http://127.0.0.1:8000
echo    Frontend: http://localhost:3000
echo.
echo Both services are running in separate windows.
echo Close the windows to stop the services.
