# RAFAEL RODRIGUES ; LUCAS TAKEMOTO
import os

paciente = input('Registrar o nome do paciente: \n')
os.system('cls')
estado = input(f'{paciente} esta em estado de emergencia ?\n') 
if estado == 'sim':
    print(f'encaminhar {paciente} para atendimento medico imediato')
elif estado == 'nao':
    os.system('cls')
    agendamento = input('É uma consulta agendada ?\n')
    if agendamento == 'sim':
        print('Direcionar paciente para a especialidade correspondente')
    else:
        os.system('cls')
        print(f'encaminhar {paciente} para triagem medica e classificar o risco\n')
        risco = input('Qual a classificação ? (vermelho; amarelo; verde; azul)\n')
        os.system('cls')
        if risco == 'vermelho':
            print('Atendimento médico em até 10 minutos')
        elif risco == 'amarelo':
            print('Atendimento médico em até 60 minutos')
        elif risco == 'verde':
            print('Atendimento médico em até 120 minutos')
        elif risco == 'azul':
            print('Encaminhamento para UBS')