# Exemplo - for

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = "")
else:
    print() # adiciona uma quebra de linha.
    print("Executa no final do laço.")


# Exemplo - range

# range(stop) -> range object
# range(star, stop[, step]) -> range object

list(range(4))
# >>> [0, 1, 2, 3]

# range com for
for numero in range(0, 11):
    print(numero, end=" ")

# >>> 0 1 2 3 4 5 6 7 8 9 10
    

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

# >>> 0 5 10 15 20 25 30 35 40 45 50
    
# Comando While

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair) \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")


# Comando break

while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

for numero in range(100):

    if numero == 12:
        break

    print(numero, end=" ")

for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")