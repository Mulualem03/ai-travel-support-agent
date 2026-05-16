import { useState } from "react";
import { sendChatMessage } from "../api/chatApi.js";

const suggestions = [
  "What is the status of booking TRV-10234?",
  "Can I cancel my hotel?",
  "Can I get a refund?",
  "What is the baggage allowance?",
  "I want to speak to a human agent",
];

export default function ChatPage() {
  const [conversationId, setConversationId] = useState(null);
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([
    {
      sender: "assistant",
      text: "Hello, I am your AI travel support assistant. Ask me about bookings, cancellations, refunds, baggage, or flight changes.",
    },
  ]);
  const [loading, setLoading] = useState(false);

  async function handleSend(text = message) {
    if (!text.trim()) return;

    const userText = text.trim();
    setMessage("");
    setMessages((prev) => [...prev, { sender: "user", text: userText }]);
    setLoading(true);

    try {
      const data = await sendChatMessage({
        message: userText,
        conversationId,
        userId: 1,
      });

      setConversationId(data.conversation_id);
      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          text: `${data.response}\n\nIntent: ${data.intent} | Tools: ${data.used_tools.join(", ")} | Confidence: ${data.confidence}`,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: "assistant", text: "Sorry, something went wrong. Please try again." },
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="panel">
      <div className="panel-header">
        <h2>Customer Chat</h2>
      </div>

      <div className="messages">
        {messages.map((item, index) => (
          <div key={index} className={`message ${item.sender}`}>
            {item.text}
          </div>
        ))}
        {loading && <div className="message assistant">Thinking...</div>}
      </div>

      <div className="quick">
        {suggestions.map((item) => (
          <button key={item} onClick={() => handleSend(item)}>
            {item}
          </button>
        ))}
      </div>

      <div className="composer">
        <input
          value={message}
          placeholder="Ask a travel support question..."
          onChange={(event) => setMessage(event.target.value)}
          onKeyDown={(event) => {
            if (event.key === "Enter") handleSend();
          }}
        />
        <button onClick={() => handleSend()}>Send</button>
      </div>
    </section>
  );
}
