# Task Tracker with Smart Insights

A full-stack web application for task management with smart insights, built with FastAPI (Python) for the backend and React (Vite) for the frontend.

## Features

- **Task Management**: Create, read, update, and delete tasks
- **Task Filtering**: Filter tasks by status and priority
- **Task Sorting**: Sort tasks by due date
- **Smart Insights**: Get analytics about your tasks including:
  - Total task count
  - High priority task count
  - Tasks due soon (within 3 days)
  - Busiest day (day with most tasks due)
  - Summary text with key insights
- **Responsive UI**: Clean, modern interface built with Tailwind CSS

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: React with Vite
- **Database**: SQLite with SQLAlchemy ORM
- **Styling**: Tailwind CSS
- **API Communication**: Axios

## Project Structure

```
TaskTracker-Q/
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   ├── routes/
│   │   └── tasks.py
│   ├── insights.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── TaskForm.jsx
│   │   │   ├── TaskList.jsx
│   │   │   └── InsightsPanel.jsx
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── index.css
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── README.md
├── DECLARATION.md
├── notes.md
└── README.md
```

## Setup and Installation

### Backend Setup

1. Navigate to the backend directory:

   ```
   cd backend
   ```

2. Create a virtual environment:

   ```
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Run the server:
   ```
   python main.py
   ```

The backend API will be available at http://localhost:8000

### Frontend Setup

1. Navigate to the frontend directory:

   ```
   cd frontend
   ```

2. Install dependencies:

   ```
   npm install
   ```

3. Run the development server:
   ```
   npm run dev
   ```

The frontend will be available at http://localhost:5173

## API Endpoints

- `POST /api/tasks` - Create a new task
- `GET /api/tasks` - List all tasks (with optional filtering by status/priority and sorting)
- `PATCH /api/tasks/{id}` - Update a task's status or priority
- `GET /api/insights` - Get task analytics and insights

## Development

### Backend Development

The backend is built with FastAPI, which provides automatic API documentation at:

- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

### Frontend Development

The frontend is built with React and Vite. Key components include:

- **TaskForm**: For creating new tasks
- **TaskList**: For viewing and managing tasks
- **InsightsPanel**: For displaying task analytics

## Database Schema

The application uses SQLite with the following task model:

```
Task:
- id (Integer, Primary Key)
- title (String, required)
- description (Text)
- priority (Enum: Low, Medium, High)
- status (Enum: Todo, In Progress, Done)
- due_date (DateTime)
- created_at (DateTime, default func.now())
```

Indexes are created on priority and status fields for improved query performance.

## Notes

For additional information about database schema decisions, insights computation logic, and possible improvements, see [notes.md](notes.md).
