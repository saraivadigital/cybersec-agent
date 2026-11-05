# 🛡️ cybersec-agent

Especialização do DIO Agent voltada para análise de segurança em infraestrutura.
O agente aprende através de arquivos — nenhum modelo é treinado.
Todo o comportamento vem do que está escrito na skill, no conhecimento e na persona.

> ⚠️ **Aviso Legal:** Os exemplos e cenários deste repositório são exclusivamente
> educacionais. Jamais aplique técnicas de segurança ofensiva em sistemas
> sem autorização expressa.

---

## 🎯 Especialização

O cybersec-agent foi especializado como um **analista de segurança em infraestrutura**
que, em vez de responder direto, sempre:

1. Coleta contexto antes de qualquer sugestão
2. Avalia impacto, probabilidade e severidade
3. Referencia técnicas do MITRE ATT&CK
4. Orienta a correção em etapas práticas

---

## 📁 Arquivos Criados ou Alterados

| Arquivo | O que faz |
|---------|-----------|
| `skills/infrastructure-security/SKILL.md` | Roteiro que o agente segue ao analisar cenários de infraestrutura |
| `skills/infrastructure-security/README.md` | Explica a skill para pessoas |
| `agent/knowledge/security-basics.md` | Base de conhecimento: vulnerabilidade, ameaça, risco, tríade CIA, MITRE ATT&CK |
| `agent/persona.md` | Define o comportamento e tom do agente |
| `agent/AGENTS.md` | Registra a skill na tabela do agente |
| `app.py` | Código com versão vulnerável (SQL Injection) e versão corrigida |

---

## 🚀 Como Rodar

```bash
# 1. Clone o repositório base do DIO Agent
git clone https://github.com/digitalinnovationone/dio-agent
cd dio-agent

# 2. Copie os arquivos deste repositório para dentro do dio-agent
# (substitua os arquivos existentes pelos desta especialização)

# 3. Instale o Hermes conforme documentação do repositório base

# 4. Abra o terminal NA PASTA DO PROJETO e rode o Hermes
# ⚠️ Abrir em outra pasta faz o agente não encontrar os arquivos
```

---

## 🧪 Cenário de Teste

Descreva este cenário para o agente e observe como ele reage:

> *"Tenho um servidor Ubuntu 22.04 de laboratório com SSH na porta 22
> exposto na internet, sem fail2ban e com login por senha habilitado."*

O agente especializado deve **perguntar o contexto antes de agir**,
ao contrário de um chat genérico que responderia com comandos imediatamente.

---

## ✅ Melhoria Escolhida

**Formato estruturado de saída** — a skill define um template fixo de resposta
(contexto coletado → vulnerabilidade → MITRE ATT&CK → avaliação de risco →
mitigação), garantindo que toda análise seja comparável e rastreável.
Isso é especialmente útil em fluxos de DevSecOps, onde a consistência
do relatório importa tanto quanto o conteúdo.

---

## 🔗 Referências

- [DIO Agent – Repositório Base](https://github.com/digitalinnovationone/dio-agent)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Kali Linux](https://www.kali.org/)
