"""
main.py — Interface de texto (menu) do sistema.

Este arquivo so conversa com o usuario. Toda regra de banco fica nos modulos
database.py, crud_aluno.py e crud_disciplina.py.

O menu de ALUNOS ja tem as opcoes 1 e 2 prontas. Use-as como modelo.
"""

from database import criar_tabelas
from crud_aluno import (inserir_aluno, listar_alunos, buscar_aluno_por_id,
                        atualizar_aluno, excluir_aluno)
from crud_disciplina import (inserir_disciplina, listar_disciplinas,
                             buscar_disciplina_por_id, atualizar_disciplina,
                             excluir_disciplina)


def ler_inteiro(mensagem):
    """Le um numero inteiro do teclado, insistindo ate o usuario acertar."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("  Valor invalido. Digite um numero inteiro.")


def menu_alunos():
    while True:
        print("""
--- ALUNOS ---
1) Cadastrar   2) Listar   3) Alterar   4) Excluir   0) Voltar""")
        opcao = input("Opcao: ").strip()

        if opcao == "1":                                   # PRONTO
            matricula = input("Matricula: ").strip()
            nome = input("Nome: ").strip()
            email = input("E-mail: ").strip()
            nascimento = input("Nascimento (AAAA-MM-DD): ").strip()
            if not matricula or not nome:
                print(">> Matricula e nome sao obrigatorios.")
                continue
            novo_id = inserir_aluno(matricula, nome, email, nascimento)
            if novo_id is None:
                print(">> Ja existe aluno com essa matricula.")
            else:
                print(">> Aluno cadastrado com id", novo_id)

        elif opcao == "2":                                 # PRONTO
            alunos = listar_alunos()
            if not alunos:
                print(">> Nenhum aluno cadastrado.")
            for a in alunos:
                print(f"  [{a[0]}] {a[1]} - {a[2]} | {a[3]} | {a[4]}")

        elif opcao == "3":
            # 7: pedir o id, buscar o aluno, avisar se nao existir,
            # ler os novos dados e chamar atualizar_aluno().
            id_aluno = ler_inteiro("digite o id do aluno: ")
            aluno = buscar_aluno_por_id(id_aluno)
            if not aluno:
                print(">> Aluno nao encontrado.")
            else:
                print(f">> Editando: {aluno[2]} (Matricula: {aluno[1]})")
                nome = input("Novo Nome: ").strip()
                email = input("Novo E-mail: ").strip()
                nascimento = input("Novo Nascimento (AAAA-MM-DD): ").strip()

            if not nome:
                print(">> O nome nao pode ficar vazio.")
                continue

            sucesso = atualizar_aluno(id_aluno, nome, email, nascimento)
            if sucesso:
                print(">> Aluno atualizado com sucesso.")
            else:
                print(">> Falha ao atualizar o aluno.")

        elif opcao == "4":
            # 8: pedir o id e chamar excluir_aluno(), tratando o False.
            id_aluno = ler_inteiro("digite o id do aluno para excluir: ")
            sucesso = excluir_aluno(id_aluno)
            if sucesso:
                print(">> Aluno excluido com sucesso.")
            else:
                print(">> Nao foi possivel excluir o aluno.")

        elif opcao == "0":
            return
        else:
            print(">> Opcao invalida.")


def menu_disciplinas():
    # 9: espelhe menu_alunos() para as disciplinas.
    while True:
        print("""
--- DISCIPLINA ---
1) Cadastrar   2) Listar   3) Alterar   4) Excluir   0) Voltar""")
        opcao = input("Opcao: ").strip()
        if opcao == "1":                                   # PRONTO
            codigo = input("Código: ").strip()
            nome = input("Nome: ").strip()
            carga_horaria = ler_inteiro("Carga Horária: ")
            periodo = ler_inteiro("Período: ")

            if not codigo or not nome or not carga_horaria:
                print(">> Codigo, nome e carga horária sao obrigatorios.")
                continue

            nova_disciplina = inserir_disciplina(codigo, nome, carga_horaria, periodo)
            if nova_disciplina is None:
                print(">> Ja existe disciplina com esse codigo.")
            else:
                print(">> Disciplina cadastrada com id", nova_disciplina)


        elif opcao == "2":
            disciplinas = listar_disciplinas()
            if not disciplinas:
                print(">> Nenhuma disciplina cadastrada.")
            for a in disciplinas:
                print(f"  [{a[0]}] {a[1]} - {a[2]} | {a[3]} | {a[4]}")

        elif opcao == "3":
            # 7: pedir o id, buscar a disciplina, avisar se nao existir,
            # ler os novos dados e chamar atualizar_disciplina().
            id_disciplina = ler_inteiro("digite o id da disciplina: ")
            disciplina = buscar_disciplina_por_id(id_disciplina)
            if not disciplina:
                print(">> Disciplina nao encontrado.")
            else:
                print(f">> Editando: {disciplina[2]} (Codigo: {disciplina[1]})")
                nome = input("Novo Nome: ").strip()
                carga_horaria = ler_inteiro("Nova Carga Horaria: ")
                periodo = ler_inteiro("Novo Periodo: ")

            if not nome:
                print(">> O nome nao pode ficar vazio.")
                continue

            sucesso = atualizar_disciplina(id_disciplina, nome, carga_horaria, periodo)
            if sucesso:
                print(">> Disciplina atualizada com sucesso.")
            else:
                print(">> Falha ao atualizar disciplina.")

        elif opcao == "4":
            # 8: pedir o id e chamar excluir_disciplina(), tratando o False.
            id_disciplina = ler_inteiro("digite o id do disciplina para excluir: ")
            sucesso = excluir_disciplina(id_disciplina)
            if sucesso:
                print(">> Disciplina excluido com sucesso.")
            else:
                print(">> Nao foi possivel excluir a disciplina.")

        elif opcao == "0":
            return
        else:
            print(">> Opcao invalida.")
        

def main():
    criar_tabelas()
    while True:
        print("""
=== SISTEMA DE REGISTRO ACADEMICO ===
1) Alunos
2) Disciplinas
0) Sair""")
        opcao = input("Opcao: ").strip()
        if opcao == "1":
            menu_alunos()
        elif opcao == "2":
            menu_disciplinas()
        elif opcao == "0":
            print("Ate logo!")
            break
        else:
            print(">> Opcao invalida.")


if __name__ == "__main__":
    main()
