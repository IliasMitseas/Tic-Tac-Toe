row1 = ["1", "2", "3"]
row2 = ["1", "2", "3"]
row3 = ["1", "2", "3"]

def display(lista1, lista2, lista3):
    print(f"{lista1[0]} \t {lista1[1]} \t {lista1[2]}")
    print(f"{lista2[0]} \t {lista2[1]} \t {lista2[2]}")
    print(f"{lista3[0]} \t {lista3[1]} \t {lista3[2]}")

def pick_x_or_o():
    while True:
        player1 = input("Player 1 pick between X or O: ")
        if player1 == "X" or player1 == "O":
            break

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    print("Player 2 you are :", player2)

    return player1, player2

def choice(player):
    row = ""
    index = 0
    while row != "row1" and row!= "row2" and row!="row3":
        row = input(player + " pick a row: ")

    while index <= 0 or index > 3:
        index = int(input(player + " pick your column: "))

    return row, index

def change_board(row, index, player):
    while True:
        if row == "row1":
            if row1[index-1].isdigit():
                row1[index - 1] = player
                break
            else:
                print("already played in that position, try again")
                row, index = choice(player)
        elif row == "row2":
            if row2[index-1].isdigit():
                row2[index - 1] = player
                break
            else:
                print("already played in that position, try again")
                row, index = choice(player)
        else:
            if row3[index-1].isdigit():
                row3[index - 1] = player
                break
            else:
                print("already played in that position, try again")
                row, index = choice(player)


def win(lista1, lista2, lista3):
    if lista1[0] == lista1[1] and lista1[0] == lista1[2]:
        return 1
    elif lista2[0] == lista2[1] and lista2[0] == lista2[2]:
        return 1
    elif lista3[0] == lista3[1] and lista3[0] == lista3[2]:
        return 1
    elif lista1[0] == lista2[1] and lista1[0] == lista3[2]:
        return 1
    elif lista1[2] == lista2[1] and lista1[2] == lista3[0]:
        return 1
    elif lista1[0] == lista2[0] == lista3[0] == "X" or lista1[0] == lista2[0] == lista3[0] == "O":
        return 1
    elif lista1[1] == lista2[1] == lista3[1] == "X" or lista1[1] == lista2[1] == lista3[1] == "O":
        return 1
    elif lista1[2] == lista2[2] == lista3[2] =="X" or lista1[2] == lista2[2] == lista3[2] =="X":
        return 1
    else:
        return 0


player1, player2 = pick_x_or_o()
moves = 0

while True:
    player1_row, player1_index = choice("player1")
    change_board(player1_row, player1_index, player1)
    moves +=1
    display(row1, row2, row3)
    check = win(row1, row2, row3)
    if check == 1:
        print("Congrats player1, just won a round")
        break
    if moves > 8:
        break
    player2_row, player2_index = choice("player2")
    change_board(player2_row, player2_index, player2)
    display(row1, row2, row3)
    check = win(row1, row2, row3)
    moves += 1
    if check == 1:
        print("Congrats player2, just won a round")
        break
    if moves > 8:
        break