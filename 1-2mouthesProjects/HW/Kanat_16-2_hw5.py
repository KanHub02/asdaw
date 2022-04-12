movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },

    "Акыркы Сабак": {}
}
def all():
    for k, v in movies.items():
        print(k, v)

def add_movie(ask):
    ask = input('Введите название фильма: ')
    if ask in movies.keys():
        print('This movie already exist!')
    else:
        print("Movie added successfully")
        movies[ask.title()] = {}


def add_rating(ask, name, rating):
    ask = input('Введите название фильма, который хотите оценить!: ')

    if not ask.title() in movies.keys():
        print("This movie doesn't exist")
    elif ask.title() in movies:
        name = input('Имя зрителя: ')
        rating = int(input('Рейтинг от 0 до 10: '))
        for i in movies:
            if name in movies[i]:
                print('Ошибка такое имя уже есть!')
                name = input('введите новое имя: ')
        if rating >= 1 and rating <= 10:
            print(f'A rating has been added for {ask}: {name} rated it {rating}')
            movies[ask.title()][name.title()] = rating
        else:
            print('не меньше 0 и не больше 10!')

def rate_view():
    for movie, rate in movies.items():
        if len(rate) == 0:
            print(f"У этого фильма {movie} нет рейтинга !!!")
        else:
            rates_list = list(rate.values())
            average = round(sum(rates_list) / len(rates_list), 1)
            print(f"фильм:{movie} - рейтинг: {average}")


while True:
    command = input(f'Выберите команду \n 1) добавить фильм \n 2) добавить рейтинг к фильму \n '
                    f'3) Общий рейтинг фильмов \n 0) выход')
    if command == '1':
        add_movie('title')
        print(movies)
    elif command == '2':
        add_rating('ask', 'name', 'rating')
        print(movies)
    elif command == '3':
        rate_view()
        print(movies)
    elif command == '0':
        print('Programm has been finished')
        break
    else:
        print('Ошибка!')

