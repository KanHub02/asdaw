def bubbleSort(numeric, step):
    # i - индексикация списка
    for i in range(len(numeric)):
        for h in range(0, len(numeric) - i - 1):
            #Numeric[h] - число с лева, numeric[h+1] число с права
            if numeric[h] > numeric[h + 1]:
                print(numeric)
                num = numeric[h]
                numeric[h] = numeric[h + 1]
                numeric[h + 1] = num
                step += 1
                print(f'Сдвигов было произведено:{step}')
                # if numeric[h] == numeric[h + 1]:
                #     print(numeric)
                #     break


numeric = [-10, 10, 24, 1232, 68, 1, -9, -11, 0, 2, 3]
step = 0
print(numeric)

bubbleSort(numeric, step)
print('Список отсортирован:')
print(numeric)
