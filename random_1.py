import random

numero_secreto = random.randint(1, 10)

tentativas = 0

while True:
    # Pedir para o usuário adivinhar
    tentativa = int(input("Adivinhe o número (entre 1 e 10): "))
    
    # Incrementar o número de tentativas
    tentativas += 1
    
    # Verificar se a tentativa está correta
    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        print("Número de tentativas:", tentativas)
        break
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")