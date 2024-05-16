import os
 
def cifra_de_cesar(palavra, modo):
    L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
    if modo == 'criptografar':
        palavra_cifrada = ''
        for i, letra in enumerate(palavra):
            if letra.isalpha():  
                indice = L.index(letra.lower())
                indice_cifrado = (indice + 4 * (i + 1)) % 26
                letra_cifrada = L[indice_cifrado]
                if letra.isupper():  
                    letra_cifrada = letra_cifrada.upper()
                palavra_cifrada += letra_cifrada
            else:
                palavra_cifrada += letra
        return palavra_cifrada
 
    elif modo == 'descriptografar':
        palavra_descriptografada = ''
        for i, letra in enumerate(palavra):
            if letra.isalpha():  
                indice = L.index(letra.lower())
                indice_descifrado = (indice - 4 * (i + 1)) % 26
                letra_descifrada = L[indice_descifrado]
                if letra.isupper():  
                    letra_descifrada = letra_descifrada.upper()
                palavra_descriptografada += letra_descifrada
            else:
                palavra_descriptografada += letra
        return palavra_descriptografada
 
while True:
    os.system('cls')  
    print("Escolha uma opção:")
    print("1. Criptografar")
    print("2. Descriptografar")
    print("3. Sair")
    opcao = input("Digite o número da opção desejada: ")
 
    if opcao == '1':
        os.system('cls')  
        palavra_original = input('Digite a palavra ou frase para criptografar: ')
        palavra_encriptada = cifra_de_cesar(palavra_original, 'criptografar')
        print("Palavra criptografada:", palavra_encriptada)
        input("Pressione Enter para continuar...")
    elif opcao == '2':
        os.system('cls')  
        palavra_original = input('Digite a palavra ou frase para descriptografar: ')
        palavra_desencriptada = cifra_de_cesar(palavra_original, 'descriptografar')
        print("Palavra descriptografada:", palavra_desencriptada)
        input("Pressione Enter para continuar...")
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        input("Pressione Enter para continuar...")
