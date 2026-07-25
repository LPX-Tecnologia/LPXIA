"use client";

import Link from 'next/link';
import { useEffect, useState } from 'react';

type DashboardData = {
  stats: {
    users: number;
    projects: number;
    active_ai_agents: number;
    logs_today: number;
  };
  users: Array<{ id: number; name: string; role: string; status: string }>;
  projects: Array<{ id: number; name: string; status: string; owner: string }>;
  ai: Array<{ id: number; name: string; health: string }>;
  logs: Array<{ id: number; message: string; level: string }>;
};

const defaultData: DashboardData = {
  stats: { users: 0, projects: 0, active_ai_agents: 0, logs_today: 0 },
  users: [],
  projects: [],
  ai: [],
  logs: [],
};

export default function DashboardPage() {
  const [data, setData] = useState<DashboardData>(defaultData);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    async function loadDashboard() {
      const token = localStorage.getItem('lpx_access_token');
      if (!token) {
        window.location.href = '/login';
        return;
      }

      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/dashboard/summary`, {
          headers: { Authorization: `Bearer ${token}` },
        });

        if (!response.ok) {
          throw new Error('Unable to load dashboard');
        }

        const json = await response.json();
        setData(json);
      } catch {
        setData(defaultData);
      } finally {
        setIsLoading(false);
      }
    }

    loadDashboard();
  }, []);

  const cards = [
    { label: 'Users', value: data.stats.users.toString(), detail: 'Active accounts' },
    { label: 'Projects', value: data.stats.projects.toString(), detail: 'Open initiatives' },
    { label: 'AI', value: data.stats.active_ai_agents.toString(), detail: 'Agents online' },
    { label: 'Logs', value: data.stats.logs_today.toString(), detail: 'Entries today' },
  ];

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-16 text-slate-100">
      <div className="mx-auto flex max-w-6xl flex-col gap-8">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Dashboard</p>
            <h1 className="mt-2 text-3xl font-semibold">Operations center for LPX-NEXUS</h1>
          </div>
          <Link href="/" className="rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:border-cyan-500 hover:text-cyan-300">
            Back home
          </Link>
        </div>

        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
          {cards.map((card) => (
            <div key={card.label} className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
              <p className="text-sm text-slate-400">{card.label}</p>
              <p className="mt-3 text-3xl font-semibold text-white">{isLoading ? '—' : card.value}</p>
              <p className="mt-2 text-sm text-cyan-400">{card.detail}</p>
            </div>
          ))}
        </div>

        <div className="grid gap-6 lg:grid-cols-2">
          <section className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
            <h2 className="text-xl font-semibold text-white">Users</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-300">
              {data.users.length > 0 ? data.users.map((user) => (
                <li key={user.id} className="flex justify-between rounded-lg bg-slate-800/70 px-3 py-2"><span>{user.name}</span><span>{user.role}</span></li>
              )) : <li className="rounded-lg bg-slate-800/70 px-3 py-2">No users available.</li>}
            </ul>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
            <h2 className="text-xl font-semibold text-white">Projects</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-300">
              {data.projects.length > 0 ? data.projects.map((project) => (
                <li key={project.id} className="rounded-lg bg-slate-800/70 px-3 py-2">{project.name} — {project.status}</li>
              )) : <li className="rounded-lg bg-slate-800/70 px-3 py-2">No projects available.</li>}
            </ul>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
            <h2 className="text-xl font-semibold text-white">AI</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-300">
              {data.ai.length > 0 ? data.ai.map((agent) => (
                <li key={agent.id} className="rounded-lg bg-slate-800/70 px-3 py-2">{agent.name} — {agent.health}</li>
              )) : <li className="rounded-lg bg-slate-800/70 px-3 py-2">No agents available.</li>}
            </ul>
          </section>

          <section className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
            <h2 className="text-xl font-semibold text-white">Logs</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-300">
              {data.logs.length > 0 ? data.logs.map((log) => (
                <li key={log.id} className="rounded-lg bg-slate-800/70 px-3 py-2">{log.level} — {log.message}</li>
              )) : <li className="rounded-lg bg-slate-800/70 px-3 py-2">No logs available.</li>}
            </ul>
          </section>
        </div>
      </div>
    </main>
  );
}
