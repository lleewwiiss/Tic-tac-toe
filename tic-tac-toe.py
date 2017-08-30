import copy
from itertools import chain
from typing import List


class Cell:
    def __init__(self):
        self.value = ' '

    def __str__(self):
        return str(self.value)


class Grid:
    def __init__(self):
        self.grid = [[Cell() for _ in range(3)] for _ in range(3)]

    def __str__(self):
        grid_print = ''
        for i in range(3):
            for k in range(3):
                grid_print += ' ' + str(self.grid[i][k]) + ' '
                if k < 2:
                    grid_print += '|'
            if i == 0 or i == 1:
                grid_print += '\n------------\n'

        return grid_print


def check_win(grid: List[List[Cell]], x: int, y: int) -> bool:
    if grid[0][y].value == grid[1][y].value == grid[2][y].value != ' ':
        return True

    if grid[x][0].value == grid[x][1].value == grid[x][2].value != ' ':
        return True

    if x == y and grid[0][0].value == grid[1][1].value == grid[2][2].value != ' ':
        return True

    if x + y == 2 and grid[0][2].value == grid[1][1].value == grid[2][0].value != ' ':
        return True

    return False


def make_move(grid: List[List[Cell]]) -> List[int]:
    for i in range(3):
        for j in range(3):
            temp = copy.deepcopy(grid)
            if temp[j][i].value == ' ':
                temp[j][i].value = 'X'
                if check_win(temp, j, i):
                    return [j, i]

    for i in range(3):
        for j in range(3):
            temp = copy.deepcopy(grid)
            if temp[j][i].value == ' ':
                temp[j][i].value = 'O'
                if check_win(temp, j, i):
                    return [j, i]

    if grid[0][0].value == ' ':
        return [0, 0]
    if grid[2][0].value == ' ':
        return [2, 0]
    if grid[2][2].value == ' ':
        return [2, 2]
    if grid[0][2].value == ' ':
        return [0, 2]
    if grid[1][1].value == ' ':
        return [1, 1]

    for i in range(3):
        for j in range(3):
            if grid[j][i].value == ' ':
                return [j, i]


def ai_play(grid: List[List[Cell]], turns: int, x: int, y: int) -> bool:
    if turns == 0 and ((y == 0 and (x == 0 or x == 2)) or (y == 2 and (x == 0 or x == 2))):
        grid[1][1].value = 'O'
        return check_win(grid, 1, 1)
    elif turns == 0 and x == y == 1:
        if grid[2][0].value == ' ':
            grid[2][0].value = 'O'
            return check_win(grid, 0, 2)
        elif grid[2][2].value == ' ':
            grid[2][2].value = 'O'
            return check_win(grid, 2, 2)
        elif grid[2][0].value == ' ':
            grid[2][0].value = 'O'
            return check_win(grid, 2, 0)
        if grid[0][0].value == ' ':
            grid[0][0].value = 'O'
            return check_win(grid, 0, 0)
    else:
        x, y = make_move(grid)[:]
        grid[x][y].value = 'O'
        return check_win(grid, x, y)

    return False


def play_game():
    grid = Grid()
    print(grid)

    win = False
    game_over = False
    tie = False
    turns = 0

    while not game_over:

        while True:
            move = input('Choose move e.g. x y:').split()
            if move[0].isdigit() and move[1].isdigit() and 0 <= int(move[0]) < 3 and 0 <= int(move[1]) < 3:
                grid.grid[int(move[1])][int(move[0])].value = 'X'
                break

        print(grid)

        if check_win(grid.grid, int(move[1]), int(move[0])):
            win = True
            game_over = True
        elif all(x.value != ' ' for x in chain.from_iterable(grid.grid)):
            tie = True
            game_over = True
        elif ai_play(grid.grid, turns, int(move[1]), int(move[0])):
            game_over = True
        elif all(x.value != ' ' for x in chain.from_iterable(grid.grid)):
            tie = True
            game_over = True
        turns += 1
        print('\n')
        print(grid)

    if win:
        print('Winner, winner chicken dinner!')
    elif tie:
        print('Tie!')
    else:
        print('Game over!')


if __name__ == '__main__':
    play_game()
