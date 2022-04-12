import random
import datetime
num = int(input('Tries?'))
c = 1
name = input('Your Name?')
stat_time = datetime.datetime.now().second
print(name)
while 1:
    ran = random.randint(1, 9)
    ran1 = random.randint(1, 9)
    otvet = ran * ran1
    primer = int(input(f'{ran} * {ran1} ='))
    print(otvet)
    c += 1
    with open('results.txt', 'a', encoding='utf - 8') as file:
        if primer == otvet:
            file.write(f"\n{ran} * {ran1} = {primer} ({otvet}) правильно ")
        elif primer != otvet:
            file.write(f"\n{ran} * {ran1} = {primer} ({otvet}) не правильно ")
    if c > num:
        print('Попытки закончились T.T')
        end_time = datetime.datetime.now().second
        timer = end_time - stat_time
        print(f'Времени ушло: {timer} секунд')
        with open('results.txt', 'a', encoding="utf-8") as file:
            file.write(f" \nбыло {num} попыток, потрачено времени: {timer} секунд, имя: {name.title()}")
        break
