"use client";

import dynamic from "next/dynamic";

const AdvancedRealTimeChart = dynamic(
  () =>
    import("react-ts-tradingview-widgets").then(
      (mod) => mod.AdvancedRealTimeChart
    ),
  {
    ssr: false,
  }
);

interface Props {
  symbol: string;
  timeframe: string;
}

const symbols: Record<string, string> = {
  // Stocks
  AAPL: "NASDAQ:AAPL",
  MSFT: "NASDAQ:MSFT",
  NVDA: "NASDAQ:NVDA",
  AMZN: "NASDAQ:AMZN",
  TSLA: "NASDAQ:TSLA",
  META: "NASDAQ:META",

  // Crypto
  BTC: "BINANCE:BTCUSDT",
  ETH: "BINANCE:ETHUSDT",

  // Metals
  XAUUSD: "OANDA:XAUUSD",

  // Forex
  EURUSD: "FX:EURUSD",
  GBPUSD: "FX:GBPUSD",
  USDJPY: "FX:USDJPY",

  // Indices
  NAS100: "NASDAQ:NDX",
  SP500: "SP:SPX",
  DJI: "DJ:DJI",
};

type TVInterval =
  | "1"
  | "3"
  | "5"
  | "15"
  | "30"
  | "60"
  | "120"
  | "180"
  | "240"
  | "D"
  | "W";

const intervals: Record<string, TVInterval> = {
  "1m": "1",
  "5m": "5",
  "15m": "15",
  "30m": "30",
  "1h": "60",
  "4h": "240",
  "1d": "D",
};

export default function TradingChart({
  symbol,
  timeframe,
}: Props) {
  const tvSymbol =
    symbols[symbol.toUpperCase()] ??
    `NASDAQ:${symbol.toUpperCase()}`;

  const interval: TVInterval =
    intervals[timeframe] ?? "60";

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6 shadow-xl">
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h2 className="text-3xl font-bold text-white">
            Live Trading Chart
          </h2>

          <p className="mt-2 text-slate-400">
            {symbol.toUpperCase()} • {timeframe.toUpperCase()}
          </p>
        </div>

        <div className="rounded-full bg-green-500/20 px-4 py-2 text-sm font-bold text-green-400">
          LIVE
        </div>
      </div>

      <div className="overflow-hidden rounded-xl border border-slate-800">
        <AdvancedRealTimeChart
          theme="dark"
          symbol={tvSymbol}
          interval={interval}
          width="100%"
          height="750"
          autosize
          hide_side_toolbar={false}
          allow_symbol_change={false}
          withdateranges
        />
      </div>
    </section>
  );
}