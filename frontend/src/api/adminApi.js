const API_BASE = "http://localhost:8000";

export async function getDashboardMetrics() {
  const response = await fetch(`${API_BASE}/admin/dashboard/metrics`);

  if (!response.ok) {
    throw new Error("Failed to load dashboard metrics");
  }

  return response.json();
}
