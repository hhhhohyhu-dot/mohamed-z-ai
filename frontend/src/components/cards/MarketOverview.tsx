interface Props {
  symbol: string;
  price: number;
  trend: string;
  signal: string;
  confidence: number;
}

export default function MarketOverview({
  symbol,
  price,
  trend,
  signal,
  confidence,
}: Props) {
  const signalColor =
    signal === "BUY"
      ? "bg-green-500/20 text-green-400 border-green-500/30"
      : signal === "SELL"
      ? "bg-red-500/20 text-red-400 border-red-500/30"
      : "bg-yellow-500/20 text-yellow-400 border-yellow-500/30";

  const trendColor =
    trend === "Bullish"
      ? "text-green-400"
      : "text-red-400";

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-xl">

      <div className="mb-8 flex flex-wrap items-center justify-between gap-4">

        <div>
          <h2 className="text-3xl font-bold text-white">
            Market Overview
          </h2>

          <p className="mt-2 text-slate-400">
            Live market information and AI analysis
          </p>
        </div>

        <div
          className={`rounded-full border px-5 py-2 text-sm font-bold ${signalColor}`}
        >
          {signal}
        </div>

      </div>

      <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-5">

        <div className="rounded-xl bg-slate-800/40 p-5 transition hover:bg-slate-800">

          <p className="text-sm text-slate-400">
            Symbol
          </p>

          <h3 className="mt-3 text-3xl font-bold text-white">
            {symbol}
          </h3>

        </div>

        <div className="rounded-xl bg-slate-800/40 p-5 transition hover:bg-slate-800">

          <p className="text-sm text-slate-400">
            Current Price
          </p>

          <h3 className="mt-3 text-3xl font-bold text-cyan-400">
            ${price.toLocaleString()}
          </h3>

        </div>

        <div className="rounded-xl bg-slate-800/40 p-5 transition hover:bg-slate-800">

          <p className="text-sm text-slate-400">
            Trend
          </p>

          <h3 className={`mt-3 text-3xl font-bold ${trendColor}`}>
            {trend}
          </h3>

        </div>

        <div className="rounded-xl bg-slate-800/40 p-5 transition hover:bg-slate-800">

          <p className="text-sm text-slate-400">
            AI Signal
          </p>

          <h3
            className={`mt-3 text-3xl font-bold ${
              signal === "BUY"
                ? "text-green-400"
                : signal === "SELL"
                ? "text-red-400"
                : "text-yellow-400"
            }`}
          >
            {signal}
          </h3>

        </div>

        <div className="rounded-xl bg-slate-800/40 p-5 transition hover:bg-slate-800">

          <p className="text-sm text-slate-400">
            Confidence
          </p>

          <h3 className="mt-3 text-3xl font-bold text-cyan-400">
            {confidence}%
          </h3>

          <div className="mt-5 h-2 w-full rounded-full bg-slate-700">

            <div
              className="h-2 rounded-full bg-cyan-400 transition-all duration-700"
              style={{
                width: `${Math.min(confidence, 100)}%`,
              }}
            />

          </div>

        </div>

      </div>

      <div className="mt-8 flex items-center justify-between border-t border-slate-800 pt-5 text-sm text-slate-400">

        <span>
          Last Update
        </span>

        <span>
          {new Date().toLocaleTimeString()}
        </span>

      </div>

    </section>
  );
}