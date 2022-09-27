"""Game words. All players can entert names
and then one by one you should input words.
Every next player should input word
that starts with last letter of previous word.
In the end of a game you will see how many words
each of you input"""

import requests
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent


# Create_players__start
class Players:

    # Create_variables_to_save_players_results_and_word_list
    def __init__(self) -> None:
        self.name_list: list[str] = []
        self.results: dict = {}

    # Set_player_name__start
    def set_players_name(self) -> None:
        word_to_exit = "ок ok"
        Info.pre_start()
        while True:
            name = input("Введите имя: \n")
            if name.lower() in word_to_exit:
                Info.start_info()
                break
            self.name_list.append(name.title())
            self.results.setdefault(name.title(), 0)


# Game_processor__start
class Words:
    def __init__(self):
        self.word = None
        self.last_letter = None
        self.word_list = []

    # Take turn and save word if it corrects
    def turn(self) -> None:
        while True:
            for name in players.name_list:
                if len(self.word_list) == 0:
                    self.word = input(f"{name}, введите слово: \n").lower()
                    while not check.check_word():
                        self.word = input(f"{name}, введите слово: \n").lower()
                else:
                    last_word = str(self.word_list[-1])
                    self.last_letter = (
                        last_word[-2]
                        if last_word.endswith(("ь", "ы", "ъ"))
                        else last_word[-1]
                    )

                    self.word = input(
                        f"{name}, слово на букву '{self.last_letter}': \n"
                    ).lower()

                    while not check.check_word():
                        self.word = input(
                            f"{name}, слово на букву '{self.last_letter}': \n"
                        ).lower()

                players.results[name] += 1
                self.word_list.append(self.word)


# Game_processor__stop


# Checking_words__start
class Checking:
    def __init__(self) -> None:
        self.headers = {"User-Agent": ua.random}

    # Check word
    def check_word(self) -> bool:
        if len(words.word.split()) > 1:
            print("Можно ввести только одно слово!")
            return False
        elif words.word == "":
            print("Слово должно включать хотя бы одну букву!")
            return False
        elif words.word == "stop":
            Info.exit_view()
            exit()
        elif words.word in words.word_list:
            print("Слово уже существует!")
            return False
        elif (
            not words.word.startswith(str(words.last_letter))
            and len(words.word_list) > 0
        ):
            print("Слово начинается с не правильной буквы!")
            return False
        elif not self.exists_word():
            print("Такого слова не существует!")
            return False
        else:
            return True

    # Check if word exists
    def exists_word(self) -> bool:

        url = (
            f"https://ru.wikipedia.org/w/index.php?search={words.word}"
            f"&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1"
            f"%8F:%D0%9F%D0%BE%D0%B8%D1%81%D0%BA"
            f"&profile=advanced&fulltext=1&ns0=1"
        )
        response = requests.get(url, headers=self.headers)
        soup = Bs(response.text, "lxml")
        try:
            data = soup.find("ul", class_="mw-search-results")
            if len(data) != 0:
                return True
        except TypeError:
            return False


# Checking_words__stop


# Create_game_info__start
class Info:

    # set exit info
    @staticmethod
    def exit_view() -> None:
        for key, value in players.results.items():
            print(f"{key}, ввел {value} слов!")
        print("***********************")
        print(f"Всего введено слов: {len(words.word_list)}")

    # set start info
    @staticmethod
    def start_info() -> None:
        print("Удачной игры! введите 'stop', чтобы закончить игру.")

    # set pre-start info
    @staticmethod
    def pre_start() -> None:
        print("Вас приветсвует игра в слова.")
        print('Для начала введите имя игрока. Введите "ok" для начала игры.')


# Create_game_info__stop

# Run_game__start
ua = UserAgent()
players = Players()
check = Checking()
players.set_players_name()
words = Words()
words.turn()

# Run_game__stop
