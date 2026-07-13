interface Props {
  reasons: string[];
}

export default function AIAnalysisCard({
  reasons,
}: Props) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">

      <h2 className="mb-6 text-xl font-bold text-white">
        AI Analysis
      </h2>

      <div className="space-y-3">

        {reasons.map((reason, index) => (
          <div
            key={index}
            className="rounded-lg bg-slate-800 p-3 text-slate-300"
          >
            ✅ {reason}
          </div>
        ))}

      </div>

    </div>
  );
}