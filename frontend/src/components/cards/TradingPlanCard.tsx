interface Props {
  entry: number;
  stopLoss: number;
  takeProfit1: number;
  takeProfit2: number;
}

export default function TradingPlanCard({
  entry,
  stopLoss,
  takeProfit1,
  takeProfit2,
}: Props) {
  const Row = ({
    title,
    value,
    color,
  }: {
    title: string;
    value: number;
    color: string;
  }) => (
    <div className="flex items-center justify-between rounded-xl bg-slate-800 px-5 py-4">
      <span className="text-slate-400">{title}</span>

      <span className={`text-xl font-bold ${color}`}>
        {value.toFixed(2)}
      </span>
    </div>
  );

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-xl font-bold text-white">
        Trading Plan
      </h2>

      <div className="space-y-4">

        <Row
          title="Entry"
          value={entry}
          color="text-cyan-400"
        />

        <Row
          title="Stop Loss"
          value={stopLoss}
          color="text-red-400"
        />

        <Row
          title="Take Profit 1"
          value={takeProfit1}
          color="text-green-400"
        />

        <Row
          title="Take Profit 2"
          value={takeProfit2}
          color="text-green-400"
        />

      </div>

    </div>
  );
}