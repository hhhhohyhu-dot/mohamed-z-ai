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

      <div className="space-y-4">

        {reasons.map((reason, index) => (

          <div
            key={index}
            className="flex items-center gap-4 rounded-xl border border-slate-700 bg-slate-800 p-4"
          >
            <div className="flex h-10 w-10 items-center justify-center rounded-full bg-green-500 font-bold text-white">
              ✓
            </div>

            <p className="text-slate-300">
              {reason}
            </p>

          </div>

        ))}

      </div>

    </div>
  );
}