"""
Игра крестики-нолики.
"""
import random


class Xo:
    array = [['&', '&', '&'], ['&', '&', '&'], ['&', '&', '&']]
    dictionary = {'a': 0, 'b': 1, 'c': 2, '1': 2, '2': 1, '3': 0}
    free = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    count_turn = 0
    flag = True
    win = ''

    def __init__(self, name, first_turn, x_or_o):
        self.name = name
        if first_turn == "player":
            self.first_turn = True
        if first_turn == "bot":
            self.first_turn = False
        if x_or_o == "X":
            self.x_or_o_player = 'X'
            self.x_or_o_bot = 'O'
        if x_or_o == "O":
            self.x_or_o_player = 'O'
            self.x_or_o_bot = 'X'

    def __str__(self):
        result = f'3 | {self.array[0][0]}    {self.array[0][1]}    {self.array[0][2]}\n2 | {self.array[1][0]}    '
        result += f'{self.array[1][1]}    {self.array[1][2]}\n1 | {self.array[2][0]}    {self.array[2][1]}    '
        result += f'{self.array[2][2]}\n    -    -    -\n    a    b    c'
        return result

    def turn_player(self):
        enter = input("Введите координату клетки в формате b1\n>>>:")
        if enter in self.free:
            self.array[self.dictionary[enter[1]]][self.dictionary[enter[0]]] = self.x_or_o_player
            self.free.remove(enter)
            return True
        else:
            return self.turn_player()

    def turn_bot(self):
        enter = random.choice(self.free)
        self.array[self.dictionary[enter[1]]][self.dictionary[enter[0]]] = self.x_or_o_bot
        self.free.remove(enter)
        return True

    def win_lose(self):
        if (self.array[0][0] == self.array[0][1] == self.array[0][2] == self.x_or_o_player) or (
                self.array[1][0] == self.array[1][1] == self.array[1][2] == self.x_or_o_player) or (
                self.array[2][0] == self.array[2][1] == self.array[2][2] == self.x_or_o_player) or (
                self.array[0][0] == self.array[1][0] == self.array[2][0] == self.x_or_o_player) or (
                self.array[0][1] == self.array[1][1] == self.array[2][1] == self.x_or_o_player) or (
                self.array[0][2] == self.array[1][2] == self.array[2][2] == self.x_or_o_player) or (
                self.array[0][0] == self.array[1][1] == self.array[2][2] == self.x_or_o_player) or (
                self.array[2][0] == self.array[1][1] == self.array[0][2] == self.x_or_o_player):
            self.flag = False
            self.win = self.name
            return True
        if (self.array[0][0] == self.array[0][1] == self.array[0][2] == self.x_or_o_bot) or (
                self.array[1][0] == self.array[1][1] == self.array[1][2] == self.x_or_o_bot) or (
                self.array[2][0] == self.array[2][1] == self.array[2][2] == self.x_or_o_bot) or (
                self.array[0][0] == self.array[1][0] == self.array[2][0] == self.x_or_o_bot) or (
                self.array[0][1] == self.array[1][1] == self.array[2][1] == self.x_or_o_bot) or (
                self.array[0][2] == self.array[1][2] == self.array[2][2] == self.x_or_o_bot) or (
                self.array[0][0] == self.array[1][1] == self.array[2][2] == self.x_or_o_bot) or (
                self.array[2][0] == self.array[1][1] == self.array[0][2] == self.x_or_o_bot):
            self.flag = False
            self.win = 'Бот'
            return True
        return False

    def play(self):
        print(f"---------{self.name} vs bot----turn {self.count_turn}---------")
        print(self.__str__())
        print("----------------------------------------")
        if not self.first_turn:
            self.turn_bot()
            self.count_turn += 1
            print(f"---------{self.name} vs bot----turn {self.count_turn}---------")
            print(self.__str__())
            print("----------------------------------------")
        while True:
            self.turn_player()
            self.count_turn += 1
            print(f"---------{self.name} vs bot----turn {self.count_turn}---------")
            print(self.__str__())
            print("----------------------------------------")
            self.win_lose()
            if not self.flag or self.count_turn == 9:
                break
            self.turn_bot()
            self.count_turn += 1
            print(f"---------{self.name} vs bot----turn {self.count_turn}---------")
            print(self.__str__())
            print("----------------------------------------")
            self.win_lose()
            if not self.flag or self.count_turn == 9:
                break
        if self.count_turn == 9:
            print("Ничья")
        else:
            print(f'{self.win} выиграл!!!')
        return True


origin_name = input("Введите имя\n>>>:")
origin_first_turn = input("Введите кто ходит первым bot/player\n>>>:")
origin_x_or_o = input("Введите кем вы играете X/O\n>>>:")
game_1 = Xo(origin_name, origin_first_turn, origin_x_or_o)
game_1.play()
