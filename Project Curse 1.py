#finish Curse, but need to put the "remove" option, save database ad fix the option "4" 

import os

notes1 = []
notes2 = []
notes3 = []

def show_app_name():
    print('''
    ▀█▀ █▀█ █▄█ █ █▄░█ █▀▀   ▀█▀ █▀█   █▄▄ █▀▀   █▄▄ █▀▀ ▀█▀ ▀█▀ █▀▀ █▀█
    ░█░ █▀▄ ░█░ █ █░▀█ █▄█   ░█░ █▄█   █▄█ ██▄   █▄█ ██▄ ░█░ ░█░ ██▄ █▀▄
    ''')

def show_options():
    print('1. At home')
    print('2. Outside')
    print('3. Inside myself')
    print('4. Quit\n')

def finish_app():
    os.system('cls')
    print('Try again, donkey...')
    invalid_option()

def invalid_option():
    os.system('cls')
    input('Press any botton !!!')
    main()

def note_1():
    os.system('cls')
    note1 = input('Right... What u need to put ?\n')
    notes1.append(note1)
    input('Perfect... was added !!! Pls press any botton.\n')
    main()

def note_2():
    os.system('cls')
    note2 = input('Right... What u need to put ?\n')
    notes2.append(note2)
    input('Perfect... was added !!! Pls press any botton.\n')
    main()

def note_3():
    os.system('cls')
    note3 = input('Right... What u need to put ?\n')
    notes3.append(note3)
    input('Perfect... was added !!! Pls press any botton.\n')
    main()

def read_1():
    
    for note1 in notes1:
        if notes1: 
            print(f'.{note1}')
    else: 
        if not notes1:
            print('Dont have things to do !!!')
        
    input('\nPress any botton to back !!!\n')
    main()

def read_2():
    
    for note2 in notes2:
        if note2:
            print(f'.{note2}')
    else:
        if not notes1:
            print('Dont have things to do !!!')
        
    input('\nPress any botton to back !!!\n')
    main()

def read_3():
    
    for note3 in notes3:
        if note3:
            print(f'.{note3}')
    else:
        if not notes1:
            print('Dont have things to do !!!')
        
    input('\nPress any botton to back !!!\n')
    main()

    
def choose_option():
    
    try:
        O_C = input('Choose one to be better: ')
        O_C = int(O_C)
        os.system('cls')
        print(f'U choose: {O_C}\n')
    except:
        invalid_option()
    
    if O_C == 1:
        prr1 = input('U need put, remove or read something ?\n')
        os.system('cls')
        print(f'U choose: {prr1}\n')
            
        if prr1 == 'put':
            note_1()

        elif prr1 == 'read':
            read_1()

        else:
            print('U only can use: put, read or remove... idiot')
            invalid_option()

    elif O_C == 2:
        prr2 = input('U need put, remove or read something ?\n')
        os.system('cls')
        print(f'U choose: {prr2}\n')
            
        if prr2 == 'put':
            note_2()

        elif prr2 == 'read':
            read_2()

        else:
            print('U only can use: put, read or remove... idiot')
            invalid_option()

    elif O_C == 3:
        prr3 = input('U need put, remove or read something ?\n')
        os.system('cls')
        print(f'U choose: {prr3}\n')
            
        if prr3 == 'put':
            note_3()

        elif prr3 == 'read':
            read_3()

        else:
            print('U only can use: put, read or remove... idiot')
            invalid_option()

    elif O_C == 4:
        prr4 = input('Do you really want to quit? (y/n)\n')
            
        if prr4 == 'y':
            os.system('cls')
            print('See you soon!!!')

        elif prr4 == 'n':
            invalid_option()


def main():
    os.system('cls')
    show_app_name()
    show_options()
    choose_option()

if __name__ == '__main__':
    main()