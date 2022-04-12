GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'},
#Добавляеи инстаграм и телефон
    'number': '996507052018',
    'instagram': '@geektech__kg'
}
#Удаляем bag
del GeekTech['bag']
#Изменяем адрес на нынешний
GeekTech['address'] = 'Ибраимова 103, БЦ Victory'
#Добавить/расширить список актуальными курсами и преобразовать в кортеж
GeekTech['courses'].append('FullStack, UX/UI, IOS, GeekCamp')
tp = tuple(GeekTech['courses'])
GeekTech['courses'] = tp
for k, v in GeekTech.items():
    print(k, ':', v)
# print(type(tp))