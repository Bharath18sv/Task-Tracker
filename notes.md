# Notes

## Database Schema Decisions

1. **Task Model Design**:

   - Used SQLite for simplicity and ease of setup
   - Created indexes on priority and status fields for faster filtering
   - Used DateTime for due_date to enable sorting and date-based queries
   - Added created_at timestamp for audit purposes

2. **Enum Usage**:
   - Used database-level enums for priority and status to ensure data consistency
   - Defined separate enums in both models and schemas to maintain clear separation between database and API layers

## Insights Summary Computation

The `/insights` endpoint computes the following metrics:

1. **Total Tasks**: Simple count of all tasks in the database
2. **High Priority Tasks**: Count of tasks with priority set to "High"
3. **Due Soon Tasks**: Count of tasks with due dates within the next 3 days
4. **Busiest Day**: Day with the highest number of tasks due (computed by grouping tasks by due date)
5. **Summary Text**: Rule-based natural language summary combining the above metrics

The summary generation follows these rules:

- Start with total task count
- Mention high priority task count if > 0
- Mention due soon count if > 0
- End with a period

## Possible Improvements

1. **Authentication**:

   - Add JWT-based user authentication and registration/login endpoints
   - Associate tasks with specific users
   - Add user-specific insights

2. **Pagination**:

   - Implement pagination for the `/tasks` endpoint to handle large datasets
   - Add limit and offset parameters
   - Return pagination metadata in responses

3. **Data Visualization**:

   - Add charts using Chart.js or Recharts to visualize task distribution
   - Show priority distribution in a pie chart
   - Display task completion trends over time

4. **Advanced Features**:

   - Add task categories/tags
   - Implement task dependencies
   - Add recurring tasks
   - Add task comments/notes

5. **Performance Optimizations**:

   - Add database query caching
   - Implement database connection pooling
   - Add API response caching for insights

6. **UI/UX Improvements**:
   - Add dark mode support
   - Implement drag-and-drop task reordering
   - Add keyboard shortcuts
   - Improve mobile responsiveness
