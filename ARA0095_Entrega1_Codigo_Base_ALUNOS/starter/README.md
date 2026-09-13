# Sistema de Registro Academico — Entrega 1

> Preencha este arquivo. Ele vale nota (item 5 da rubrica).

## Identificacao

- **Disciplina:** ARA0095 — Desenvolvimento Rapido de Aplicacoes em Python
- **Turma:**
- **Integrantes do grupo:** (nome completo e matricula)
  1.José Matheus Nagata Kulibaba/202502195877
  2.
  3.

## Como executar

```bash
python database.py   # cria o banco e as tabelas
python seed.py       # carrega dados de exemplo (opcional)
python main.py       # abre o menu do sistema
```

## Modelo de dados

Descreva em poucas linhas as tabelas criadas, as chaves primarias, as chaves
estrangeiras e por que a tabela `inscricao` foi necessaria.

tabela aluno: id chave primaria, matricula com auto incremento.
tabela disciplina: id chave primaria, codigo unico.
tabela inscricao: tabela como objetivo de relacionar n para n duas tabelas aluno e disciplina onde o aluno pode cursar varias disciplinas e uma disciplina pode conter varios alunos.
id chave primaria, aluno_id referenciando aluno(id) e disciplina_id referenciando disciplina(id)


## Decisoes que tomamos

Ex.: por que `data_nascimento` e TEXT; o que acontece ao tentar excluir um
aluno que tem inscricoes; o que o grupo decidiu fazer nesse caso.

exclusao dos alunos com inscicoes que usa o PRAGMA ON, O sqlite rejeita a delecao dos alunos que tenham inscicoes.

nos comandos de insert, update e delete usado o try except, se der certo da o commit() ou se der errado rollback()

## O que ficou faltando

Seja honesto. Um item pendente declarado vale mais que um bug escondido.

|
