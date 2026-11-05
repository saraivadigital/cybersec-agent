# infrastructure-security

Skill de análise de segurança em infraestrutura para o cybersec-agent.

## O que faz

Transforma o agente num analista de segurança que, antes de qualquer sugestão,
coleta contexto, avalia impacto, probabilidade e severidade, referencia técnicas
do MITRE ATT&CK e orienta a correção passo a passo.

## Quando o agente usa esta skill

Quando o usuário descreve um cenário de infraestrutura com possível exposição
ou vulnerabilidade: servidor exposto, serviço sem autenticação, porta aberta,
configuração insegura, etc.

## Exemplo de uso

**Usuário:**
> Tenho um servidor Ubuntu 22.04 de laboratório com SSH na porta 22 exposto
> na internet, sem fail2ban e com login por senha habilitado.

**Agente (com a skill):**
> Antes de analisar, preciso entender melhor o contexto:
> 1. Este servidor está em produção ou é exclusivamente para laboratório?
> 2. Existe alguma regra de firewall limitando o acesso à porta 22?
> 3. O login root via SSH está habilitado?

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `SKILL.md` | Roteiro que o agente segue ao usar esta skill |
| `README.md` | Este arquivo — explicação para pessoas |
