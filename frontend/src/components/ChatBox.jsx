import { useState } from "react";

function ChatBox() {
  const [question, setQuestion] = useState("");

  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Your video is ready. Ask me anything about its content.",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    const trimmedQuestion = question.trim();

    if (!trimmedQuestion || loading) {
      return;
    }

    setMessages((previousMessages) => [
      ...previousMessages,
      {
        role: "user",
        content: trimmedQuestion,
      },
    ]);

    setQuestion("");
    setLoading(true);

    // Temporary response.
    await new Promise((resolve) => setTimeout(resolve, 1200));

    setMessages((previousMessages) => [
      ...previousMessages,
      {
        role: "assistant",
        content:
          "This is a temporary response. Vidora's FastAPI backend will answer this question once we connect the API.",
      },
    ]);

    setLoading(false);
  };

  return (
    <div className="mx-auto max-w-4xl">
      <div className="mb-5">
        <h2 className="text-lg font-medium">
          Ask about your video
        </h2>

        <p className="mt-1 text-sm text-zinc-500">
          Ask questions directly from the video's content.
        </p>
      </div>

      <div className="overflow-hidden rounded-2xl border border-white/10 bg-white/[0.03] backdrop-blur-xl">
        <div className="min-h-[420px] space-y-6 p-6">
          {messages.map((message, index) => (
            <div
              key={index}
              className={
                message.role === "user"
                  ? "flex justify-end"
                  : "flex justify-start"
              }
            >
              <div
                className={
                  message.role === "user"
                    ? "max-w-[80%] rounded-2xl rounded-br-md bg-white px-4 py-3 text-sm text-black"
                    : "max-w-[80%] rounded-2xl rounded-bl-md border border-white/10 bg-white/[0.04] px-4 py-3 text-sm leading-6 text-zinc-300"
                }
              >
                {message.content}
              </div>
            </div>
          ))}

          {loading && (
            <div className="flex justify-start">
              <div className="rounded-2xl rounded-bl-md border border-white/10 bg-white/[0.04] px-4 py-3 text-sm text-zinc-500">
                Vidora is thinking...
              </div>
            </div>
          )}
        </div>

        <form
          onSubmit={handleSubmit}
          className="border-t border-white/10 p-3"
        >
          <div className="flex items-center rounded-xl border border-white/10 bg-black/40 px-4 py-1">
            <input
              type="text"
              value={question}
              onChange={(event) => setQuestion(event.target.value)}
              disabled={loading}
              placeholder="Ask anything about the video..."
              className="flex-1 bg-transparent py-3 text-sm text-white outline-none placeholder:text-zinc-600 disabled:opacity-50"
            />

            <button
              type="submit"
              disabled={!question.trim() || loading}
              className="ml-3 rounded-lg bg-white px-4 py-2 text-sm font-medium text-black transition hover:bg-zinc-200 disabled:cursor-not-allowed disabled:opacity-40"
            >
              Ask
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default ChatBox;