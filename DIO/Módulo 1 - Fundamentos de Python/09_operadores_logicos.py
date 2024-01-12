saldo = 1000
saque = 200
limite = 100

saldo >= saque
# >>> True

saque <= limite
# >>> False

# Operador E
saldo = 1000
saque = 200
limite = 100

saldo >= saque and saque <= limite
# >>> False

# Operador OU
saldo = 1000
saque = 200
limite = 100

saldo >= saque or saque <= limite
# >>> True

# Operador de Negação
contatos_emergencia = []

not 1000 > 1500
# >>> True

not contatos_emergencia
# >>> True

not "saque 1500;"
# >>> False

not ""
# >>> True

# Parênteses
saldo = 1000
saque = 200
limite = 100
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)
# >>> True

exp_2 = (saldo >= saque and saque <= limite ) or (conta_especial and saldo >= saque)
print(exp_2)
# >>> True

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
# >>> True

# AND = para ser True tudo que ser True
# OR = para ser True apenas um tem que ser True

print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)