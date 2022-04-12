# # гласные = 0
# # согласные = 0
# # word = input('Введите слово')
# # # exit = input('Если хотите выйти из программы напишите "Да')
# # while 1:
# #     print(f'Ваше слово {word}')
# #     for i in word:
# #         letter = i.lower()
# #         if letter == "a" or letter == "e" or \
# #                 letter == "i" or letter == "o" or \
# #                 letter == "u" or letter == "y":
# #             гласные += 1
# #         else:
# #             согласные += 1
# #             print("Vowels %i\nConsonants %i" % (гласные, согласные))
# #             break
# # while 2:
# #     exit = input('Если хотите выйти из программы напишите "Да')
# #     if exit.lower() == 'Да':
# #         print('Programm has been finished')
# #
# #
# #     break
# word = input('Ваше слово:')
# letter = 0
# sogl = 0
# while 1:
#     if letter == 'a' or letter == "u" or letter == 'i' or letter == 'o' or letter == 'y' or letter == 'e':
#
#         gl += 1
#     else:
#         sogl += 1
#         print(f'Гласных букв {letter}')
#         print(f'Гласных букв {sogl}')
#         break
# vowels = list('aeyuio')
# cons = list('bcdfghjklmnpqrstvexz')
# complete = False
# while complete == False:
#     ask = input('Ваше слово').lower().strip()
#     print(f'Слово {ask}'
gl = list('aeyuio')
sgl = list('bcdfghjklmnpqrstvexz')
while True:
    ask = input('Ваше слово?').lower()
    print(f'Ваше слово {ask}')
    print(f'Кол-во букв: {len(ask)}')
    print(f'Кол-во гласных {led(gl) in ask}')








