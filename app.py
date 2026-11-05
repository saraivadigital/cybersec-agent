# ================================================================
# VERSÃO VULNERÁVEL — apenas para fins educacionais
# Demonstra SQL Injection por concatenação de string
# ================================================================

import sqlite3

def login_vulneravel(usuario, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # VULNERÁVEL: entrada do usuário concatenada diretamente na query
    query = "SELECT * FROM usuarios WHERE usuario='" + usuario + "' AND senha='" + senha + "'"
    print(f"[DEBUG] Query executada: {query}")

    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


# ================================================================
# VERSÃO CORRIGIDA — consulta parametrizada
# ================================================================

def login_seguro(usuario, senha):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # SEGURO: parâmetros separados da query — SQL Injection impossível
    query = "SELECT * FROM usuarios WHERE usuario=? AND senha=?"
    cursor.execute(query, (usuario, senha))

    resultado = cursor.fetchone()
    conn.close()
    return resultado is not None


# ================================================================
# Exemplo de exploração (apenas demonstração)
# ================================================================

# Com login_vulneravel, isso retorna True sem senha válida:
# login_vulneravel("admin' --", "qualquer_coisa")
# Query gerada: SELECT * FROM usuarios WHERE usuario='admin' --' AND senha='...'
# O -- comenta o resto, ignorando a verificação de senha

# Com login_seguro, o mesmo input é tratado como texto literal — sem exploração possível
