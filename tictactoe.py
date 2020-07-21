numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def main():
    play_field_cells, next_to_move = game_start()
    while True:
        play_field_cells, next_to_move = play_game(play_field_cells, next_to_move)
        if ' ' not in play_field_cells:
            break


def game_start():
    starting_cells = list(input("Enter cells: "))
    if who_first(starting_cells):
        starting = "Y"
    else:
        starting = "X"
    starting_cells = swap_underscore_to_space(starting_cells)
    starting_cells = refactor_list(starting_cells)
    show_play_field(starting_cells)
    return starting_cells, starting


def play_game(cells, move):
    while True:
        choice = input("Enter the coordinates: ")
        choice_list = choice.split(" ")
        print(choice_list)
        try:
            choice_list[0] = int(choice_list[0])
            choice_list[1] = int(choice_list[1])
        except ValueError:
            print("You should enter numbers")
            continue
        if cells[choice_list[0] - 1][choice_list[1] - 1] != ' ':
            print("This cells is occupied! Choose another one!")
            continue
        if choice[0] not in range(1, 4) or choice[1] not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
            continue
        if move:
            cells[int(choice[0]) - 1][int(choice[1]) - 1] = "Y"
            return cells, False
        else:
            cells[int(choice[0]) - 1][int(choice[1]) - 1] = "X"
            return cells, True


def who_first(cells):
    counter = 0
    for i in cells:
        if i == '_':
            counter += 1
    return counter % 2 == 0


def show_play_field(cells):
    print("---------")
    print(f"| {cells[0][2]} {cells[1][2]} {cells[2][2]} |")
    print(f"| {cells[0][1]} {cells[1][1]} {cells[2][1]} |")
    print(f"| {cells[0][0]} {cells[1][0]} {cells[2][0]} |")
    print("---------")


def swap_underscore_to_space(list_with_cells):
    for i in range(len(list_with_cells)):
        if list_with_cells[i] == '_':
            list_with_cells[i] = ' '
    return list_with_cells


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
