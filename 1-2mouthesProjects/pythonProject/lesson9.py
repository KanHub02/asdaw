# pres = {'name':'Садыр', 'Surname': ' Эеенбеков'}
# new = {'name': 'Канат', 'Surname': 'Усманов'}
# pres.update(new)
# print(pres)
letter = 'word'[2]
print(letter)
# user = {"пользователь", "Шерлок", "пароль", "BakerStreet221"}
# print(user['пароль'])


# list_1 = ['baha', 'nurik', 'adi', 'kesha']
# list_1.sort()
# rev_list = list_1[::-1]
# list_1.reverse()
# print(list_1 == rev_list, list_1 is rev_list)


# def name(name, age = 26):
#     return f'menya zovut{name} i mne {age} let'
# print(name('Kanat', 20))

def fun(a, *args, **kwargs):
    print('{} | {} | {}'.format(a, args, kwargs))
fun(1, 2, 3, x = 4, y = 5)