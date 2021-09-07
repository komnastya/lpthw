# ex35

from sys import exit


def door_one():
    print("За этой дверью медведь поедает чизкейк.")
    print("У тебя 3 варианта")
    print("1. Попробовать поговорить")
    print("2. Наорать на медведя и забрать чизкейк")
    print("3. Убежать")
    print("Что делаем?")

    bear = input("> ")

    if bear == "1":
        print(
            "Поздравляю! Медведь оказался ручным! Теперь вы  вместе пьете пиво, закусывая вторым чизкейком"
        )
        print("Game over")
    elif bear == "2":
        print("А Миша говорящий!")
        print(
            "- Слышь, ты чё тут разорался! Да поделюсь я с тобой, поделюсь, несчастный ты человек"
        )
        print("Game over")
    elif bear == "3":
        print("Ээээх, зряяя, такого другана потерял")
        print("Game over")
    else:
        print("Ты что, до 3-х считать не умеешь?")


def door_two():
    print("В этой комнате крокодил. Он спит")
    print("Что будешь делать?")
    print("1. Разбужу крокодила")
    print("2. Не буду его трогать")

    crocodile_satisfied = False

    while True:
        crocodile = input("> ")

        if crocodile == "1" and not crocodile_satisfied:
            print("Он открыл глаза")
            print("Похоже, он хочет есть...")
            eat()
            crocodile_satisfied = True

        elif crocodile == "1" and crocodile_satisfied:
            print("Похоже, сейчас он хочет сожрать тебя! Фруктами сыт не будешь!")
            dead("Беги, Форест, беги!")

        elif crocodile == "2" and crocodile_satisfied:
            dead("Ну так и всё. Скучно с тобой...")

        elif crocodile == "2" and not crocodile_satisfied:
            print("Ходишь как слон. Вот разбудил его - теперь корми.")
            eat()
            crocodile_satisfied = True

        else:
            print('Покормлю крокодила" или "Не буду его трогать" надо было выбирать!')
            dead("Game over")


def door_three():
    print("Здесь бегемотик гуляет по полю и собирает ромашки.")
    dead("Скучно")


def eat():
    print("Чем можно накормить крокодила?")
    print("Бананами или кокосами?")
    eat = input("> ")
    if eat == "Бананами":
        print("Его попёрло! Теперь он танцует")
        print("Сытый крокодил - не голодный крокодил")
        print("Может ещё его покормишь?")
        print("1. Покормлю крокодила")
        print("2. Не буду его трогать")
    elif eat == "Кокосами":
        print("Он заговорил и предложил выпить коньяка на двоих")
        print("Поздравляю! Ты нашёл еще одного другана. Что дальше?")
        print("1. Покормлю крокодила")
        print("2. Не буду его трогать")
    else:
        print('Нужно было написать "Бананами" или "Кокосами".')
        dead("Ну так и всё")


def dead(reason):
    print(reason, "Game over!")
    exit(0)


def start():
    print(
        """Привет! Ты попал в мою первую игрушку!
   Перед тобой три двери. В какую войдешь?"""
    )

    door = input("> ")

    if door == "1":
        door_one()
    elif door == "2":
        door_two()
    elif door == "3":
        door_three()
    else:
        print("Ты что, до  трёх считать не умеешь? Я же сказала, 1, 2 или 3!")
        dead("Мдааа...")


start()
