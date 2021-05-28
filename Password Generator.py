import random


chars = 'abcdefghijklmnopqrstuvwxzy1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@£%^&*'

number = input('How many passwords do you want to generate? ')
number = int(number)

length = input('What length would you like your password to be? ')
length = int(length)




for p in range (number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password) 


