# Tuitando
T = input()
tamanho = len(T)

if(tamanho <= 140):
    print("TWEET")
else:
    print("MUTE")
    

T = "RT @TheEllenShow: If only Bradley's arm was longer. Best photo ever. #oscars pic.twitter.com/C9U5NOtGap"

# Mês do ano

month = input()

months_dict = {
  
    "1" : "January",
      
    "2" : "February",
      
    "3" : "March",
      
    "4" : "April",
      
    "5" : "May",
    
    "6" : "June",
      
    "7" : "July",
      
    "8" : "August",
      
    "9" : "September",
    
    "10" : "October",
      
    "11" : "November",
      
    "12" : "December"
}

if month > "0" <= "12":
  print(months_dict[month])
else:
  print("Inexistent month")

# Encaixa ou não?
  
# Entrada do número de casos de teste
n = int(input("Digite o número de casos de teste: "))

def encaixa(a, b):
    # Verifica se o tamanho de B é maior que o tamanho de A
    if len(b) > len(a):
        return "nao encaixa"

    # Compara os últimos dígitos de A e B
    if a[-len(b):] == b:
        return "encaixa"
    else:
        return "nao encaixa"

# Loop através dos casos de teste
for _ in range(n):
    # Entrada dos valores A e B
    a, b = input().split()

    # Chama a função e imprime o resultado
    resultado = encaixa(a, b)
    print(resultado)