movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },

    "Spider-Man": {}
}

def show():
    for name, rates in movies.items():
        print(f"\nФильм:{name}")
        if len(rates) == 0:
            print("Рейтинг ещё не доступен")
        else:
            print("Рейтинг: ")
            for user, rate in rates.items():
                print(f"{user}: {rate}")

def add_movie(movie):
    if movie in movies.keys():
        print("Фильм добавлен")
    else:
        movies.update({movie:dict()})

def add_rate(movie):
    if movie not in movies.keys():
        print("Такого фильма нет")
    else:
        name = input("Введите имя человека:")
        rate = int(input("Введите рейтинг:"))
        if rate < 0 or rate > 10:
            print("Введите оценку от 0 до 10!")
        else:
            movies[movie].update({name: rate})
            print(f"{name} оценено в {rate}")

def rate_view():
    for movie, rate in movies.items():
        rates = []
        for i in rate.values():
            rates.append(i)
        if len(rates) == 0:
            print(f"Рейтинг ещё не доступен для {movie}")
        else:
            print(f"{movie} оценка этого фильма {sum(rates) / len(rates)}")

while 1:
    show()
    concluded = int(input("\nВведите команду (1 - добавить фильм, 2 - добавить оценку, 3 - просмотр оценок, 0 - конец программы): "))
    print("---"*67)
    if concluded == 0:
        print("Программа закончена")
        break
    elif concluded == 1:
        movie = input("Напишите имя фильма:")
        add_movie(movie)
    elif concluded == 2:
        movie = input("Введите название фильма для добавления рейтинга:")
        add_rate(movie)
    elif concluded == 3:
        rate_view()
    else:
        print("Такой команды нету")
