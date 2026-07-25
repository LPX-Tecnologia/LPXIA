import Link from 'next/link';

export function Navbar() {
  return (
    <nav className="flex items-center justify-between rounded-full border border-slate-800 bg-slate-900/70 px-4 py-3 text-sm text-slate-300 backdrop-blur">
      <Link href="/" className="font-semibold text-white">
        LPX-NEXUS
      </Link>
      <div className="flex items-center gap-4">
        <Link href="/dashboard" className="hover:text-cyan-300">
          Dashboard
        </Link>
        <Link href="/login" className="rounded-full bg-cyan-500 px-3 py-2 font-medium text-slate-950 hover:bg-cyan-400">
          Login
        </Link>
      </div>
    </nav>
  );
}
