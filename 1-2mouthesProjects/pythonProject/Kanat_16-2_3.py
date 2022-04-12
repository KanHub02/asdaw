#Добавление (программа просит ввести имя, затем добавляет имя в список)
mentors = ['Эсенбек', 'Мирхад', 'Беки', 'Азиз', 'Эмир', 'Элина', 'Малина']
fav_mentors = []
print('Составьте топ 5 ваших менторов')
while True:
    print(f'Выберите из списка менторов{mentors}')
    ask = input('Введите имя ментора:')
    if len(ask) == 16:
        print('Слишком длинное имя')
    elif ask.title() == 'Эсенбек' or ask.title() == 'Мирхад' or ask.title() == 'Беки' \
            or ask.title() == 'Азиз' or ask.title() == 'Эмир' or ask.title() == 'Элина' \
                or ask.title() == 'Малина':
        print('')
#Здесь не смог правильно продолжить программу при не првильном написании имени
    else:
        print('Такого имени нет в списке!')
        print('Начните программу заново')
        continue
    if ask.title() in fav_mentors:
        fav_mentors.remove(ask.title())
        print('Вы уже вводили данного ментора')
    menu = input('Хотите добавить или убрать ментора из списка?\n Добавить/Удалить')
#Удалять ментора по имени или индексу
    if menu.title() == 'Добавить':
        fav_mentors.append(ask.title())
    elif menu.title() == 'Удалить':
        fav_mentors.remove(ask.title())
        if ask.title() in fav_mentors:
            fav_mentors.remove(ask.title())
            print('Вы уже вводили данного ментора')

    if len(fav_mentors) == 5:
        print('Максимальное кол-во менторв 5!')
        print(f'Ваш список любимых менторов {fav_mentors}')
        # else:
        #     print('Такого имени нету в списке')

        ask2 = input('Что бы выйти из программы напишите EXIT')
        if ask2.title() == 'Exit':
#После выхода из цикла преобразовать список менторов в кортеж и вывести его на экран
            print(f'Ваш список любимых менторов {fav_mentors}')
            print('Пока')
            break
        else:
            print('Начните программу заново')
    print(fav_mentors)







