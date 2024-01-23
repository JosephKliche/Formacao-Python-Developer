# Daenerys dos Dothraki

C = int(input())  # Solicita o número de casos de teste

for i in range(C):  # Loop para cada caso de teste
    N = int(input())  # Solicita um número N para cada caso

    # Verifica a condição e imprime a mensagem correspondente
    if N >= 8001:
        print('Mais de 8000!')
    else:
        print('Inseto!')


# Promoção de refrigerantes
        
T = int(input())  # Lê o número de casos de teste
while T > 0:
    T -= 1
    N, K = map(int, input().split())  # Lê os valores N e K para cada caso de teste
    total = N % K + N // K  # Calcula a soma de N % K e N // K
    print(total)  # Imprime o resultado da soma


# Características do animal
    
# Solicita as características do animal
a = input()
b = input()
c = input()

# Verifica se o animal é vertebrado
if a == 'vertebrado':
    # Verifica as características específicas do animal vertebrado
    if b == 'ave' and c == 'carnivoro':
        print('aguia')
    elif b == 'ave' and c == 'onivoro':
        print('pomba')
    elif b == 'mamifero' and c == 'onivoro':
        print('homem')
    elif b == 'mamifero' and c =='herbivoro':
        print('vaca')
# Se o animal não é vertebrado, verifica se é invertebrado
elif a == 'invertebrado':
    # Verifica as características específicas do animal invertebrado
    if b == 'inseto' and c == 'hematofago':
        print('pulga')
    elif b == 'inseto' and c == 'herbivoro':
        print('lagarta')
    elif b == 'anelideo' and c == 'hematofago':
        print('sanguessuga')
    elif b == 'anelideo' and c =='onivoro':
        print('minhoca')