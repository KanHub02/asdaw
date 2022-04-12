import random
import datetime
def timer():
    start_time = datetime.datetime.now().second
    c = 1
    ai_num = random.randint(1, 100)
    tries = []
    print('Загадай число от 1 до 100')
    while 1:
        try:
            ask = int(input('Какое число я загадал?'))
        except ValueError:
            print('Только целые числа, без букв')
            continue
        if ask == ai_num:
            c -= 1
            tries.append(c)
            print(f'Мое число {ai_num}')
            print('Хорошо сыграно GG/WP')
            print(f'Попыток ушло{tries}')
            break
        elif ask <= ai_num:
            print('Не а, твое число < моего')
            c += 1
            if ask >= 101 or ask <= 1:
                print('Хаха, ты дурак? не больше 100 и не меньше 1!!!')
                c -= 1
            continue
        elif ask >= ai_num:
            print('Не а, твое число > моего')
            c += 1
            if ask >= 101 or ask <= 1:
                print('Хаха, ты дурак? не больше 100 и не меньше 1!!!')
                c -= 1
            continue
    end_time = datetime.datetime.now().second
    print('Времени ушло')
    print("--- %s секунд ---" % (end_time - start_time))

timer()
