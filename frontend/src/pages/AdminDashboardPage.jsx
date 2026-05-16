import { useEffect, useState } from "react";
import { getDashboardMetrics } from "../api/adminApi.js";

export default function AdminDashboardPage() {
  const [metrics, setMetrics] = useState(null);

  useEffect(() => {
    getDashboardMetrics()
      .then(setMetrics)
      .catch(() => setMetrics(null));
  }, []);

  return (
    <section className="panel">
      <div className="panel-header">
        <h2>Admin Dashboard</h2>
      </div>

      <div className="metrics">
        <Metric label="Conversations" value={metrics?.total_conversations ?? "—"} />
        <Metric label="Messages" value={metrics?.total_messages ?? "—"} />
        <Metric label="Open Tickets" value={metrics?.open_tickets ?? "—"} />
        <Metric label="Resolved Tickets" value={metrics?.resolved_tickets ?? "—"} />
      </div>
    </section>
  );
}

function Metric({ label, value }) {
  return (
    <div className="metric">
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}
