import sqlite3


# Parte 1 — Criar o banco de dados e conexão

conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

print("✅ Conexão com o banco de dados 'escola.db' criada com sucesso!")


# Parte 2 — Criar a tabela 'alunos'

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT UNIQUE NOT NULL
)
""")
print("✅ Tabela 'alunos' criada (ou já existia).")



# Parte 3 — Inserir registros de exemplo

def inserir_aluno(nome, idade, email):
    cursor.execute("INSERT INTO alunos (nome, idade, email) VALUES (?, ?, ?)", (nome, idade, email))
    conexao.commit()
    print(f" Aluno '{nome}' inserido com sucesso!")


# Inserindo alguns registros de exemplo

inserir_aluno("Hercilio Oliveira", 20, "hercilioalencaro@gmail.com")
inserir_aluno("Hercilio Oliveira", 22, "hercilioalencaro@gmail.com")
inserir_aluno("Hercilio Oliveira", 19, "hercilioalencaro@gmail.com")



# Parte 4 — Listar todos os alunos

def listar_alunos():
    print("\n Lista de alunos cadastrados:")
    for aluno in cursor.execute("SELECT * FROM alunos"):
        print(aluno)


listar_alunos()



# Parte 5 — Buscar aluno por ID

def buscar_aluno_por_id(aluno_id):
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
    resultado = cursor.fetchone()
    if resultado:
        print(f"\n Aluno encontrado: {resultado}")
    else:
        print(f"\n Nenhum aluno encontrado com ID {aluno_id}.")


buscar_aluno_por_id(2)



#  Parte 6 — Atualizar informações de um aluno

def atualizar_aluno(aluno_id, novo_nome, nova_idade, novo_email):
    cursor.execute("""
        UPDATE alunos
        SET nome = ?, idade = ?, email = ?
        WHERE id = ?
    """, (novo_nome, nova_idade, novo_email, aluno_id))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"\n Aluno ID {aluno_id} atualizado com sucesso!")
        buscar_aluno_por_id(aluno_id)
    else:
        print(f"\n Nenhum aluno encontrado com ID {aluno_id}.")


# Exemplo de atualização
atualizar_aluno(1, "Hercilio Oliveira", 21, "hercilioalencaro@gmail.com")


def deletar_aluno(aluno_id):
    cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"\n Aluno ID {aluno_id} deletado com sucesso!")
    else:
        print(f"\n Nenhum aluno encontrado com ID {aluno_id}.")

    listar_alunos()


# Exemplo de exclusão

deletar_aluno(3)


conexao.close()
print("\n Conexão com o banco de dados encerrada.")