export default function Navbar() {
  return (
    <header className="h-16 border-b border-slate-800 bg-slate-950">
      <div className="mx-auto flex h-full items-center justify-between px-6">

        <div className="flex items-center gap-3">

          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-600 font-bold text-white">
            M
          </div>

          <div>
            <h1 className="text-lg font-bold text-white">
              Mohamed Z AI
            </h1>

            <p className="text-xs text-slate-400">
              Professional Trading Platform
            </p>
          </div>

        </div>

        <nav className="flex items-center gap-8 text-sm text-slate-300">

          <button className="hover:text-white">
            Dashboard
          </button>

          <button className="hover:text-white">
            Markets
          </button>

          <button className="hover:text-white">
            News
          </button>

          <button className="hover:text-white">
            AI
          </button>

        </nav>

      </div>
    </header>
  );
}