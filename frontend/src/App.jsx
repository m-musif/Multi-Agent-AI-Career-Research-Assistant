import { useState } from "react";
import { sendMessage, getMemory } from "./services/api";

function App() {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [memory, setMemory] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSend() {
    if (!message.trim()) return;

    const userMessage = message;
    setMessage("");
    setLoading(true);

    try {
      const data = await sendMessage(userMessage);

      setChatHistory((prev) => [
        ...prev,
        {
          user: userMessage,
          assistant: data.response,
          agent: data.agent,
        },
      ]);
    } catch (error) {
      alert("Error sending message");
    } finally {
      setLoading(false);
    }
  }

  async function handleLoadMemory() {
    const data = await getMemory();
    setMemory(data);
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <div className="max-w-6xl mx-auto p-6">
        <h1 className="text-3xl font-bold mb-2">
          Multi-Agent AI Career & Research Assistant
        </h1>

        <p className="text-slate-400 mb-6">
          Career Agent • Research Agent • Personal Agent • Reviewer Agent
        </p>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2 bg-slate-900 rounded-xl p-5 border border-slate-800">
            <h2 className="text-xl font-semibold mb-4">Chat</h2>

            <div className="h-[420px] overflow-y-auto space-y-4 mb-4">
              {chatHistory.length === 0 && (
                <p className="text-slate-500">
                  Ask about internships, resume, LinkedIn, research, or your goals.
                </p>
              )}

              {chatHistory.map((chat, index) => (
                <div key={index} className="space-y-2">
                  <div className="bg-blue-600 p-3 rounded-lg">
                    <p className="text-sm font-semibold">You</p>
                    <p>{chat.user}</p>
                  </div>

                  <div className="bg-slate-800 p-3 rounded-lg">
                    <div className="flex justify-between mb-2">
                      <p className="text-sm font-semibold">Assistant</p>
                      <span className="text-xs bg-emerald-600 px-2 py-1 rounded-full">
                        {chat.agent}
                      </span>
                    </div>
                    <p className="whitespace-pre-wrap text-slate-200">
                      {chat.assistant}
                    </p>
                  </div>
                </div>
              ))}
            </div>

            <div className="flex gap-2">
              <input
                className="flex-1 bg-slate-800 border border-slate-700 rounded-lg px-4 py-3 outline-none"
                placeholder="Ask your multi-agent assistant..."
                value={message}
                onChange={(e) => setMessage(e.target.value)}
              />

              <button
                onClick={handleSend}
                disabled={loading}
                className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg font-semibold disabled:opacity-50"
              >
                {loading ? "Thinking..." : "Send"}
              </button>
            </div>
          </div>

          <div className="bg-slate-900 rounded-xl p-5 border border-slate-800">
            <h2 className="text-xl font-semibold mb-4">Memory</h2>

            <button
              onClick={handleLoadMemory}
              className="w-full bg-emerald-600 hover:bg-emerald-700 px-4 py-3 rounded-lg font-semibold mb-4"
            >
              Load Memory
            </button>

            <div className="h-[480px] overflow-y-auto space-y-3">
              {memory.length === 0 && (
                <p className="text-slate-500">No memory loaded yet.</p>
              )}

              {memory.map((item, index) => (
                <div key={index} className="bg-slate-800 p-3 rounded-lg">
                  <p className="text-xs text-slate-400">User</p>
                  <p className="text-sm mb-2">{item.user_message}</p>

                  <p className="text-xs text-slate-400">Assistant</p>
                  <p className="text-sm text-slate-300">
                    {item.assistant_response.slice(0, 160)}...
                  </p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
