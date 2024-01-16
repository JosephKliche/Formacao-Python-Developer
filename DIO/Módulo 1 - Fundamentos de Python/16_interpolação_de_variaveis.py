# Old style %

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." %(nome, idade, profissao, linguagem))

# >>> Olá, me chamo Guilher. Eu tenho 28 anos de idade, trabalho como Programador e estou matriulado no curso de Python.

# Método Format

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}." .format(nome, idade, profissao, linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}." .format(nome, idade, profissao, linguagem))

# Método f-string

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
# >>> "Valor de PI: 3.14"

print(f"Valor de PI: {PI:10.2f}")
# >>> "Valor de PI:           3.14"