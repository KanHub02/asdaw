#Создать/сгенерировать список ten, состоящий из целых чисел от одного до десяти
ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Создать список evens, который состоит из четных чисел списка ten
even = list(filter(lambda x: x % 2 == 0, ten))
#Вывести на экран список возведенных в квадрат чисел от списка evens.
squares = list(map(lambda x: x**2, even))
print(even)
print(squares)
#Создать функцию для вывода объекта списка по указанному индексу.
def find_ind(ten):#У функции должен быть один аргумент по умолчанию -  список ten.
        for i in ten:
            if i in ten:
                print(ten[num])
                return
#Функция должна работать в бесконечном цикле с командой выхода.
while True:
    menu = input('Начать(1)\nВыйти(2)')
    if menu.title() == '1':
        while 1:
            try:
                num = int(input('Введите индекс'))
            except:
                print('Вводите только числа')
                continue
            try:
                if num in ten:
                    find_ind(ten)
                    menu2 = input('Хотите вернутся в меню(+), если нет нажмите любую клавишу?')
                    if menu2 == '+':
                        break
                    else:
                        continue
#При неверно указанном индексе использовать исключения с подсказкой ввода актуальных индексов указанного списка.
            except:
                print(f'Вводите числа от 0 до 9 \n из списка {ten}')
            if num >= 11:
                print(f'Вводите числа от 0 до 9 \n из списка {ten}')
            # elif num == 0:
            #     print((f'Индекс {num}\nЧисло из списка 1'))
            #     continue
            else:
                continue
        continue
    elif menu.title() == '2':
        print('GoodBye T_T')
        break