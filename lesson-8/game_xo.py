"""
Игра крестики-нолики.
"""
import random


def enter(line):
    data = input(line)
    if line == "Введите кто ходит первым bot/player\n>>>:":
        if data == "player":
            return True
        if data == "bot":
            return False
    if line == "Введите кем вы играете X/O\n>>>:":
        if data == "X" or data == "x" or data == "х" or data == "Х":
            return True
        if data == "O" or data == "o" or data == "0" or data == "о" or data == "О":
            return False
    print("Ввод неверный!!!")
    return enter(line)


class Xo:
    array = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    dictionary = {'a': 0, 'b': 1, 'c': 2, '1': 2, '2': 1, '3': 0}
    free = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    count_turn = 0
    flag = True
    win = ''

    def __init__(self, name, first_turn, x_or_o):
        self.name = name
        self.first_turn = first_turn
        if x_or_o:
            self.x_or_o_player = 'X'
            self.x_or_o_bot = 'O'
        if not x_or_o:
            self.x_or_o_player = 'O'
            self.x_or_o_bot = 'X'

    def __str__(self):
        result = f'  |-----|-----|-----|\n3 |  {self.array[0][0]}  |  {self.array[0][1]}  '
        result += f'|  {self.array[0][2]}  |\n  |-----|-----|-----|\n2 |  {self.array[1][0]}  |  '
        result += f'{self.array[1][1]}  |  {self.array[1][2]}  |\n  |-----|-----|-----|\n1 '
        result += f'|  {self.array[2][0]}  |  {self.array[2][1]}  |  '
        result += f'{self.array[2][2]}  |\n  |-----|-----|-----|\n     a     b     c'
        return result

    def enter_cell(self):
        result = input("Введите координату клетки в формате b1\n>>>:")
        if result in self.free:
            return result
        print("Ввод неверный или клетка уже занята!!!")
        return self.enter_cell()

    def turn_player(self):
        cell = self.enter_cell()
        if cell in self.free:
            self.array[self.dictionary[cell[1]]][self.dictionary[cell[0]]] = self.x_or_o_player
            self.free.remove(cell)
            return True
        else:
            return self.turn_player()

    def turn_bot(self):
        cell = random.choice(self.free)
        self.array[self.dictionary[cell[1]]][self.dictionary[cell[0]]] = self.x_or_o_bot
        self.free.remove(cell)
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
origin_first_turn = enter("Введите кто ходит первым bot/player\n>>>:")
origin_x_or_o = enter("Введите кем вы играете X/O\n>>>:")
game_1 = Xo(origin_name, origin_first_turn, origin_x_or_o)
game_1.play()
