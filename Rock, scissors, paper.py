from random import randint

print("Привет, это игра в камень, ножницы, бумага")
print("Выбери (1 - камень, 2 - ножницы, 3 - бумага)")

while True:
    result_bot = randint(1, 3)

    if result_bot == 1:
        choose = 'камень'
    elif result_bot == 2:
        choose = 'ножницы'
    else:
        choose = 'бумага'

    try:
        result = int(input("Выбери: "))
    except ValueError:
        print("Вы ввели не число")
        continue

    if result not in [1, 2, 3]:
        print("Диапазон должен быть только от 1 до 3")
        continue

    if result == result_bot:
        print("Давай переиграем")
        continue

    if (result == 1 and result_bot == 2) or \
            (result == 2 and result_bot == 3) or \
            (result == 3 and result_bot == 1):
        print("You win")
    else:
        print("Bot win")

    print(f"бот выбрал {choose}")
    break
