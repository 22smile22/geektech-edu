"""
Группа  Geektech 14Py - студент Акылбек Мамбетакунов
Месяц 4 - Django REST. Домашнее задание № 1

Домашнее задание 1.
Создать проект (Afisha) с одним приложением (movie_app). Будут три модели:
Director
name

Movie
title
description
duration
director(ForeignKey)

Review
text
movie(ForeignKey)

Вывести список режиссеров /api/v1/directors/
Вывести одного режиссера   /api/v1/directors/<int:id>/

Вывести список фильмов      /api/v1/movies/
Вывести один фильм             /api/v1/movies/<int:id>/

Вывести список отзывов       /api/v1/reviews/
Вывести один отзыв              /api/v1/reviews/<int:id>/
"""