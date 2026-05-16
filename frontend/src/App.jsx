import ChatPage from "./pages/ChatPage.jsx";
import AdminDashboardPage from "./pages/AdminDashboardPage.jsx";

export default function App() {
  return (
    <div className="app">
      <header className="topbar">
        <div>
          <h1>AI Travel Support Agent</h1>
          <p>RAG, tool calling, booking lookup, and human escalation</p>
        </div>
      </header>

      <main className="layout">
        <ChatPage />
        <AdminDashboardPage />
      </main>
    </div>
  );
}
