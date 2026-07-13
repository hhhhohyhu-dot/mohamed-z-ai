interface Props {
  entry: number;
  stopLoss: number;
  takeProfit1: number;
  takeProfit2: number;
}

export default function TradeSetup({
  entry,
  stopLoss,
  takeProfit1,
  takeProfit2,
}: Props) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-6 text-2xl font-bold text-white">
        Trade Setup
      </h2>

      <div className="grid grid-cols-2 gap-4">
        <div className="rounded-xl border border-slate-700 bg-slate-800 p-5">
          <p className="text-sm text-slate-400">
            Entry
          </p>

          <h3 className="mt-2 text-2xl font-bold text-cyan-400">
            {entry.toFixed(2)}
          </h3>
        </div>

        <div className="rounded-xl border border-red-500 bg-slate-800 p-5">
          <p className="text-sm text-slate-400">
            Stop Loss
          </p>

          <h3 className="mt-2 text-2xl font-bold text-red-400">
            {stopLoss.toFixed(2)}
          </h3>
        </div>

        <div className="rounded-xl border border-green-500 bg-slate-800 p-5">
          <p className="text-sm text-slate-400">
            Take Profit 1
          </p>

          <h3 className="mt-2 text-2xl font-bold text-green-400">
            {takeProfit1.toFixed(2)}
          </h3>
        </div>

        <div className="rounded-xl border border-green-500 bg-slate-800 p-5">
          <p className="text-sm text-slate-400">
            Take Profit 2
          </p>

          <h3 className="mt-2 text-2xl font-bold text-green-400">
            {takeProfit2.toFixed(2)}
          </h3>
        </div>
      </div>
    </div>
  );
}