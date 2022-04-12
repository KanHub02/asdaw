import random
from time import sleep

print('Welcome to 777Casino')
sleep(0.5)
print('777Casino')


def fortune():
    winlot = random.randint(1, 30)
    lot = int(input('Введите слот 1 - 30'))
    sleep(0.5)
    print('...')
    sleep(0.3)
    print('Идет вращения барабана')
    sleep(1)
    print('...')
    sleep(0.5)
    if lot == winlot:
        print('You win!!!')
    elif lot != winlot:
        print(f'Your slot was{lot}\nWin slot:{winlot}\nSorry(, try again')


fortune()
