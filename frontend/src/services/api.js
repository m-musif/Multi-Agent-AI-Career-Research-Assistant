const API_BASE_URL = "http://127.0.0.1:8000";

export async function sendMessage(message) {
  const response = await fetch(`${API_BASE_URL}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    throw new Error("Failed to send message");
  }

  return response.json();
}

export async function getMemory() {
  const response = await fetch(`${API_BASE_URL}/memory`);

  if (!response.ok) {
    throw new Error("Failed to load memory");
  }

  return response.json();
}
