# numbers = [1, 2 , 3 , 4 , 5 , 6]
# studens = ['Asel', 'Marsel', 'Renat', 2, 10,True, False, numbers]
# numbers.remove(1)
# print(numbers)
# numbers = [1, 2, 3, 4, 5, 6, 7]
# new_numbers = [i + 1 for i in numbers]
# print(numbers)
# new = (1, 2, 3, 4, 5)
# new = list(new)
# new.append(6)
# print(type(new))
# print(new)
students = ['beka', 'Temirlan', 'Elmar', 'Azia' 'Asel', 'Emirlan']
students1 = ['Бека','Темирлан', 'Ельмар', 'Азия', 'Асель', 'Эмирлан']
second_row = []

while True:
    name = input('Youre name?')
    if name.title() in students or name.title() in students1:
        if name.title() in second_row:
            print('Уже есть такой ментор в списке!')
    ask2 = input('Хотите его заменить?')
    if ask2.title() == 'Да':


        second_row.append(name.title())
    elif name.title() == 'Exit':
        print('Good Bye')
        break
    else:
        print('No')
