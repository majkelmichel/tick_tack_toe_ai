from random import randint

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


class Player:
    def __init__(self, player_type):
        self.player_type: str = player_type

    def move(self, cells):
        if self.player_type == "user":
            choice = input("Enter the coordinates: ")
            choice_l = choice.split(" ")
            return [int(choice_l[0]) - 1, int(choice_l[1]) - 1]
        elif self.player_type == "easy":
            choice_l = [randint(0, 2), randint(0, 2)]
            return choice_l
        elif self.player_type == "medium":
            for x in range(3):
                if cells[x][0] == cells[x][1] and cells[x][2] == ' ' and cells[x][0] != ' ':
                    return [x, 2]
                elif cells[x][1] == cells[x][2] and cells[x][0] == ' ' and cells[x][1] != ' ':
                    return [x, 0]
                elif cells[x][0] == cells[x][2] and cells[x][1] == ' ' and cells[x][0] != ' ':
                    return [x, 1]
            for y in range(3):
                if cells[0][y] == cells[1][y] and cells[2][y] == ' ' and cells[0][y] != ' ':
                    return [2, y]
                elif cells[1][y] == cells[2][y] and cells[0][y] == ' ' and cells[1][y] != ' ':
                    return [0, y]
                elif cells[0][y] == cells[2][y] and cells[1][y] == ' ' and cells[0][y] != ' ':
                    return [1, y]
            score: int = 0
            for x in range(2):
                if cells[x][x] == cells[x + 1][x + 1]:
                    score += 1
                if cells[0][0] == cells[2][2]:
                    score += 1
            if score == 2:
                for i in range(3):
                    if cells[i][i] == ' ':
                        return [i, i]
            score = 0
            for x in range(2):
                if cells[x][2 - x] == cells[x + 1][2 - 1]:
                    score += 1
                if cells[0][2] == cells[2][0]:
                    score += 1
            if score == 2:
                for i in range(3):
                    if cells[i][2 - i] == ' ':
                        return [i, 2 - i]

            choice_l = [randint(0, 2), randint(0, 2)]
            return choice_l


def main():
    while True:
        starting_args = input("Input command: ").split(' ')
        if len(starting_args) == 1 and starting_args == 'exit':
            return None
        if len(starting_args) != 3:
            print("Bad parameters!")
            continue
        else:
            break
    player_x = Player(starting_args[1])
    player_y = Player(starting_args[2])
    play_field_cells = refactor_list([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    moves = 0
    next_to_move = "X"
    show_play_field(play_field_cells)
    while moves < 9:
        play_field_cells, next_to_move = play_game(play_field_cells, next_to_move, player_x, player_y)
        moves += 1
        if check_win(play_field_cells):
            print(check_win(play_field_cells))
            return None
    print("Draw")


# def game_start():
#     moves_made = 0
#     starting_cells = list(input("Enter cells: "))
#     # print(who_first(starting_cells))
#     if who_first(starting_cells):
#         starting = "X"
#     else:
#         starting = "O"
#
#     starting_cells = swap_underscore_to_space(starting_cells)
#     for cell in starting_cells:
#         if cell == "X" or cell == "O":
#             moves_made += 1
#
#     starting_cells = refactor_list(starting_cells)
#     show_play_field(starting_cells)
#
#     return starting_cells, starting, moves_made


def play_game(cells, move, player_one, player_two):
    while True:
        if move == "O":
            choice_list = player_two.move(cells)

            try:
                choice_list[0] = int(choice_list[0])
                choice_list[1] = int(choice_list[1])
            except ValueError:
                if player_two.player_type == "user":
                    print("You should enter numbers!")
                continue
            if choice_list[0] not in range(3) or choice_list[1] not in range(3):
                if player_two.player_type == "user":
                    print("Coordinates should be from 1 to 3!")
                continue
            if cells[choice_list[0]][choice_list[1]] != ' ':
                if player_two.player_type == "user":
                    print("This cell is occupied! Choose another one!")
                continue
        else:
            choice_list = player_one.move(cells)

            try:
                choice_list[0] = int(choice_list[0])
                choice_list[1] = int(choice_list[1])
            except ValueError:
                if player_one.player_type == "user":
                    print("You should enter numbers!")
                continue
            if choice_list[0] not in range(3) or choice_list[1] not in range(3):
                if player_one.player_type == "user":
                    print("Coordinates should be from 1 to 3!")
                continue
            if cells[choice_list[0]][choice_list[1]] != ' ':
                if player_one.player_type == "user":
                    print("This cell is occupied! Choose another one!")
                continue

        if move == "O":
            cells[int(choice_list[0])][int(choice_list[1])] = "O"
            if player_two.player_type == "easy" or player_two.player_type == "medium":
                print(f'Making move "{player_two.player_type}"')
            show_play_field(cells)
            return cells, "X"
        else:
            cells[int(choice_list[0])][int(choice_list[1])] = "X"
            if player_one.player_type == "easy" or player_one.player_type == "medium":
                print(f'Making move "{player_one.player_type}"')
            show_play_field(cells)
            return cells, "O"


def check_win(cells):
    # Horizontal check
    if cells[0][0] == cells[0][1] == cells[0][2] and cells[0][0] != ' ':
        return f'{cells[0][0]} wins'
    if cells[1][0] == cells[1][1] == cells[1][2] and cells[1][0] != ' ':
        return f'{cells[1][0]} wins'
    if cells[2][0] == cells[2][1] == cells[2][2] and cells[2][0] != ' ':
        return f'{cells[2][0]} wins'
    # Vertical check
    if cells[0][0] == cells[1][0] == cells[2][0] and cells[0][0] != ' ':
        return f'{cells[0][0]} wins'
    if cells[0][1] == cells[1][1] == cells[2][1] and cells[0][1] != ' ':
        return f'{cells[0][1]} wins'
    if cells[0][2] == cells[1][2] == cells[2][2] and cells[0][2] != ' ':
        return f'{cells[0][2]} wins'
    # Cross check
    if cells[0][0] == cells[1][1] == cells[2][2] and cells[0][0] != ' ':
        return f'{cells[0][0]} wins'
    if cells[0][2] == cells[1][1] == cells[2][0] and cells[1][1] != ' ':
        return f'{cells[0][2]} wins'
    return False


def show_play_field(cells):
    print("---------")
    print(f"| {cells[0][2]} {cells[1][2]} {cells[2][2]} |")
    print(f"| {cells[0][1]} {cells[1][1]} {cells[2][1]} |")
    print(f"| {cells[0][0]} {cells[1][0]} {cells[2][0]} |")
    print("---------")


# def who_first(cells):
#     counter = 0
#     for i in cells:
#         if i == '_':
#             counter += 1
#     return counter % 2 != 0


# def swap_underscore_to_space(list_with_cells):
#     for i in range(len(list_with_cells)):
#         if list_with_cells[i] == '_':
#             list_with_cells[i] = ' '
#     return list_with_cells


def refactor_list(list_to_refactor):
    new = []
    i = 0
    for x in range(3):
        new.append([])
        for _ in range(3):
            new[x].append("")
    for x in range(2, -1, -1):
        for y in range(3):
            new[y][x] = list_to_refactor[i]
            i += 1
    return new


main()
