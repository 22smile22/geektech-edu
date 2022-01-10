# for, while

#word = "python"
# print(len(word))


# print(word[-1])

# for i in range(1, 5+1):
#     print(i)
#     if i == 3:
#         print("medium")
#
#for letter in word:
    #print(letter)
    #print(letter, end = '\n')

# counter = 0
#
# while counter < 5:
#     print(counter)
#     counter += 1
#     # if counter == 3:
#     #     print("Program finished")
#     #     break
#     if counter == 3:
#         print("something wrong")
#         continue

# index = 0
# while len(word) != index:
#     print(word[index])
#     print(index)
#     index += 1
#     # for i in word:
#     #     if i == "3":
#     #         print("нашли ошибку")
#     #         continue

# round = 0
#
# while round != 5:
#     round += 1
#     if round == 3:
#         print("Пропускаем")
#         continue
#     print(round)

min = 1
max = 100
medium = (min + max) // 2
secret_number = 45

while True:
    answer = input(f"{medium} ?")
    if answer == "yes":
        print("Yes!")
        break
    elif answer == ">":
        min = medium
    elif answer == "<":
        medium = max
    else:
        print("Incorrect")
