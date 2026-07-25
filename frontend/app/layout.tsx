import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'LPX-NEXUS',
  description: 'A platform for building software, automations and content with AI.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
