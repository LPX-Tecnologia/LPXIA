'use client';

import { useMemo, useState } from 'react';
import Link from 'next/link';

interface ChatMessage {
  role: string;
  content: string;
}

interface ChatResponse {
  session_id: string;
  reply: string;
  history: ChatMessage[];
}

export default function ChatPage() {
  const [sessionId, setSessionId] = useState('default');
  const [input, setInput] = useState('');
  const [history, setHistory] = useState<ChatMessage[]>([]);
  const [status, setStatus] = useState('Ready');

  const sessionLabel = useMemo(() => `Session ${sessionId}`, [sessionId]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    setStatus('Sending...');
    const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL ?? 'http://localhost:8000'}/api/v1/chat/send`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ session_id: sessionId, message: input }),
    });

    const data: ChatResponse = await response.json();
    setSessionId(data.session_id);
    setHistory(data.history);
    setInput('');
    setStatus('Delivered');
  };

  return (
    <main className="min-h-screen bg-slate-950 px-6 py-16 text-slate-100">
      <div className="mx-auto flex max-w-5xl flex-col gap-6 rounded-3xl border border-slate-800 bg-slate-900/80 p-8 shadow-2xl shadow-cyan-950/30">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Chat</p>
            <h1 className="mt-2 text-3xl font-semibold">Conversational AI workspace</h1>
          </div>
          <Link href="/" className="rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:border-cyan-500 hover:text-cyan-300">
            Back home
          </Link>
        </div>

        <div className="rounded-2xl border border-slate-800 bg-slate-950/70 p-4">
          <div className="mb-3 flex items-center justify-between text-sm text-slate-400">
            <span>{sessionLabel}</span>
            <span>{status}</span>
          </div>
          <div className="space-y-3">
            {history.length === 0 ? (
              <div className="rounded-xl border border-dashed border-slate-700 p-4 text-sm text-slate-500">No messages yet. Start the conversation.</div>
            ) : (
              history.map((message, index) => (
                <div key={`${message.role}-${index}`} className={`rounded-xl px-4 py-3 ${message.role === 'assistant' ? 'bg-cyan-500/10 text-cyan-100' : 'bg-slate-800/80 text-slate-200'}`}>
                  <p className="text-xs uppercase tracking-[0.3em] text-slate-500">{message.role}</p>
                  <p className="mt-2 text-sm">{message.content}</p>
                </div>
              ))
            )}
          </div>
        </div>

        <div className="flex gap-3">
          <input
            value={input}
            onChange={(event) => setInput(event.target.value)}
            onKeyDown={(event) => {
              if (event.key === 'Enter') {
                void sendMessage();
              }
            }}
            className="flex-1 rounded-full border border-slate-700 bg-slate-950 px-4 py-3 text-sm text-slate-100 outline-none ring-0"
            placeholder="Type a message..."
          />
          <button
            onClick={() => void sendMessage()}
            className="rounded-full bg-cyan-500 px-5 py-3 text-sm font-medium text-slate-950 transition hover:bg-cyan-400"
          >
            Send
          </button>
        </div>
      </div>
    </main>
  );
}
