interface Props {
  ema20: number;
  ema50: number;
  ema200: number;
  rsi: number;
  macd: number;
  atr: number;
}

export default function IndicatorsCard(props: Props) {
  const indicators = [
    { title: "EMA20", value: props.ema20 },
    { title: "EMA50", value: props.ema50 },
    { title: "EMA200", value: props.ema200 },
    { title: "RSI", value: props.rsi },
    { title: "MACD", value: props.macd },
    { title: "ATR", value: props.atr },
  ];

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-xl font-bold text-white">
        Technical Indicators
      </h2>

      <div className="grid grid-cols-2 gap-5 lg:grid-cols-3">

        {indicators.map((item) => (

          <div
            key={item.title}
            className="rounded-xl border border-slate-700 bg-slate-800 p-5 transition hover:border-cyan-500"
          >
            <p className="text-slate-400">
              {item.title}
            </p>

            <h3 className="mt-3 text-3xl font-bold text-white">
              {item.value.toFixed(2)}
            </h3>
          </div>

        ))}

      </div>

    </div>
  );
}