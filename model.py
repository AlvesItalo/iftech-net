'''IFTECH user management system
Final project for Algorithms and Estructured Programming class

This module handles the database. It implements the CRUD functions
and simulate a database within a text file.
'''

import os
import re

__author__ = 'Ítalo Alves'
__email__ = 'italo.alves.jp@gmail.com'


def read_db():
    '''returns a string with all bd content'''

    try:
        file = open('db.txt', 'r')
        db = file.readlines()
        file.close()
    except:
        db = []

    return db

def write_db(db):
    '''Writes over the db file.'''

    # Updates db
    file = open('tempfile', 'w')
    file.writelines(db)

    # Assures writing on disk
    os.replace('tempfile', 'db.txt')
    
    file.close()

def validate_cpf(cpf):
    '''Returns True if CPF is valid and returns False when it isn't.'''
    
    # Regular expression to match with a valid CPF
    valid = re.search('([0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2})', cpf)

    if valid:
        return True
    else:
        return False

def create_user(cpf, name, email):
    '''Appends a new user to the end of db file.'''

    db = read_db()

    line = '{};{};{}\n'.format(cpf, name, email) 
    db.append(line)
    
    write_db(db)

def gen_email(cpf, name):
    '''Returns a tuple with three email options.'''

    domain = '@ifnet.com.br'

    opt1 = '{}{}'.format(cpf, domain)

    name_parts = name.split()

    opt2 = '{}.{}{}'.format(name_parts[0].lower(), name_parts[-1].lower(), domain)

    opt3 = '{}{}{}'.format(name_parts[0].lower(), cpf[0:3], domain)

    return (opt1, opt2, opt3)

def search_user(cpf):
    '''Searches and returns user data if found.'''

    db = read_db()
    db_size = len(db)

    for i in range(db_size):
        if cpf in db[i]:
            return db[i]

def update_user(cpf, new_name):
    '''Updates the name of a user in the db, if it exists.'''

    db = read_db()
    db_size = len(db)

    for i in range(db_size):
      if cpf in db[i]:
        cpf, name, email = db[i].split(';')
        db[i] = f'{cpf};{new_name};{email}'
        break
    
    write_db(db)

def delete_user(cpf):
    '''Removes a user from the database'''
    
    db = read_db()
    db_size = len(db)

    for i in range(db_size):
        if cpf in db[i]:
            db.pop(i)
            break
    
    write_db(db)
