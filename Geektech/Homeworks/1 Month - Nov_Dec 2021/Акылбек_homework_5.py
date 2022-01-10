"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Домашнее задание №5 - Рейтинг фильмов

Нужно написать программу, которая будет хранить информацию о рейтинге фильмов.
Для одного фильма может быть от нуля и более рейтингов.
Каждый рейтинг содержит информацию об имени пользователя и его оценку от 0 до 10
Базовые данные для программы:

movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Spider-Man": {}
}

Программа должна уметь:

Добавлять фильм:
пользователь вводит название, например "Interstellar", если его нет в списке фильмов,
то программа выводит сообщение об успешном добавлении фильма:
"Movie added successfully"
если фильм уже есть, то вывести: “This movie already exist!”

Добавлять рейтинг к фильму
Пользователь вводит название, например "Interstellar"
Если фильм не существует, вывести сообщение
"This movie doesn't exist"
Если фильм существует, спросить пользователя два параметра: имя оценивающего и его оценку от 0 до 10.
Вывести на экран сообщение об успешном добавлении рейтинга:
A rating has been added for Interstellar: Rick rated it 9

Просматривать рейтинг для всех фильмов
Программа выводит средние рейтинги для всех фильмов
Interstellar is rated 7.7
Django Unchained is rated 9.5
Если рейтинга для фильма нет то выводить сообщение:
Rating is not yet available for movie_name

Указания:
В программе необходимо использовать бесконечный цикл для ввода команд.
Добавить пункт "Выход", который завершит программу.
Если пользователь вводит рейтинг, не попадающий в интервал от 1 до 10, выводить сообщение об ошибке и не добавлять этот рейтинг.

"""
movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Spider-Man": {}
}

def cinema_add(cinema):
    if cinema in movies.keys():
        print("Movie added successfully")
    else:
        movies.update({cinema: dict()})

def cinema_vote(cinema_r):
    if cinema_r not in movies.keys():
        print("This movie doesn't exist")
    else:
        p_name = input("Enter a name of person:")
        p_rate = int(input("Enter a rate:"))
        if p_rate < 0 or p_rate > 10:
            print("You must enter a value from 0 to 10!")
        else:
            movies[cinema_r].update({p_name: p_rate})
            print(f"{p_name} is rated in {p_rate}")

def vote_higlight():
    for cinema, vote in movies.items():
        vote_list = []
        for r in vote.values():
            vote_list.append(r)
        if len(vote_list) == 0:
            print(f"Rating is not yet available for {cinema}")
        else:
            print(f"A rating has been added for {cinema}: rated it {sum(vote_list) / len(vote_list)}")

def review():
    for f_name, f_rates in movies.items():
        print(f"\nThe film name is: {f_name}")
        if len(f_rates) == 0:
            print("Rating is not available")
        else:
            print("The rate is: ")
            for p_user, p_rate in f_rates.items():
                print(f"{p_user}: {p_rate}")

while 1:
    review()
    action = str.upper((input("\nChoose a action\nA - to add a film\nR - to add a grades\n"
                              "G - to view a grades\nE - the end of program:\nEnter here: ")))
    print("---" * 67)
    if action == 'E':
        print("The program has finished")
        break
    elif action == 'A':
        f_name = input("Enter a film name:")
        cinema_add(f_name)
    elif action == 'R':
        n_vote = input("Enter the name of the movie to add a rating:")
        cinema_vote(n_vote)
    elif action == 'G':
        vote_higlight()
    else:
        print("Invalid action, please try again")