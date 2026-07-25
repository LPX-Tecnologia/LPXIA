'use client';

import Link from 'next/link';

const modules = [
  { id: 11, name: 'Prompt Engine', focus: 'Templates, personas e contexto automático' },
  { id: 12, name: 'Agente Desenvolvedor', focus: 'HTML, CSS, JS, React, Next' },
  { id: 13, name: 'Agente Backend', focus: 'Python, FastAPI, Node, APIs' },
  { id: 14, name: 'Agente Mobile', focus: 'Flutter, React Native, Kotlin, Swift' },
  { id: 15, name: 'Agente Designer', focus: 'Logos, UI, UX, Banners' },
  { id: 16, name: 'Agente Vídeo', focus: 'Roteiro, Narração, Legendas, Storyboard' },
  { id: 17, name: 'Agente Marketing', focus: 'SEO, Blog, Landing Pages, Social Media' },
  { id: 18, name: 'Agente QA', focus: 'Testes, cobertura e correções' },
  { id: 19, name: 'Agente DevOps', focus: 'Docker, deploy e CI/CD' },
  { id: 20, name: 'Editor', focus: 'Monaco, Explorer, Arquivos, Git' },
  { id: 21, name: 'Terminal', focus: 'Shell, logs e execução' },
  { id: 22, name: 'Gerenciador', focus: 'Projetos, pastas e arquivos' },
  { id: 23, name: 'Executor', focus: 'Python, Node e Docker' },
  { id: 24, name: 'Git', focus: 'Clone, commit, push e branch' },
  { id: 25, name: 'Feedback', focus: 'Gostei, não gostei e correções' },
  { id: 26, name: 'Perfis', focus: 'Preferências, estilo e idiomas' },
  { id: 27, name: 'Conhecimento', focus: 'Indexação e organização' },
  { id: 28, name: 'Workflows', focus: 'Fluxos, agendamentos e triggers' },
  { id: 29, name: 'API', focus: 'REST, webhooks e SDK' },
  { id: 30, name: 'Plugins', focus: 'Instalação e marketplace' },
  { id: 31, name: 'Sistema Financeiro', focus: 'Planos e assinaturas' },
  { id: 32, name: 'Admin', focus: 'Usuários, logs e monitoramento' },
  { id: 33, name: 'Monitoramento', focus: 'CPU, RAM, banco e IA' },
  { id: 34, name: 'Segurança', focus: 'Rate limit e auditoria' },
  { id: 35, name: 'Deploy', focus: 'VPS, Docker e Kubernetes' },
  { id: 36, name: 'Multiagentes', focus: 'Coordenação entre agentes' },
  { id: 37, name: 'Planejador', focus: 'Planejamento estratégico' },
  { id: 38, name: 'Executor Inteligente', focus: 'Execução guiada por contexto' },
  { id: 39, name: 'Autoavaliação', focus: 'Qualidade e risco' },
  { id: 40, name: 'Memória Global', focus: 'Memória compartilhada' },
  { id: 41, name: 'Base de Conhecimento', focus: 'Base documental e semântica' },
  { id: 42, name: 'Documentação Automática', focus: 'Docs geradas automaticamente' },
  { id: 43, name: 'Gerador de Sites', focus: 'Landing pages e sites' },
  { id: 44, name: 'Gerador de Apps', focus: 'Aplicativos web e mobile' },
  { id: 45, name: 'Gerador de APIs', focus: 'Backends e integrações' },
  { id: 46, name: 'Gerador de Bancos', focus: 'Schemas e migrations' },
  { id: 47, name: 'Gerador de Vídeos', focus: 'Roteiros e storyboards' },
  { id: 48, name: 'Gerador de Imagens', focus: 'Assets e branding' },
  { id: 49, name: 'Marketplace', focus: 'Plugins e produtos' },
  { id: 50, name: 'Release Final v1.0', focus: 'Testes finais e CI/CD' },
];

export default function ModulesPage() {
  return (
    <main className="min-h-screen bg-slate-950 px-6 py-16 text-slate-100">
      <div className="mx-auto max-w-6xl rounded-3xl border border-slate-800 bg-slate-900/80 p-8 shadow-2xl shadow-cyan-950/30">
        <div className="flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.3em] text-cyan-400">Modules</p>
            <h1 className="mt-2 text-3xl font-semibold">Escopo completo do LPX-NEXUS</h1>
          </div>
          <Link href="/" className="rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:border-cyan-500 hover:text-cyan-300">
            Back home
          </Link>
        </div>

        <div className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-3">
          {modules.map((module) => (
            <div key={module.id} className="rounded-2xl border border-slate-800 bg-slate-950/70 p-4">
              <p className="text-sm text-cyan-400">Módulo {module.id}</p>
              <h2 className="mt-2 text-lg font-semibold text-white">{module.name}</h2>
              <p className="mt-2 text-sm text-slate-400">{module.focus}</p>
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}
