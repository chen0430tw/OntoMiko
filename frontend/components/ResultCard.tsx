export type DivineResult = {
  category: string;
  state: string;
  reason: string;
  permission_score?: number;
  note?: string;
};

export default function ResultCard({ result }: { result: DivineResult | null }) {
  if (!result) return null;

  return (
    <div className="mt-6 rounded-2xl border border-slate-700 bg-slate-900 p-6 shadow-lg">
      <h2 className="text-2xl font-bold">{result.category}</h2>
      <p className="mt-2 text-slate-300">终态：{result.state}</p>
      <p className="mt-4">{result.reason}</p>
      {typeof result.permission_score === "number" && (
        <p className="mt-4">许可度：{(result.permission_score * 100).toFixed(1)}%</p>
      )}
      {result.note && <p className="mt-2 text-pink-300">OntoMiko 备注：{result.note}</p>}
    </div>
  );
}
