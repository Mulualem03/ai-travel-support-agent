const API_BASE = "http://localhost:8000";

export async function sendChatMessage({ message, conversationId, userId = 1 }) {
  const response = await fetch(`${API_BASE}/chat/message`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
      conversation_id: conversationId,
      user_id: userId,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to send message");
  }

  return response.json();
}
