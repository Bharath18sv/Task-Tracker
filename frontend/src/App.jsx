import React from "react";
import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";
import InsightsPanel from "./components/InsightsPanel";

function App() {
  return (
    <div className="min-h-screen bg-gray-50 p-4">
      <div className="max-w-6xl mx-auto">
        <header className="mb-6 text-center">
          <h1 className="text-2xl font-semibold text-gray-800">Task Tracker</h1>
          <p className="text-gray-600 text-sm mt-1">
            Manage your tasks efficiently
          </p>
        </header>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-5">
          {/* Left column - Task Form */}
          <div className="lg:col-span-1">
            <TaskForm />
          </div>

          {/* Right column - Task List and Insights */}
          <div className="lg:col-span-2 space-y-5">
            <InsightsPanel />
            <TaskList />
          </div>
        </div>

        <footer className="mt-8 text-center text-gray-500 text-xs">
          <p>Task Tracker © {new Date().getFullYear()}</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
