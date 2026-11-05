# Base de Conhecimento: Fundamentos de Segurança

## Conceitos Essenciais

### Vulnerabilidade
Fraqueza em um sistema, configuração ou processo que pode ser explorada
por um agente malicioso. Exemplos: serviço desatualizado, porta exposta
sem autenticação, permissão excessiva.

### Ameaça
Agente ou evento capaz de explorar uma vulnerabilidade.
Pode ser externa (atacante na internet) ou interna (funcionário mal-intencionado).

### Risco
Combinação de probabilidade de uma ameaça se concretizar com o impacto
que causaria. Risco = Probabilidade × Impacto.

---

## Tríade CIA

| Pilar | Significado | Exemplo de violação |
|-------|-------------|---------------------|
| **Confidencialidade** | Só quem autorizado acessa | Vazamento de banco de dados |
| **Integridade** | Dados não são alterados indevidamente | Alteração de logs por atacante |
| **Disponibilidade** | Sistema acessível quando necessário | Ataque DDoS derruba serviço |

---

## Superfície de Ataque em Infraestrutura

Pontos comuns de exposição:
- Portas abertas sem necessidade (SSH, RDP, SMB expostos na internet)
- Serviços sem autenticação ou com credenciais padrão
- Softwares desatualizados com CVEs conhecidos
- Ausência de firewall ou regras permissivas demais
- Logs desabilitados ou sem monitoramento

---

## Boas Práticas

### Hardening de Servidores
- Desativar serviços desnecessários
- Alterar portas padrão de serviços críticos
- Aplicar patches de segurança regularmente
- Usar autenticação por chave SSH, nunca só por senha
- Implementar fail2ban para bloquear tentativas de força bruta

### Monitoramento
- Centralizar logs (SIEM)
- Alertas para tentativas de acesso suspeitas
- Revisão periódica de regras de firewall

### Princípio do Menor Privilégio
Cada usuário, serviço ou processo deve ter apenas as permissões
estritamente necessárias para sua função.

---

## Referência: MITRE ATT&CK (Táticas Comuns em Infraestrutura)

| Tática | Descrição | Técnica comum |
|--------|-----------|---------------|
| Initial Access | Obter acesso inicial | T1190 – Exploit Public-Facing Application |
| Credential Access | Roubar credenciais | T1110 – Brute Force |
| Discovery | Mapear o ambiente | T1046 – Network Service Scanning |
| Lateral Movement | Mover-se pela rede | T1021 – Remote Services |
| Persistence | Manter acesso | T1098 – Account Manipulation |
