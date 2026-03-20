"use client";

import { useState } from "react";
import ResultCard, { DivineResult } from "../components/ResultCard";
import { divineText } from "../lib/api";

export default function HomePage() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<DivineResult | null>(null);
  const [loading, setLoading] = useState(false);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    try {
      const data = await divineText(text);
      setResult(data);
    } catch (err) {
      setResult({
        category: "系统异常",
        state: "client-error",
        reason: "无法连接 OntoMiko 后端。",
      });
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="mx-auto max-w-3xl p-8">
      <div className="rounded-3xl border border-slate-800 bg-slate-900/70 p-8">
        <p className="text-sm uppercase tracking-[0.3em] text-pink-300">OntoMiko</p>
        <h1 className="mt-3 text-4xl font-black">宇宙许可占卜姬</h1>
        <p className="mt-4 text-slate-300">
          把你的天马行空交给宇宙审核。OntoMiko 会先看来源、承载、权限、代价与一致性，再决定宇宙是否点头。
        </p>

        <form onSubmit={onSubmit} className="mt-8">
          <textarea
            className="h-40 w-full rounded-2xl border border-slate-700 bg-slate-950 p-4 outline-none"
            placeholder="输入一个设想，例如：未来是否存在依靠潜势和惯性计算的通用拟构处理器？"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
          <button
            type="submit"
            className="mt-4 rounded-xl bg-pink-500 px-5 py-3 font-semibold text-white hover:bg-pink-400 disabled:opacity-50"
            disabled={!text.trim() || loading}
          >
            {loading ? "占验中..." : "开始占验"}
          </button>
        </form>

        <ResultCard result={result} />
      </div>
    </main>
  );
}
