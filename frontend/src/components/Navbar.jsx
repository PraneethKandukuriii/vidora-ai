function Navbar() {
  return (
    <nav className="border-b border-white/10">
      <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-5">
        <h2 className="text-xl font-semibold tracking-tight">
          Vidora
        </h2>

        <span className="text-sm text-zinc-500">
          AI Video Assistant
        </span>
      </div>
    </nav>
  );
}

export default Navbar;