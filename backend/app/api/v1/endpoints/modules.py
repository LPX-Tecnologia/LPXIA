from fastapi import APIRouter

router = APIRouter(prefix="/modules", tags=["modules"])

MODULES = [
    {"id": 11, "slug": "prompt-engine", "name": "Prompt Engine", "focus": "Templates, Personas, Cadeias de prompts, Contexto automático"},
    {"id": 12, "slug": "developer-agent", "name": "Agente Desenvolvedor", "focus": "HTML, CSS, JS, React, Next"},
    {"id": 13, "slug": "backend-agent", "name": "Agente Backend", "focus": "Python, FastAPI, Node, APIs"},
    {"id": 14, "slug": "mobile-agent", "name": "Agente Mobile", "focus": "Flutter, React Native, Kotlin, Swift"},
    {"id": 15, "slug": "designer-agent", "name": "Agente Designer", "focus": "Logos, UI, UX, Banners"},
    {"id": 16, "slug": "video-agent", "name": "Agente Vídeo", "focus": "Roteiro, Narração, Legendas, Storyboard"},
    {"id": 17, "slug": "marketing-agent", "name": "Agente Marketing", "focus": "SEO, Blog, Landing Pages, Social Media"},
    {"id": 18, "slug": "qa-agent", "name": "Agente QA", "focus": "Testes, Cobertura, Correções"},
    {"id": 19, "slug": "devops-agent", "name": "Agente DevOps", "focus": "Docker, Deploy, VPS, CI/CD"},
    {"id": 20, "slug": "editor-tool", "name": "Editor", "focus": "Monaco, Explorer, Arquivos, Git"},
    {"id": 21, "slug": "terminal-tool", "name": "Terminal", "focus": "Shell, Logs, Execução"},
    {"id": 22, "slug": "manager-tool", "name": "Gerenciador", "focus": "Projetos, Pastas, Arquivos"},
    {"id": 23, "slug": "executor-tool", "name": "Executor", "focus": "Python, Node, Docker"},
    {"id": 24, "slug": "git-tool", "name": "Git", "focus": "Clone, Commit, Push, Branch"},
    {"id": 25, "slug": "feedback-learning", "name": "Feedback", "focus": "Gostei, Não gostei, Correções"},
    {"id": 26, "slug": "profiles-learning", "name": "Perfis", "focus": "Preferências, Estilo, Idiomas"},
    {"id": 27, "slug": "knowledge-learning", "name": "Conhecimento", "focus": "Indexação, Organização, Busca"},
    {"id": 28, "slug": "workflows-automation", "name": "Workflows", "focus": "Fluxos, Agendamentos, Triggers"},
    {"id": 29, "slug": "api-automation", "name": "API", "focus": "REST, Webhooks, SDK"},
    {"id": 30, "slug": "plugins-automation", "name": "Plugins", "focus": "Instalação, Marketplace"},
    {"id": 31, "slug": "financial-production", "name": "Sistema Financeiro", "focus": "Planos, Assinaturas, Cobrança"},
    {"id": 32, "slug": "admin-production", "name": "Admin", "focus": "Usuários, Logs, Monitoramento"},
    {"id": 33, "slug": "monitoring-production", "name": "Monitoramento", "focus": "CPU, RAM, Banco, IA"},
    {"id": 34, "slug": "security-production", "name": "Segurança", "focus": "Rate Limit, Auditoria, Criptografia"},
    {"id": 35, "slug": "deploy-production", "name": "Deploy", "focus": "VPS, Docker, Kubernetes (opcional)"},
    {"id": 36, "slug": "multiagents-advanced", "name": "Multiagentes", "focus": "Coordenação entre agentes"},
    {"id": 37, "slug": "planner-advanced", "name": "Planejador", "focus": "Planejamento estratégico e execução"},
    {"id": 38, "slug": "smart-executor-advanced", "name": "Executor Inteligente", "focus": "Execução guiada por contexto"},
    {"id": 39, "slug": "self-evaluation-advanced", "name": "Autoavaliação", "focus": "Avaliação de qualidade e risco"},
    {"id": 40, "slug": "global-memory-advanced", "name": "Memória Global", "focus": "Memória compartilhada entre projetos"},
    {"id": 41, "slug": "knowledge-base-advanced", "name": "Base de Conhecimento", "focus": "Base documental e semântica"},
    {"id": 42, "slug": "automatic-docs-advanced", "name": "Documentação Automática", "focus": "Docs e guias gerados automaticamente"},
    {"id": 43, "slug": "site-generator-advanced", "name": "Gerador de Sites", "focus": "Landing pages e sites completos"},
    {"id": 44, "slug": "app-generator-advanced", "name": "Gerador de Apps", "focus": "Aplicativos web e mobile"},
    {"id": 45, "slug": "api-generator-advanced", "name": "Gerador de APIs", "focus": "Backends e integrações"},
    {"id": 46, "slug": "database-generator-advanced", "name": "Gerador de Bancos", "focus": "Schema, migrations e seeds"},
    {"id": 47, "slug": "video-generator-advanced", "name": "Gerador de Vídeos", "focus": "Storyboards e roteiros automáticos"},
    {"id": 48, "slug": "image-generator-advanced", "name": "Gerador de Imagens", "focus": "Assets visuais e branding"},
    {"id": 49, "slug": "marketplace-advanced", "name": "Marketplace", "focus": "Disponibilização de plugins e produtos"},
    {"id": 50, "slug": "release-final", "name": "Release Final v1.0", "focus": "Testes finais, documentação e deploy"},
]


@router.get("/")
def list_modules() -> list[dict[str, object]]:
    return MODULES
