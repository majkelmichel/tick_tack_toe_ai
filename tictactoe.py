from random import randint

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ai_sign = "X"
en_sign = "O"


class Player:
    def __init__(self, player_type, player_sign):
        self.player_type: str = player_type
        self.player_sign: str = player_sign

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
        elif self.player_type == "hard":
            global ai_sign
            global en_sign
            ai_sign = self.player_sign
            en_sign = "X" if ai_sign == "O" else "O"
            cells = defactor_list(cells)
            return get_two_dim_index(minimax(cells, self.player_sign)["index"])


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
    player_x = Player(starting_args[1], "X")
    player_y = Player(starting_args[2], "Y")
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


def defactor_list(list_to_defactor):
    new = []
    c = 0
    for i in list_to_defactor:
        for j in i:
            if j == ' ':
                j = c
            new.append(j)
            c += 1
    return new


def check_if_win(cells, player):
    # Horizontal check
    if cells[0] == cells[1] == cells[2] == player or cells[3] == cells[4] == cells[5] == player\
            or cells[6] == cells[7] == cells[8] == player or cells[0] == cells[3] == cells[6] == player\
            or cells[1] == cells[4] == cells[7] == player or cells[2] == cells[5] == cells[8] == player\
            or cells[0] == cells[4] == cells[8] == player or cells[2] == cells[4] == cells[6] == player:
        return True
    return False


def available_spots(old_cells):
    available_cells = []
    for i in range(len(old_cells)):
        if isinstance(old_cells[i], int):
            available_cells.append(i)
    return available_cells


def minimax(new_cells, player):
    possible_spots = available_spots(new_cells)
    if check_if_win(new_cells, en_sign):
        return {"score": -10}
    elif check_if_win(new_cells, ai_sign):
        return {"score": 10}
    elif len(possible_spots) == 0:
        return {"score": 0}

    moves = []
    for i in range(len(possible_spots)):
        move: dict = dict()
        # print(new_cells, new_cells[possible_spots[i]], possible_spots[i], i)
        move["index"] = new_cells[possible_spots[i]]
        new_cells[possible_spots[i]] = player
        if player == ai_sign:
            result = minimax(new_cells, en_sign)
            move["score"] = result["score"]
        else:
            result = minimax(new_cells, ai_sign)
            move["score"] = result["score"]

        new_cells[possible_spots[i]] = move["index"]
        moves.append(move)
    # print(moves)
    best_move = []
    if player == ai_sign:
        best_score = -100000
        for i in range(len(moves)):
            if moves[i]["score"] > best_score:
                best_score = moves[i]["score"]
                best_move = i
    else:
        best_score = 100000
        for i in range(len(moves)):
            if moves[i]["score"] < best_score:
                best_score = moves[i]["score"]
                best_move = i
    return moves[best_move]


def get_two_dim_index(index):
    c = 0
    for x in range(3):
        for j in range(3):
            if index == c:
                return [x, j]
            c += 1


main()
# lst = defactor_list(["X", "O", " ", "O", " ", " ", " ", "X", "X"])
# lst = ["O",1 ,"X","X",4 ,"X", 6 ,"O","O"]
# print(available_spots(lst))
# print(minimax(lst, "X"))
