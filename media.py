#Média do Project Checkpoint Challenge & Feedbacks = Média
#3CPs (<nota retirada)
#(Entregavel1+Entregavel2+Cp1+Cp2) == 40% da notaS

# Cada professor disponibilizará 4 tarefas por disciplina (2 obrigatórias + 2 opcionais):
#As tarefas obrigatórias da disciplina valem
#A média de todas as tarefas opcionais que o aluno escolheu vale 20% (0 a 20).

import os

def main():
    os.system('cls')
    app_name()
    mediacp1 = media_checkpoint()
    chl1 = media_challenge()
    gs1 = media_gs()
    media1s = media_1s(mediacp1, chl1, gs1)  
    input('\nPresseine qualquer bottão: \n')
    os.system('cls')
    mediacp2 = media_checkpoint_2()
    chl2 = media_challenge_2()
    gs2 = media_gs_2()
    media2s = media_2s(mediacp2, chl2, gs2)  
    input('\nPresseine qualquer bottão: \n')
    os.system('cls')
    media_anual(media1s, media2s) 

def app_name():
    print('𝑵𝑶𝑻𝑨𝑺 𝑪𝑨𝑳𝑪𝑼𝑳𝑨𝑻𝑶𝑹')

def media_checkpoint():
    cp1 = float(input('Quanto você tirou no CheckPoint 1: \n'))
    cp2 = float(input('Quanto você tirou no CheckPoint 2: \n'))
    cp3 = float(input('Quanto você tirou no CheckPoint 3: \n'))
    notascp = [cp1, cp2, cp3]
    os.system('cls')
    notascp.sort(reverse=True)
    mediacp1 = sum(notascp[:2]) / 2
    print('As duas maiores notas são:', notascp[0], 'e', notascp[1])
    print('A média das duas maiores notas é:', mediacp1)
    return mediacp1

def media_checkpoint_2():
    cp1_2 = float(input('Quanto você tirou no CheckPoint 1: \n'))
    cp2_2 = float(input('Quanto você tirou no CheckPoint 2: \n'))
    cp3_2 = float(input('Quanto você tirou no CheckPoint 3: \n'))
    notascp_2 = [cp1_2, cp2_2, cp3_2]
    os.system('cls')
    notascp_2.sort(reverse=True)
    mediacp2 = sum(notascp_2[:2]) / 2
    print('As duas maiores notas são:', notascp_2[0], 'e', notascp_2[1])
    print('A média das duas maiores notas é:', mediacp2)
    return mediacp2

def media_challenge():
    chl1 = float(input('\nQuanto você tirou no Challenge 1: \n'))
    return chl1

def media_challenge_2():
    chl2 = float(input('\nQuanto você tirou no Challenge 2: \n'))
    return chl2

def media_gs():
    gs1 = float(input('\nQuanto você tirou no GS 1: \n'))
    return gs1

def media_gs_2():
    gs2 = float(input('\nQuanto você tirou no GS 2: \n'))
    return gs2

def media_1s(mediacp1, chl1, gs1):
    media1s = mediacp1*0.2 + chl1*0.2 + gs1*0.6
    os.system('cls')
    print(f'Sua nota no primeiro semestre eh: {media1s}')
    return media1s

def media_2s(mediacp2, chl2, gs2):
    media2s = mediacp2*0.2 + chl2*0.2 + gs2*0.6
    os.system('cls')
    print(f'Sua nota no segundo semestre eh: {media2s}')
    return media2s

def media_anual(media1s, media2s):
    mediaa1 = media1s*0.4 + media2s*0.6
    os.system('cls')
    print(f'Sua nota anual eh: {mediaa1}')
    
main()

