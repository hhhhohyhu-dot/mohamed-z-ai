"use client";

interface Props {
  selected: string;
  onSelect: (symbol: string) => void;
}

const assets = [
  {
    category: "📈 Stocks",
    items: ["AAPL", "MSFT", "NVDA", "AMZN", "META", "TSLA"],
  },
  {
    category: "₿ Crypto",
    items: ["BTC", "ETH"],
  },
  {
    category: "💱 Forex",
    items: ["EURUSD", "GBPUSD", "USDJPY"],
  },
  {
    category: "🥇 Metals",
    items: ["XAUUSD", "SILVER"],
  },
  {
    category: "🌍 Indices",
    items: ["NAS100", "SP500", "DJI"],
  },
];

export default function Watchlist({
  selected,
  onSelect,
}: Props) {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6 shadow-xl">

      <div className="mb-8 flex items-center justify-between">

        <div>

          <h2 className="text-3xl font-bold text-white">
            Watchlist
          </h2>

          <p className="mt-2 text-slate-400">
            Select any asset to analyze with AI
          </p>

        </div>

        <div className="rounded-full bg-cyan-500/20 px-4 py-2 text-sm font-semibold text-cyan-400">
          {assets.reduce(
            (total, group) => total + group.items.length,
            0
          )}{" "}
          Assets
        </div>

      </div>

      <div className="space-y-8">

        {assets.map((group) => (

          <div key={group.category}>

            <div className="mb-4 flex items-center justify-between">

              <h3 className="text-lg font-bold text-white">
                {group.category}
              </h3>

              <span className="rounded-full bg-slate-800 px-3 py-1 text-xs text-slate-400">
                {group.items.length}
              </span>

            </div>

            <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">

              {group.items.map((asset) => {

                const active = selected === asset;

                return (

                  <button
                    key={asset}
                    onClick={() => onSelect(asset)}
                    className={`group rounded-xl border p-4 text-left transition-all duration-300

                    ${
                      active
                        ? "border-cyan-500 bg-cyan-500/15 shadow-lg shadow-cyan-500/10"
                        : "border-slate-800 bg-slate-950 hover:border-cyan-500 hover:bg-slate-800"
                    }`}
                  >

                    <div className="flex items-center justify-between">

                      <h4
                        className={`text-lg font-bold ${
                          active
                            ? "text-cyan-300"
                            : "text-white"
                        }`}
                      >
                        {asset}
                      </h4>

                      <div
                        className={`h-3 w-3 rounded-full ${
                          active
                            ? "bg-green-400"
                            : "bg-slate-600 group-hover:bg-cyan-400"
                        }`}
                      />

                    </div>

                    <p className="mt-3 text-sm text-slate-400">
                      Click to analyze
                    </p>

                  </button>

                );

              })}

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}