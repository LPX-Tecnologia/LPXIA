'use client';

import { FormEvent, useState } from 'react';
import Link from 'next/link';

interface RetrievedDocument {
  id: string;
  title: string;
  content: string;
}

export default function RagPage() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<RetrievedDocument[]>([]);

  const handleIndex = async (event: FormEvent) => {
    event.preventDefault();
    await fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/rag/documents`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, content }),
    });
    setTitle('');
    setContent('');
  };

  const handleSearch = async (event: FormEvent) => {
    event.preventDefault();
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/rag/search`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, limit: 3 }),
    });
    const payload = await response.json();
    setResults(payload);
  };

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-16 text-slate-100">
      <div className="mx-auto flex max-w-5xl flex-col gap-6 rounded-3xl border border-slate-800 bg-slate-900/80 p-8 shadow-2xl shadow-cyan-950/30">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">RAG</p>
            <h1 className="mt-2 text-3xl font-semibold">Vectorized documents and semantic retrieval</h1>
          </div>
          <Link href="/" className="rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:border-cyan-500 hover:text-cyan-300">
            Back home
          </Link>
        </div>

        <form onSubmit={handleIndex} className="grid gap-4 rounded-2xl border border-slate-800 bg-slate-950/70 p-6">
          <label className="text-sm text-slate-300">
            Title
            <input value={title} onChange={(event) => setTitle(event.target.value)} className="mt-2 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100" />
          </label>
          <label className="text-sm text-slate-300">
            Content
            <textarea value={content} onChange={(event) => setContent(event.target.value)} className="mt-2 min-h-28 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100" />
          </label>
          <button type="submit" className="rounded-full bg-cyan-500 px-5 py-3 text-sm font-medium text-slate-950 transition hover:bg-cyan-400">
            Index document
          </button>
        </form>

        <form onSubmit={handleSearch} className="grid gap-4 rounded-2xl border border-slate-800 bg-slate-950/70 p-6">
          <label className="text-sm text-slate-300">
            Search query
            <input value={query} onChange={(event) => setQuery(event.target.value)} className="mt-2 w-full rounded-xl border border-slate-700 bg-slate-900 px-3 py-3 text-sm text-slate-100" />
          </label>
          <button type="submit" className="rounded-full bg-cyan-500 px-5 py-3 text-sm font-medium text-slate-950 transition hover:bg-cyan-400">
            Search context
          </button>
        </form>

        <div className="space-y-3">
          {results.map((result) => (
            <div key={result.id} className="rounded-2xl border border-slate-800 bg-slate-950/70 p-4">
              <p className="text-sm font-medium text-white">{result.title}</p>
              <p className="mt-2 text-sm text-slate-400">{result.content}</p>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
