import {
  ArrowUpRight,
  Play,
  Sparkles,
  MessageCircle,
  FileText,
  Lightbulb,
  Search,
} from "lucide-react";

function FloatingCard({ children, className = "" }) {
  return (
    <div
      className={`absolute rounded-2xl border border-white/10 bg-[#0d0d0f]/90 shadow-2xl backdrop-blur-xl ${className}`}
    >
      {children}
    </div>
  );
}

function App() {
  return (
    <main className="min-h-screen overflow-hidden bg-[#050505] text-white">

      {/* Background */}
      <div className="pointer-events-none fixed inset-0">
        <div className="absolute left-1/2 top-[15%] h-[500px] w-[500px] -translate-x-1/2 rounded-full bg-indigo-500/[0.08] blur-[140px]" />

        <div className="absolute left-[15%] top-[35%] h-[250px] w-[250px] rounded-full bg-blue-500/[0.04] blur-[120px]" />

        <div className="absolute right-[10%] top-[40%] h-[300px] w-[300px] rounded-full bg-violet-500/[0.04] blur-[130px]" />

        <div
          className="absolute inset-0 opacity-[0.035]"
          style={{
            backgroundImage:
              "linear-gradient(rgba(255,255,255,.5) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.5) 1px, transparent 1px)",
            backgroundSize: "80px 80px",
          }}
        />
      </div>

      {/* Navbar */}
      <nav className="sticky top-0 z-50 border-b border-white/[0.08] bg-[#050505]/80 backdrop-blur-xl">
        <div className="mx-auto flex h-[78px] max-w-[1320px] items-center justify-between px-6 lg:px-10">

          {/* Logo */}
          <div className="text-[21px] font-semibold tracking-[-0.04em]">
            Vidora
          </div>

          {/* Navigation */}
          <div className="hidden items-center gap-9 text-[13px] text-zinc-500 md:flex">
            <a className="cursor-pointer text-white transition hover:text-white">
              Home
            </a>

            <a className="cursor-pointer transition hover:text-white">
              Features
            </a>

            <a className="cursor-pointer transition hover:text-white">
              How it works
            </a>

            <a className="cursor-pointer transition hover:text-white">
              Pricing
            </a>
          </div>

          {/* CTA */}
          <button className="group flex items-center gap-2 rounded-full border border-white/15 px-5 py-2.5 text-[13px] transition hover:border-white/30 hover:bg-white/[0.05]">
            Get Started

            <ArrowUpRight
              size={15}
              className="transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
            />
          </button>

        </div>
      </nav>

      {/* Hero */}
      <section className="relative z-10 px-6 pt-10 lg:px-10 lg:pt-14">
        <div className="mx-auto max-w-[1320px]">

          {/* Hero Heading */}
          <div className="mx-auto max-w-[900px] text-center">

            <h1 className="text-[clamp(52px,6.5vw,88px)] font-medium leading-[0.9] tracking-[-0.075em]">
              Turn videos
              <br />

              <span className="bg-gradient-to-b from-white via-white to-zinc-500 bg-clip-text text-transparent">
                into knowledge.
              </span>
            </h1>

            <p className="mx-auto mt-5 max-w-[570px] text-[14px] leading-6 text-zinc-500">
              Vidora transforms YouTube videos into something you can
              understand, search, and talk to.
            </p>

          </div>

          {/* Product Visual */}
          <div className="relative mx-auto mt-8 h-[500px] max-w-[1100px]">

            {/* Main ambient glow */}
            <div className="absolute left-1/2 top-1/2 h-[450px] w-[450px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-indigo-500/[0.08] blur-[100px]" />

            {/* Vertical connection */}
            <div className="absolute left-1/2 top-[27%] h-[180px] w-px -translate-x-1/2 bg-gradient-to-b from-white/20 via-indigo-400/30 to-transparent" />

            {/* Left connection */}
            <div className="absolute left-[21%] top-[48%] h-px w-[190px] rotate-[16deg] bg-gradient-to-r from-transparent via-indigo-400/30 to-transparent" />

            {/* Right connection */}
            <div className="absolute right-[21%] top-[48%] h-px w-[190px] -rotate-[16deg] bg-gradient-to-r from-transparent via-indigo-400/30 to-transparent" />

            {/* Main Video */}
            <div className="absolute left-1/2 top-[2%] w-[620px] max-w-[82%] -translate-x-1/2">

              <div className="relative overflow-hidden rounded-[24px] border border-white/15 bg-[#101012] shadow-[0_30px_100px_rgba(0,0,0,.8)]">

                {/* Browser bar */}
                <div className="flex h-10 items-center justify-between border-b border-white/[0.08] px-4">

                  <div className="flex items-center gap-2">
                    <div className="h-2 w-2 rounded-full bg-red-500" />

                    <span className="text-[10px] text-zinc-500">
                      youtube.com
                    </span>
                  </div>

                  <span className="text-[10px] text-zinc-600">
                    vidora.ai
                  </span>

                </div>

                {/* Video */}
                <div className="relative h-[270px] overflow-hidden bg-gradient-to-br from-zinc-900 via-[#121216] to-black">

                  {/* Video glow */}
                  <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_35%,rgba(100,100,255,.18),transparent_45%)]" />

                  {/* Fake video frame */}
                  <div className="absolute inset-8 overflow-hidden rounded-xl border border-white/[0.06] bg-[#080809]">

                    <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_45%,rgba(255,255,255,.08),transparent_30%)]" />

                    {/* Play */}
                    <div className="absolute left-1/2 top-1/2 flex h-14 w-14 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border border-white/20 bg-white/[0.08] backdrop-blur-md">

                      <Play
                        size={20}
                        fill="white"
                      />

                    </div>

                    {/* Bottom gradient */}
                    <div className="absolute inset-x-0 bottom-0 h-24 bg-gradient-to-t from-black/80 to-transparent" />

                    {/* Timeline */}
                    <div className="absolute bottom-4 left-5 right-5">

                      <div className="mb-2 h-1 rounded-full bg-white/10">
                        <div className="h-1 w-[38%] rounded-full bg-white" />
                      </div>

                      <div className="flex justify-between text-[9px] text-zinc-500">
                        <span>04:21</span>
                        <span>12:48</span>
                      </div>

                    </div>

                  </div>

                  {/* Video title */}
                  <div className="absolute bottom-4 left-5">

                    <p className="text-sm font-medium">
                      The Future of AI
                    </p>

                    <p className="mt-1 text-[10px] text-zinc-600">
                      YouTube video
                    </p>

                  </div>

                </div>
              </div>

              {/* Processing */}
              <div className="absolute -bottom-5 left-1/2 flex -translate-x-1/2 items-center gap-2 whitespace-nowrap rounded-full border border-white/10 bg-[#0b0b0c] px-4 py-2 text-[10px] text-zinc-400 shadow-xl backdrop-blur-xl">

                <Sparkles
                  size={12}
                  className="text-indigo-400"
                />

                Vidora is understanding the video

                <span className="flex gap-1">
                  <span className="h-1 w-1 animate-pulse rounded-full bg-white/60" />

                  <span className="h-1 w-1 animate-pulse rounded-full bg-white/40 [animation-delay:150ms]" />

                  <span className="h-1 w-1 animate-pulse rounded-full bg-white/20 [animation-delay:300ms]" />
                </span>

              </div>

            </div>

            {/* Transcript */}
            <FloatingCard className="left-[2%] top-[32%] w-[175px] -rotate-3 p-4 transition-transform duration-500 hover:-translate-y-2 hover:rotate-0">

              <div className="mb-4 flex items-center gap-2">

                <FileText
                  size={13}
                  className="text-zinc-400"
                />

                <span className="text-[10px] text-zinc-500">
                  Transcript
                </span>

              </div>

              <div className="space-y-2">

                <div className="h-1.5 w-[90%] rounded-full bg-white/10" />

                <div className="h-1.5 w-[75%] rounded-full bg-white/10" />

                <div className="h-1.5 w-[82%] rounded-full bg-white/10" />

                <div className="h-1.5 w-[60%] rounded-full bg-white/[0.06]" />

              </div>

            </FloatingCard>

            {/* Insight */}
            <FloatingCard className="right-[2%] top-[31%] w-[195px] rotate-3 p-4 transition-transform duration-500 hover:-translate-y-2 hover:rotate-0">

              <div className="mb-4 flex items-center gap-2">

                <Lightbulb
                  size={13}
                  className="text-indigo-300"
                />

                <span className="text-[10px] text-zinc-500">
                  Key insight
                </span>

              </div>

              <p className="text-[12px] leading-5 text-zinc-300">
                AI systems learn patterns from large amounts of data.
              </p>

              <div className="mt-4 h-px bg-white/[0.06]" />

              <p className="mt-3 text-[9px] text-zinc-600">
                Extracted from 04:21
              </p>

            </FloatingCard>

            {/* AI Node */}
            <div className="absolute left-1/2 top-[48%] flex h-12 w-12 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border border-indigo-400/30 bg-indigo-500/10 shadow-[0_0_40px_rgba(99,102,241,.25)] backdrop-blur-xl">

              <Sparkles
                size={17}
                className="text-indigo-300"
              />

            </div>

            {/* Search */}
            <div className="absolute bottom-[18%] left-[18%] hidden items-center gap-2 rounded-xl border border-white/10 bg-black/70 px-3 py-2 backdrop-blur-xl lg:flex">

              <Search
                size={11}
                className="text-zinc-600"
              />

              <span className="text-[9px] text-zinc-600">
                Search this video
              </span>

            </div>

            {/* Q&A */}
            <FloatingCard className="bottom-[2%] left-1/2 w-[400px] max-w-[80%] -translate-x-1/2 p-4 shadow-[0_20px_70px_rgba(0,0,0,.7)]">

              <div className="mb-3 flex items-center gap-2">

                <MessageCircle
                  size={14}
                  className="text-indigo-300"
                />

                <span className="text-[10px] text-zinc-500">
                  Ask Vidora
                </span>

              </div>

              {/* Question */}
              <div className="rounded-xl border border-white/[0.08] bg-white/[0.035] px-4 py-3">

                <p className="text-[12px] text-zinc-300">
                  How does the AI actually learn from this data?
                </p>

              </div>

              {/* Answer */}
              <div className="mt-3 flex items-start gap-3">

                <div className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-lg bg-white/10">

                  <Sparkles size={11} />

                </div>

                <p className="text-[11px] leading-5 text-zinc-500">
                  Vidora found this concept in the video and can explain it
                  using the surrounding context.
                </p>

              </div>

            </FloatingCard>

          </div>

          {/* CTA */}
          <div className="mt-2 flex flex-col items-center pb-12">

            <button className="group flex items-center gap-3 rounded-full bg-white px-7 py-3.5 text-[13px] font-medium text-black transition-all duration-300 hover:scale-[1.03] hover:bg-zinc-200">

              Try Vidora

              <ArrowUpRight
                size={16}
                className="transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
              />

            </button>

          </div>

        </div>

      </section>

    </main>
  );
}

export default App;