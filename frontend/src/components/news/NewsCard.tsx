interface NewsItem {
  title: string;
  summary: string;
  sentiment: string;
  impact: number;
  confidence: number;
}

interface Props {
  news: NewsItem[];
}

export default function NewsCard({ news }: Props) {
  if (!news?.length) {
    return (
      <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
        <h2 className="mb-6 text-2xl font-bold text-white">
          AI Market News
        </h2>

        <p className="text-slate-400">
          No news available.
        </p>
      </div>
    );
  }

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-2xl font-bold text-white">
        AI Market News
      </h2>

      <div className="space-y-5">

        {news.map((item, index) => {

          const color =
            item.sentiment === "Bullish"
              ? "text-green-400"
              : item.sentiment === "Bearish"
              ? "text-red-400"
              : "text-yellow-400";

          return (
            <div
              key={index}
              className="rounded-xl border border-slate-800 bg-slate-950 p-5"
            >
              <div className="flex items-center justify-between">

                <span className={`font-bold ${color}`}>
                  {item.sentiment}
                </span>

                <span className="text-cyan-400 font-semibold">
                  Impact {item.impact}%
                </span>

              </div>

              <h3 className="mt-4 text-lg font-bold text-white">
                {item.title}
              </h3>

              <p className="mt-3 text-slate-400">
                {item.summary}
              </p>

              <div className="mt-4 text-sm text-slate-500">
                Confidence: {item.confidence}%
              </div>

            </div>
          );
        })}

      </div>

    </div>
  );
}