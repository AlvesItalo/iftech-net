#!/usr/bin/env python

'''IFTECH user management system
Final project for Algorithms and Estructured Programming class

This module handles the front-end of the application. 
It presents and retireves data for the user.
'''

from model import *
import os

__author__ = 'Ítalo Alves'
__email__ = 'italo.alves.jp@gmail.com'


def clear():
    '''Clears console screen'''

    if os.name == 'posix':
        command = 'clear'    
    else:
        command = 'cls'

    os.system(command)

def menu():
    clear()

    print('''
    IFTECH-SYS Bem vindo!

    Selecione uma opção:
    [1] Cadastrar usuário
    [2] Pesquisar usuário
    [3] Alterar usuário
    [4] Excluir usuário
    [5] Listar usuários
    [0] Sair
    ''')

    opt = int(input('> '))
    while opt < 0 or opt > 5:
        print('Opção inválida!')
        opt = int(input('> '))
    
    return opt

def create_user_view():
    clear()

    name = input('Insira o nome: ')
    
    while True:
        cpf = input('Insira o CPF: ')
        cpf = cpf.replace('-', '')
        cpf = cpf.replace('.', '')
        
        if not validate_cpf(cpf):
            print('CPF é Inválido!')
        elif search_user(cpf):
            print('Usuário já existe!')
        else:
            break

    print('Escolha um email: ')
    options = gen_email(cpf, name)
    i = 1
    for option in options:
        print(i, option)
        i+=1
    
    email_opt = int(input('Opção> '))
    while email_opt < 1 or email_opt > 3:
        email_opt = int(input('\nOpção inválida!\nOpção> '))
    
    create_user(cpf, name, options[email_opt-1])
    print('Usuário criado com sucesso.')
    input('Pressione <ENTER> ')

def search_user_view():
    clear()

    cpf = input('Insira o CPF para buscar: ')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace('.', '')

    if validate_cpf(cpf):
        user = search_user(cpf) 
        if user:
            cpf, name, email = user.split(';')
            print('Dados do usuário:')
            print('CPF: {}\nNome: {}\nEmail: {}'.format(cpf, name, email))
        else:
            print('Usuário não encontrado.')
    else:
        print('CPF inválido!')

    input('Pressione <ENTER> ')

def update_user_view():
    clear()
    
    cpf = cpf = input('Insira o CPF do usuário a ser atualizado: ')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace('.', '')

    if validate_cpf(cpf):
        user = search_user(cpf)

        if user:
            cpf, name, email = user.split(';')
            print('Dados do usuário:')
            print('CPF: {}\nNome: {}\nEmail: {}'.format(cpf, name, email))

            new_name = input('Insira o novo nome: ')
            confirmation = input('Confirma a atualização?(S/n)> ')
            if confirmation.lower() == 's':
                update_user(cpf, new_name)
                print('Usuário atualizado com sucesso.')
            elif confirmation.lower() == 'n':
                print('Operação cancelada')
        else:
            print('Usuário não encontrado')
    else:
        print('CPF inválido!')

    input('Pressione <ENTER> ')

def delete_user_view():
    clear()
    
    cpf = cpf = input('Insira o CPF do usuário a remover: ')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace('.', '')
    
    if validate_cpf(cpf):
        user = search_user(cpf)

        if user:
            cpf, name, email = user.split(';')
            print('Dados do usuário:')
            print('CPF: {}\nNome: {}\nEmail: {}'.format(cpf, name, email))

            confirmation = input('Confirma a remoção?(S/n)> ')
            if confirmation.lower() == 's':
                delete_user(cpf)
                print('Usuário removido com sucesso.')
            elif confirmation.lower() == 'n':
                print('Operação cancelada')
            
        else:
            print('Usuário não encontrado')
    else:
        print('CPF Inválido!')

    input('Pressione <ENTER>')

def list_user_view():
    clear()
    
    print('Usuários cadastrados:\n')
    n = 0
    for user in read_db():
        cpf, name, email = user.split(';')
        print('CPF: {}\nNome: {}\nEmail: {}'.format(cpf, name, email))
        print('----------------------------')
        n+=1
        
    print(n, 'Usuários.')
    input('Pressione <ENTER> ')
    

if __name__ == '__main__':
    while True:
        #Program main loop
        opt = menu()

        if opt == 1:
           create_user_view()
        elif opt == 2:
            search_user_view()
        elif opt == 3:
            update_user_view()
        elif opt == 4:
            delete_user_view()
        elif opt == 5:
            list_user_view()
        elif opt == 0:
            quit()
