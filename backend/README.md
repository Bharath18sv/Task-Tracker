# Task Tracker Backend

This is the backend API for the Task Tracker application built with FastAPI.

## Setup

1. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Run the server:
   ```
   python main.py
   ```

The API will be available at http://localhost:8000

## API Endpoints

- `POST /api/tasks` - Create a new task
- `GET /api/tasks` - List all tasks (with optional filtering by status/priority and sorting)
- `PATCH /api/tasks/{id}` - Update a task's status or priority
- `GET /api/insights` - Get task analytics and insights
