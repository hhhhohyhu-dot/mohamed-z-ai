interface Props {
  signal: string;
  confidence: number;
  risk: string;
  score: number;
}

export default function AIDecisionCard({
  signal,
  confidence,
  risk,
  score,
}: Props) {
  const signalStyle =
    signal === "BUY"
      ? {
          bg: "bg-green-500/20",
          text: "text-green-400",
          border: "border-green-500/30",
          icon: "🟢",
        }
      : signal === "SELL"
      ? {
          bg: "bg-red-500/20",
          text: "text-red-400",
          border: "border-red-500/30",
          icon: "🔴",
        }
      : {
          bg: "bg-yellow-500/20",
          text: "text-yellow-400",
          border: "border-yellow-500/30",
          icon: "🟡",
        };

  const riskStyle =
    risk === "Low"
      ? "text-green-400"
      : risk === "Medium"
      ? "text-yellow-400"
      : "text-red-400";

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-xl transition hover:border-cyan-500/40">

      <div className="mb-8 flex items-center justify-between">

        <div>
          <h2 className="text-3xl font-bold text-white">
            AI Decision
          </h2>

          <p className="mt-2 text-slate-400">
            Artificial Intelligence Trading Signal
          </p>
        </div>

        <div
          className={`rounded-full border px-5 py-2 font-bold ${signalStyle.bg} ${signalStyle.text} ${signalStyle.border}`}
        >
          {signalStyle.icon} {signal}
        </div>

      </div>

      <div className="grid gap-6 md:grid-cols-2">

        <div className="rounded-xl bg-slate-800/40 p-5">

          <p className="text-sm text-slate-400">
            Risk Level
          </p>

          <h3 className={`mt-3 text-3xl font-bold ${riskStyle}`}>
            {risk}
          </h3>

        </div>

        <div className="rounded-xl bg-slate-800/40 p-5">

          <p className="text-sm text-slate-400">
            AI Score
          </p>

          <h3 className="mt-3 text-3xl font-bold text-cyan-400">
            {score}/100
          </h3>

        </div>

      </div>

      <div className="mt-8">

        <div className="mb-2 flex items-center justify-between">

          <span className="text-slate-400">
            Confidence
          </span>

          <span className="font-bold text-cyan-400">
            {confidence}%
          </span>

        </div>

        <div className="h-3 overflow-hidden rounded-full bg-slate-700">

          <div
            className="h-3 rounded-full bg-cyan-500 transition-all duration-700"
            style={{
              width: `${Math.min(confidence, 100)}%`,
            }}
          />

        </div>

      </div>

      <div className="mt-8">

        <div className="mb-2 flex items-center justify-between">

          <span className="text-slate-400">
            AI Accuracy
          </span>

          <span className="font-bold text-green-400">
            {score}%
          </span>

        </div>

        <div className="h-3 overflow-hidden rounded-full bg-slate-700">

          <div
            className="h-3 rounded-full bg-green-500 transition-all duration-700"
            style={{
              width: `${Math.min(score, 100)}%`,
            }}
          />

        </div>

      </div>

      <div className="mt-8 rounded-xl border border-cyan-500/20 bg-cyan-500/5 p-5">

        <h3 className="mb-3 text-lg font-bold text-white">
          AI Recommendation
        </h3>

        {signal === "BUY" && (
          <ul className="space-y-2 text-slate-300">
            <li>✅ Strong bullish momentum detected.</li>
            <li>✅ Trend confirms buying opportunity.</li>
            <li>✅ Risk remains under control.</li>
          </ul>
        )}

        {signal === "SELL" && (
          <ul className="space-y-2 text-slate-300">
            <li>🔻 Bearish momentum is increasing.</li>
            <li>🔻 Selling pressure is dominant.</li>
            <li>🔻 Protect capital with stop-loss.</li>
          </ul>
        )}

        {signal === "HOLD" && (
          <ul className="space-y-2 text-slate-300">
            <li>⚠ Market is neutral.</li>
            <li>⚠ Wait for stronger confirmation.</li>
            <li>⚠ Avoid unnecessary entries.</li>
          </ul>
        )}

      </div>

    </section>
  );
}