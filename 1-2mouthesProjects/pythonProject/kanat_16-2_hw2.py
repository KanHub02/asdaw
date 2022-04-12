# Просим пользователя вести слово
word = input("Cлово: ")
print(word.upper())
gl = 0
sgl = 0
while 1:
    for i in word:
        letter = i.lower()
        if letter == "а" or letter == "е" or\
           letter == "ё" or letter == "и" or\
           letter == "о" or letter == "у" or\
           letter == "ы" or letter == "э" or\
           letter == "ю" or letter == "я":
            gl += 1
        elif letter == "a" or letter == "e" or\
             letter == "i" or letter == "o" or\
             letter == "u" or letter == "y":
             gl += 1
        else:
            sgl += 1
    # Вывод количество букв в слове
    print (f"Количество символов: {len(word)}")
    # Вывод количество гласных и согласных букв
    print(f"Гласныx букв: {gl} \nСогласныx букв: {sgl}")
    gl = round(gl/len(word)*100, 2)
    print(f"Гласные {gl}% / Согласные {round(100-gl, 2)}%")
    ask = input('Что бы выйти из программы напишите QUIT')
    if ask == 'quit'.lower():
        break
# ask = input("Вы хотите выйти из программы?  Если да то нажмите N")
# if ask == "N":
#     print('Начните программу заново')
# else:
#     print('До свидания')








