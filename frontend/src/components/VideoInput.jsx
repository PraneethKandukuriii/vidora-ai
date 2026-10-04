import { useState } from "react";

function VideoInput({ onProcess }) {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!url.trim()) {
      return;
    }

    setLoading(true);

    // Temporary simulation.
    await new Promise((resolve) => setTimeout(resolve, 1500));

    setLoading(false);
    onProcess(url);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="mt-10 w-full max-w-3xl"
    >
      <div className="rounded-2xl border border-white/10 bg-white/[0.04] p-2 shadow-2xl backdrop-blur-xl">
        <div className="flex flex-col gap-2 sm:flex-row">
          <input
            type="text"
            value={url}
            onChange={(event) => setUrl(event.target.value)}
            placeholder="Paste a YouTube URL..."
            className="min-w-0 flex-1 rounded-xl bg-transparent px-4 py-4 text-sm text-white outline-none placeholder:text-zinc-600"
          />

          <button
            type="submit"
            disabled={loading}
            className="rounded-xl bg-white px-6 py-4 text-sm font-medium text-black transition hover:bg-zinc-200 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {loading ? "Processing..." : "Process Video"}
          </button>
        </div>
      </div>

      <p className="mt-3 text-xs text-zinc-600">
        Vidora will analyze the video's available transcript.
      </p>
    </form>
  );
}

export default VideoInput;