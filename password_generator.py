from random import randint
import string

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*_+№#1234567890'

def generator(letters: string) -> string:
    i = 0
    password = []
    while i < 256:
        password.append(letters[randint(0,(len(letters))-1)])
        i += 1
    s = ''.join(password)
    return s

while True:
    print(generator(letters)) 
