"use client";

import { useState, useEffect } from "react";

import Navbar from "../layout/Navbar";
import Sidebar from "../layout/Sidebar";
import Footer from "../layout/Footer";
import SearchBar from "../ui/SearchBar";

import TradingChart from "../chart/TradingChart";

import MarketOverview from "../cards/MarketOverview";
import AIDecisionCard from "../cards/AIDecisionCard";
import TradingPlanCard from "../cards/TradingPlanCard";
import IndicatorsCard from "../cards/IndicatorsCard";
import AIAnalysisCard from "../cards/AIAnalysisCard";
import NewsCard from "../news/NewsCard";

import Watchlist from "../watchlist/Watchlist";

import { getDashboard } from "@/services/market";

export default function Dashboard() {
  const [symbol, setSymbol] = useState("AAPL");
  const [timeframe, setTimeframe] = useState("1h");

  const [marketData, setMarketData] = useState({
    symbol: "AAPL",
    timeframe: "1h",

    price: 0,

    trend: "",
    signal: "",
    confidence: 0,

    risk: "",
    score: 0,

    reasons: [] as string[],

    ema20: 0,
    ema50: 0,
    ema200: 0,

    rsi: 0,
    macd: 0,
    atr: 0,

    entry: 0,
    stopLoss: 0,
    takeProfit1: 0,
    takeProfit2: 0,
  });

  const [news, setNews] = useState<any[]>([]);

  const loadDashboard = async (
    asset: string,
    tf: string = timeframe
  ) => {
    try {
      const data = await getDashboard(asset, tf);

      setMarketData(data.market);
      setNews(data.news);
    } catch (error) {
      console.error(error);
    }
  };

  const handleAnalyze = async () => {
    await loadDashboard(symbol, timeframe);
  };

  useEffect(() => {
    loadDashboard(symbol, timeframe);

    const interval = setInterval(() => {
      loadDashboard(symbol, timeframe);
    }, 10000);

    return () => clearInterval(interval);
  }, [symbol, timeframe]);

  const timeframes = [
    "1m",
    "5m",
    "15m",
    "1h",
    "4h",
    "1d",
  ];

  return (
    <main className="min-h-screen bg-slate-950">
      <Navbar />

      <div className="flex">
        <Sidebar />

        <section className="flex-1 space-y-8 p-8">

          <SearchBar
            symbol={symbol}
            setSymbol={setSymbol}
            onAnalyze={handleAnalyze}
          />

          <Watchlist
            selected={symbol}
            onSelect={(asset) => {
              setSymbol(asset);
            }}
          />

          <div className="flex flex-wrap gap-3">

            {timeframes.map((tf) => (

              <button
                key={tf}
                onClick={() => setTimeframe(tf)}
                className={`rounded-xl px-5 py-2 font-semibold transition

                ${
                  timeframe === tf
                    ? "bg-cyan-500 text-white"
                    : "bg-slate-900 text-slate-300 hover:bg-slate-800"
                }`}
              >
                {tf.toUpperCase()}
              </button>

            ))}

          </div>

          <MarketOverview
            symbol={marketData.symbol}
            price={marketData.price}
            trend={marketData.trend}
            signal={marketData.signal}
            confidence={marketData.confidence}
          />

          <div className="grid gap-6 lg:grid-cols-2">

            <AIDecisionCard
              signal={marketData.signal}
              confidence={marketData.confidence}
              risk={marketData.risk}
              score={marketData.score}
            />

            <TradingPlanCard
              entry={marketData.entry}
              stopLoss={marketData.stopLoss}
              takeProfit1={marketData.takeProfit1}
              takeProfit2={marketData.takeProfit2}
            />

          </div>

          <IndicatorsCard
            ema20={marketData.ema20}
            ema50={marketData.ema50}
            ema200={marketData.ema200}
            rsi={marketData.rsi}
            macd={marketData.macd}
            atr={marketData.atr}
          />

          <TradingChart symbol={symbol} timeframe={timeframe} />

          <AIAnalysisCard
            reasons={marketData.reasons}
          />

          <NewsCard
            news={news}
          />

        </section>
      </div>

      <Footer />
    </main>
  );
}