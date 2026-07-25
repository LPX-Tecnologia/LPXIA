"use client";

import Link from 'next/link';
import { useEffect, useState } from 'react';

interface HealthResponse {
  status: string;
}

export default function HomePage() {
  const [health, setHealth] = useState<string>('checking...');

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/health`)
      .then((response) => response.json())
      .then((data: HealthResponse) => setHealth(data.status))
      .catch(() => setHealth('offline'));
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-[radial-gradient(circle_at_top,_rgba(59,130,246,0.18),_transparent_70%)] px-6 py-16">
      <div className="w-full max-w-5xl rounded-3xl border border-slate-800 bg-slate-900/70 p-8 shadow-2xl shadow-cyan-950/40 backdrop-blur">
        <div className="flex flex-wrap items-center justify-between gap-4">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">LPX-NEXUS</p>
            <h1 className="mt-2 text-4xl font-semibold text-white sm:text-5xl">
              The intelligent platform for building with AI.
            </h1>
          </div>
          <div className="rounded-full border border-cyan-500/30 bg-cyan-500/10 px-4 py-2 text-sm text-cyan-300">
            API status: {health}
          </div>
        </div>

        <div className="mt-8 flex flex-wrap gap-3">
          <Link href="/dashboard" className="rounded-full bg-cyan-500 px-5 py-3 text-sm font-medium text-slate-950 transition hover:bg-cyan-400">
            Open dashboard
          </Link>
          <Link href="/chat" className="rounded-full border border-cyan-500/40 px-5 py-3 text-sm font-medium text-cyan-300 transition hover:border-cyan-400 hover:text-cyan-200">
            Open chat
          </Link>
          <Link href="/orchestrator" className="rounded-full border border-cyan-500/40 px-5 py-3 text-sm font-medium text-cyan-300 transition hover:border-cyan-400 hover:text-cyan-200">
            Open orchestrator
          </Link>
          <Link href="/memory" className="rounded-full border border-cyan-500/40 px-5 py-3 text-sm font-medium text-cyan-300 transition hover:border-cyan-400 hover:text-cyan-200">
            Open memory
          </Link>
          <Link href="/rag" className="rounded-full border border-cyan-500/40 px-5 py-3 text-sm font-medium text-cyan-300 transition hover:border-cyan-400 hover:text-cyan-200">
            Open RAG
          </Link>
          <Link href="/modules" className="rounded-full border border-cyan-500/40 px-5 py-3 text-sm font-medium text-cyan-300 transition hover:border-cyan-400 hover:text-cyan-200">
            Explore modules
          </Link>
        </div>

        <div className="mt-10 grid gap-6 md:grid-cols-3">
          <div className="rounded-2xl border border-slate-800 bg-slate-950/70 p-6">
            <h2 className="text-lg font-semibold text-white">Authentication</h2>
            <p className="mt-2 text-sm text-slate-400">JWT-based login and registration ready for your product experience.</p>
          </div>
          <div className="rounded-2xl border border-slate-800 bg-slate-950/70 p-6">
            <h2 className="text-lg font-semibold text-white">Dashboard</h2>
            <p className="mt-2 text-sm text-slate-400">A modular workspace for agents, projects, and workflows.</p>
          </div>
          <div className="rounded-2xl border border-slate-800 bg-slate-950/70 p-6">
            <h2 className="text-lg font-semibold text-white">Extensible</h2>
            <p className="mt-2 text-sm text-slate-400">Built to grow from a startup MVP into a full AI operating layer.</p>
          </div>
        </div>
      </div>
    </main>
  );
}
