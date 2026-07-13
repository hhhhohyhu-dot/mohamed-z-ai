"use client";

interface SearchBarProps {
  symbol: string;
  setSymbol: (value: string) => void;
  onAnalyze: () => void;
}

export default function SearchBar({
  symbol,
  setSymbol,
  onAnalyze,
}: SearchBarProps) {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-5 shadow-xl">

      <div className="flex flex-col gap-4 lg:flex-row lg:items-center">

        {/* Search */}

        <div className="relative flex-1">

          <span className="absolute left-4 top-1/2 -translate-y-1/2 text-xl text-slate-400">
            🔍
          </span>

          <input
            value={symbol}
            onChange={(e) => setSymbol(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                onAnalyze();
              }
            }}
            placeholder="Search Asset (AAPL, BTC, XAUUSD, EURUSD...)"
            className="w-full rounded-xl border border-slate-700 bg-slate-950 py-4 pl-12 pr-4 text-lg text-white outline-none transition focus:border-cyan-500"
          />

        </div>

        {/* Status */}

        <div className="flex items-center justify-center rounded-xl border border-green-500/30 bg-green-500/10 px-5 py-4">

          <span className="mr-2 h-3 w-3 rounded-full bg-green-400 animate-pulse" />

          <span className="font-semibold text-green-400">
            LIVE
          </span>

        </div>

        {/* Analyze */}

        <button
          onClick={onAnalyze}
          className="rounded-xl bg-cyan-500 px-8 py-4 text-lg font-bold text-white transition hover:bg-cyan-600 active:scale-95"
        >
          ⚡ Analyze
        </button>

      </div>

      <div className="mt-4 flex flex-wrap gap-3 text-sm text-slate-400">

        <span className="rounded-full bg-slate-800 px-3 py-1">
          Stocks
        </span>

        <span className="rounded-full bg-slate-800 px-3 py-1">
          Crypto
        </span>

        <span className="rounded-full bg-slate-800 px-3 py-1">
          Forex
        </span>

        <span className="rounded-full bg-slate-800 px-3 py-1">
          Metals
        </span>

        <span className="rounded-full bg-slate-800 px-3 py-1">
          Indices
        </span>

      </div>

    </section>
  );
}