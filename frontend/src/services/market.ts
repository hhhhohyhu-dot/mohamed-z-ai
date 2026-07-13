import api from "./api";
import { MarketData } from "@/types/market";

export async function analyzeMarket(
  symbol: string
): Promise<MarketData> {
  const response = await api.post<MarketData>("/api/analyze", {
    symbol,
  });

  return response.data;
}

export async function getDashboard(
  symbol: string,
  timeframe: string = "1h"
) {
  const response = await api.get(
    `/api/dashboard/${encodeURIComponent(symbol)}`,
    {
      params: {
        timeframe,
      },
    }
  );

  return response.data;
}