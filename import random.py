import random

def password_ASCI(lenght):
    psword=''
    for i in range(int(lenght)):
        asci_code=random.randint(33,126)
        psword+=chr(asci_code)
    return psword
a = input('Длина пароля: ')
password = password_ASCI(a)
print(f'Ваш пароль: {password}')