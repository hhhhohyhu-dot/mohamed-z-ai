const items = [
  "Dashboard",
  "Markets",
  "Watchlist",
  "Signals",
  "Portfolio",
  "History",
  "Settings",
];

export default function Sidebar() {
  return (
    <aside className="w-72 border-r border-slate-800 bg-slate-950 p-5">

      <h2 className="mb-6 text-sm uppercase tracking-widest text-slate-500">
        Navigation
      </h2>

      <div className="space-y-3">

        {items.map((item) => (
          <button
            key={item}
            className="w-full rounded-xl bg-slate-900 px-5 py-4 text-left text-white transition hover:bg-blue-600"
          >
            {item}
          </button>
        ))}

      </div>

    </aside>
  );
}