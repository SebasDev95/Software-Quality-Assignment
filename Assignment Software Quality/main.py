import re
import sqlite3

from Users import ValidateUsers, Encryption
from Clients import ValidateClients

conn = sqlite3.connect('database.db')

c = conn.cursor()


def createUser():
    # usernameRequirements = '-' * 30 + '\nCreate your username \n\nAt least 5 characters\nAt most 20 characters\nStart with a letter\nOnly lower- uppercase, - , _ , \' and . \n'
    # passwordRequirements = '-' * 30 + '\nCreate your password\n\nAt least 8 characters\nAt most 30 characters\nOnly lower- uppercase, numbers and special characters\nMust have one lowercase letter, one uppercase letter, one digit and one special character\n'
    pass

def createClient():
    pass


def initiateDatabase():
    c.execute("""CREATE TABLE users (
                username text,
                password text,
                status text
                ) """)

    c.execute("""CREATE TABLE clients (
                name text,
                street text,
                housenumber text,
                zipcode text,
                email text,
                mobile text
                ) """)

    conn.commit()

    # Super administrator
    c.execute("INSERT INTO users VALUES ('Pootato', 'Testing123!', 'Super Administrator')")

    conn.commit()
    conn.close()

def addUser(user):
    with conn:
        c.execute("""INSERT INTO users VALUES (:username :password :status)""",
            {'username': Encryption().encrypt(user.username), 'password': Encryption().encrypt(user.password), 'status': user.status})

def addClient(client):
    with conn:
        c.execute("""INSERT INTO clients VALUES (:name :email :street :hnumber :zipcode :city :mobile)""", 
            {'name': client.name, 'email': client.email, 'street': client.street, 'housenumber': client.hnumber,
            'zipcode': client.zipcode, 'city': client.city, 'mobile': client.mobile})

