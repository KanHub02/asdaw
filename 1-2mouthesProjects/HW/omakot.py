while True:
    menu = input('1)Войти\n2)Найти \n3)Выход')

    if menu == "1":
        print("Добро пожаловать")
        while True:

            name = input('Введите логин: ')
            password = input('Введите пароль: ')
            if name.title() == 'Omka':
                print('')
            if password == '123':
                print('Салам')
                while 1:
                    jopa = input("Что желаеете найти\n(1)Мышки \n(2)Клавиатура \n(3)Монитор\n 4)Exit")
                    if jopa == '1':
                        print("цена 1000сом")
                        continue
                    if jopa == '2':
                        print("Цена 15000сом")
                        continue
                    if jopa == "3":
                        print("Цена 2ляма")
                        continue
                    if jopa == '4':
                        break

                break
            else:
                print('Котогуму же')
                break


    elif menu == "2":
        print('Нет доступа, зайдите на сайт')
        continue
    elif menu == "3":
        print("Давай")
        break
