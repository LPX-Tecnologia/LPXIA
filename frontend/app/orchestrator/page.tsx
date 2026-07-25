'use client';

import { FormEvent, useState } from 'react';
import Link from 'next/link';

interface ToolPlan {
  name: string;
  purpose: string;
}

interface OrchestratorResponse {
  agent: string;
  summary: string;
  context: string | null;
  memory_used: boolean;
  tools: ToolPlan[];
}

export default function OrchestratorPage() {
  const [agent, setAgent] = useState('research');
  const [prompt, setPrompt] = useState('Summarize the opportunity for a B2B AI startup.');
  const [context, setContext] = useState('Target: SMB SaaS, Europe, 2026');
  const [useMemory, setUseMemory] = useState(true);
  const [tools, setTools] = useState<string[]>([]);
  const [result, setResult] = useState<OrchestratorResponse | null>(null);

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/orchestrator/plan`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ agent, prompt, context, use_memory: useMemory, tools }),
    });
    const payload: OrchestratorResponse = await response.json();
    setResult(payload);
  };

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-16 text-slate-100">
      <div className="mx-auto flex max-w-5xl flex-col gap-6 rounded-3xl border border-slate-800 bg-slate-900/80 p-8 shadow-2xl shadow-cyan-950/30">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Orchestrator</p>
            <h1 className="mt-2 text-3xl font-semibold">Choose an agent and build an execution plan</h1>
          </div>
          <Link href="/" className="rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:border-cyan-500 hover:text-cyan-300">
            Back home
          </Link>
        </div>

        <form onSubmit={handleSubmit} className="grid gap-4 rounded-2xl border border-slate-800 bg-slate-950/70 p-6">
          <label className="text-sm text-slate-300">
            Agent
            <select value={agent} onChange={(event) => setAgent(event.target.value)} className="mt-2 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100">
              <option value="research">Research Agent</option>
              <option value="design">Design Agent</option>
              <option value="ops">Ops Agent</option>
            </select>
          </label>

          <label className="text-sm text-slate-300">
            Prompt
            <textarea value={prompt} onChange={(event) => setPrompt(event.target.value)} className="mt-2 min-h-24 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100" />
          </label>

          <label className="text-sm text-slate-300">
            Context
            <textarea value={context} onChange={(event) => setContext(event.target.value)} className="mt-2 min-h-20 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100" />
          </label>

          <label className="flex items-center gap-2 text-sm text-slate-300">
            <input type="checkbox" checked={useMemory} onChange={() => setUseMemory((value) => !value)} />
            Use memory
          </label>

          <button type="submit" className="rounded-full bg-cyan-500 px-5 py-3 text-sm font-medium text-slate-950 transition hover:bg-cyan-400">
            Build plan
          </button>
        </form>

        {result && (
          <div className="rounded-2xl border border-slate-800 bg-slate-950/70 p-6">
            <h2 className="text-xl font-semibold text-white">Execution plan</h2>
            <p className="mt-3 text-sm text-slate-300">{result.summary}</p>
            <p className="mt-3 text-sm text-cyan-400">Memory used: {result.memory_used ? 'yes' : 'no'}</p>
            <div className="mt-4 space-y-2">
              {result.tools.map((tool) => (
                <div key={tool.name} className="rounded-xl border border-slate-800 bg-slate-900/70 px-4 py-3 text-sm text-slate-300">
                  <p className="font-medium text-white">{tool.name}</p>
                  <p className="mt-1 text-slate-400">{tool.purpose}</p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </main>
  );
}
