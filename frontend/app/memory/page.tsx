'use client';

import { FormEvent, useEffect, useState } from 'react';
import Link from 'next/link';

interface MemoryItem {
  id: string;
  title: string;
  content: string;
  memory_type: string;
}

export default function MemoryPage() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [memoryType, setMemoryType] = useState('short_term');
  const [items, setItems] = useState<MemoryItem[]>([]);

  const loadMemories = async () => {
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/memory/`, {
      headers: { Authorization: 'Bearer demo-token' },
    });
    if (response.ok) {
      const data = await response.json();
      setItems(data);
    }
  };

  useEffect(() => {
    void loadMemories();
  }, []);

  const handleSubmit = async (event: FormEvent) => {
    event.preventDefault();
    await fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/memory/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: 'Bearer demo-token',
      },
      body: JSON.stringify({ title, content, memory_type: memoryType }),
    });
    setTitle('');
    setContent('');
    setMemoryType('short_term');
    await loadMemories();
  };

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-16 text-slate-100">
      <div className="mx-auto flex max-w-5xl flex-col gap-6 rounded-3xl border border-slate-800 bg-slate-900/80 p-8 shadow-2xl shadow-cyan-950/30">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Memory</p>
            <h1 className="mt-2 text-3xl font-semibold">Capture short-term, long-term, preference, and feedback memories</h1>
          </div>
          <Link href="/" className="rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:border-cyan-500 hover:text-cyan-300">
            Back home
          </Link>
        </div>

        <form onSubmit={handleSubmit} className="grid gap-4 rounded-2xl border border-slate-800 bg-slate-950/70 p-6">
          <label className="text-sm text-slate-300">
            Title
            <input value={title} onChange={(event) => setTitle(event.target.value)} className="mt-2 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100" />
          </label>
          <label className="text-sm text-slate-300">
            Content
            <textarea value={content} onChange={(event) => setContent(event.target.value)} className="mt-2 min-h-24 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100" />
          </label>
          <label className="text-sm text-slate-300">
            Memory type
            <select value={memoryType} onChange={(event) => setMemoryType(event.target.value)} className="mt-2 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100">
              <option value="short_term">Short term</option>
              <option value="long_term">Long term</option>
              <option value="preferences">Preferences</option>
              <option value="feedback">Feedback</option>
            </select>
          </label>
          <button type="submit" className="rounded-full bg-cyan-500 px-5 py-3 text-sm font-medium text-slate-950 transition hover:bg-cyan-400">
            Save memory
          </button>
        </form>

        <div className="grid gap-4">
          {items.map((item) => (
            <div key={item.id} className="rounded-2xl border border-slate-800 bg-slate-950/70 p-4">
              <div className="flex items-center justify-between">
                <p className="text-sm font-medium text-white">{item.title}</p>
                <span className="rounded-full bg-cyan-500/10 px-3 py-1 text-xs uppercase tracking-[0.2em] text-cyan-300">{item.memory_type}</span>
              </div>
              <p className="mt-2 text-sm text-slate-400">{item.content}</p>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
