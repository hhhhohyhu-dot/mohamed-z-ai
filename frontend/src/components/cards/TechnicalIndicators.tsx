interface Props {
  ema20: number;
  ema50: number;
  ema200: number;
  rsi: number;
  macd: number;
  atr: number;
}

export default function TechnicalIndicators({
  ema20,
  ema50,
  ema200,
  rsi,
  macd,
  atr,
}: Props) {
  const cards = [
    { title: "EMA 20", value: ema20 },
    { title: "EMA 50", value: ema50 },
    { title: "EMA 200", value: ema200 },
    { title: "RSI", value: rsi },
    { title: "MACD", value: macd },
    { title: "ATR", value: atr },
  ];

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-6 text-2xl font-bold text-white">
        Technical Indicators
      </h2>

      <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-6">
        {cards.map((item) => (
          <div
            key={item.title}
            className="rounded-xl border border-slate-700 bg-slate-800 p-4"
          >
            <p className="text-sm text-slate-400">
              {item.title}
            </p>

            <h3 className="mt-2 text-xl font-bold text-cyan-400">
              {Number(item.value).toFixed(2)}
            </h3>
          </div>
        ))}
      </div>
    </div>
  );
}