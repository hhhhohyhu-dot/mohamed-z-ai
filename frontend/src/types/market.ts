export interface MarketData {
  symbol: string;

  price: number;

  trend: string;

  signal: string;

  confidence: number;

  ema20: number;
  ema50: number;
  ema200: number;

  rsi: number;
  macd: number;
  atr: number;

  entry: number;
  stopLoss: number;

  takeProfit1: number;
  takeProfit2: number;

  analysis: string;
}