"""
crud_disciplina.py — Operacoes CRUD da entidade Disciplina.

TODO 6: implemente as cinco funcoes abaixo, espelhando crud_aluno.py.
Se a estrutura ficar identica, voce fez certo: previsibilidade e reuso sao
principios do RAD.
"""

import sqlite3

from database import conectar


def inserir_disciplina(codigo, nome, carga_horaria, periodo):
    """Devolve o id gerado ou None se o codigo ja existir."""
    conexao = conectar()
    cursor = conexao.cursor()
    sql = """INSERT INTO disciplina (codigo, nome, carga_horaria, periodo)
                VALUES (?, ?, ?, ?)"""
    valores = (codigo, nome, carga_horaria, periodo)
    try:
        cursor.execute(sql, valores)
        conexao.commit()
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        conexao.rollback()
        return None
    finally:
        cursor.close()
        conexao.close()


def listar_disciplinas():
    """Devolve a lista de todas as disciplinas, ordenada por codigo."""

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""SELECT id, codigo, nome, carga_horaria, periodo
                        FROM disciplina ORDER BY nome""")
    alunos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return alunos
    


def buscar_disciplina_por_id(id_disciplina):
    """Devolve uma tupla, ou None se nao existir."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""SELECT id, codigo, nome, carga_horaria, periodo
                      FROM disciplina WHERE id = ?""", (id_disciplina,))
    alunos = cursor.fetchone()
    cursor.close()
    conexao.close()
    return alunos


def atualizar_disciplina(id_disciplina, nome, carga_horaria, periodo):
    """Devolve True se alguma linha foi alterada."""
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""UPDATE disciplina SET nome = ?, carga_horaria = ?, periodo = ?
                            WHERE id = ? """, (nome, carga_horaria, periodo, id_disciplina,))
        linhas = cursor.rowcount

    except sqlite3.IntegrityError:
        conexao.rollback()
        return False

    finally:
        conexao.commit()
        cursor.close()
        conexao.close()
        return linhas > 0
    

def excluir_disciplina(id_disciplina):
    """Devolve True se alguma linha foi removida."""
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""DELETE FROM disciplina where id = ?""",(id_disciplina,))
        removido = cursor.rowcount > 0
        conexao.commit()
        return removido
    except sqlite3.IntegrityError:
        conexao.rollback()
        return False
    
    finally:
        conexao.commit()
        cursor.close()
        conexao.close()
