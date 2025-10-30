import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api";

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
  timeout: 10000, // 10 second timeout
});

// Response interceptor
api.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    if (error.response) {
      console.error("API Error:", error.response.status, error.response.data);
    } else if (error.request) {
      console.error("Network Error:", error.request);
    } else {
      console.error("Error:", error.message);
    }
    return Promise.reject(error);
  }
);

export const taskApi = {
  // Get all tasks
  getTasks: (params = {}) => api.get("/tasks", { params }),

  // Create new task
  createTask: (taskData) => api.post("/tasks", taskData),

  // Update task
  updateTask: (id, taskData) => api.patch(`/tasks/${id}`, taskData),

  // Get insights
  getInsights: () => api.get("/insights"),
};

export default api;
