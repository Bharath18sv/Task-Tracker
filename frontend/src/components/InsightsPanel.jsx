import React, { useState, useEffect } from "react";
import { taskApi } from "../api";

const InsightsPanel = () => {
  const [insights, setInsights] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchInsights = async () => {
    try {
      setLoading(true);
      const response = await taskApi.getInsights();
      setInsights(response.data);
    } catch (err) {
      setError("Failed to fetch insights");
      console.error("Error fetching insights:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchInsights();

    // Refresh insights every minute
    const interval = setInterval(fetchInsights, 60000);

    return () => clearInterval(interval);
  }, []);

  if (loading)
    return (
      <div className="bg-white rounded-lg border border-gray-200 p-5">
        <h2>Loading...</h2>
      </div>
    );

  if (error) return <div className="text-red-600 text-sm">{error}</div>;

  return (
    <div className="bg-white rounded-lg border border-gray-200 p-5">
      <h2 className="text-lg font-medium text-gray-800 mb-3">Smart Insights</h2>

      {insights && (
        <div className="space-y-4">
          <div className="p-3 bg-blue-50 rounded border border-blue-100">
            <p className="text-gray-700 text-sm">{insights?.summary}</p>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            <div className="bg-gray-50 p-3 rounded border border-gray-100 text-center">
              <div className="text-lg font-medium text-gray-800">
                {insights?.total_tasks}
              </div>
              <div className="text-xs text-gray-600">Total Tasks</div>
            </div>

            <div className="bg-gray-50 p-3 rounded border border-gray-100 text-center">
              <div className="text-lg font-medium text-red-600">
                {insights?.high_priority}
              </div>
              <div className="text-xs text-gray-600">High Priority</div>
            </div>

            <div className="bg-gray-50 p-3 rounded border border-gray-100 text-center">
              <div className="text-lg font-medium text-yellow-600">
                {insights?.due_soon}
              </div>
              <div className="text-xs text-gray-600">Due Soon</div>
            </div>

            <div className="bg-gray-50 p-3 rounded border border-gray-100 text-center">
              <div className="text-lg font-medium text-green-600">
                {insights?.busiest_day
                  ? new Date(insights?.busiest_day).toLocaleDateString()
                  : "N/A"}
              </div>
              <div className="text-xs text-gray-600">Busiest Day</div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default InsightsPanel;
