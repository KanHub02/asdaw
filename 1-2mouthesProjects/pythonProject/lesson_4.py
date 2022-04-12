# students = ['sam', 'jack', 'azat', 'adilet']
# del_name = input('Введите индекс или имя')
# if del_name in students:
#     students.remove(del_name)
# elif del_name.isnumeric():
#     del students[int(del_name)]
#     print(students)
# students[0] = 'samat'
# old_name = input('old students')
# new_name = input('new students')
# students[students.index(old_name)] = new_name
# print(students)
# students = {
#     'name':'Adilet',
#     'age':19,
#     'height': 1.78
# }
# print(students)
# students2 = {
#     'name':'Kanat',
#     'age': 19,
#     'height': 178,
# }
# student2 = dict(name = 'Kanat', age = 18, height = 178)
# student2['weight'] =80
# student2['age'] = 20
# for k, v in student2.items():
#     print(student2)
#
# del students2['age']
# a = student2.pop('name')
# students = []
# candidates = [
#     {'name': 'Azat', 'ORT':150},
#     {'name': 'Kanat', 'ORT':120, 'next_yeat': True},
#     {'name': 'Beka', 'ORT':160},
# ]
# for i in candidates:
#     if i['ORT'] <= 110:
#         students.append(students.pop(students.index(i)))
#     else:
#         i['sled_god'] = True
# for i in candidates:
#     print(i)
# print(candidates)
# print(students)
countries = {
    'kg':{'red', 'yellow', },
    'ru':{'blue', 'white', 'blue'}
}
# name = 'abc'
# name - name.split()
# while True:
#     color = input('Цвет').split()
#     color = set(color)
#     print(color)
#     for k, v  in countries.items():
#         if color & v:
#             print(k)
#         else:
#             print('Такого цвета нет')
nom = [20, 50, 100, 200]
person = ['Тоголок Молдо', 'К.Датка', 'Т.Сатылганов', 'А. Осмонов']
kgdic = dict(zip(nom, person))
print(kgdic)
# c = 0
# while len(kgdic) != len(person):
#     kgdic[nom[c]] = person[c]
#     c += 1
# print(f'{k}: {v}')
# print(kgdic)


