#!/bin/bash
set -e

echo "🌸 Starting OntoMiko development environment..."

# Function to cleanup background processes
cleanup() {
    echo ""
    echo "🛑 Stopping services..."
    if [ -n "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null || true
    fi
    if [ -n "$FRONTEND_PID" ]; then
        kill $FRONTEND_PID 2>/dev/null || true
    fi
    exit 0
}

# Trap SIGINT and SIGTERM
trap cleanup SIGINT SIGTERM

# Start backend
echo "📦 Starting backend..."
cd backend
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt -q
echo "✅ Backend starting at http://127.0.0.1:8000"
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000 &
BACKEND_PID=$!

# Wait a bit for backend to start
sleep 2

# Start frontend
echo "🎨 Starting frontend..."
cd ../frontend
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi
echo "✅ Frontend starting at http://localhost:3000"
npm run dev &
FRONTEND_PID=$!

echo ""
echo "🚀 OntoMiko is running!"
echo "   Backend: http://127.0.0.1:8000"
echo "   Frontend: http://localhost:3000"
echo ""
echo "Press Ctrl+C to stop both services"

# Wait for any process to exit
wait
