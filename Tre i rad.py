matrix = [[" ", " "," "], 
          [" ", " "," "],
          [" ", " "," "]]


def display_board():
    for row in matrix:
        print(" | ".join(row))
        print("-" * 10)

def check_board():
    for row in matrix:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return f"{row[0]} wins!"
    

    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != " ":
            return f"{matrix[0][col]} wins!"

    
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != " ":
        return f"{matrix[0][0]} wins!"
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != " ":
        return f"{matrix[0][2]} wins!"



    if all(cell != " " for row in matrix for cell in row):
        return "It's a draw!"

    return None


while True:
    display_board()
    result = check_board()
    if result:
        print(result)
        break

    p1_row = int(input("Player 1 - Ange rad (0, 1, 2 ): "))
    p1_col = int(input("Player 1 - Ange rad (0, 1, 2 ): "))
    if matrix[p1_row][p1_col] == " ":
        matrix[p1_row][p1_col] = "X"

    display_board()
    result = check_board()
    if result:
        print(result)
        break

    p2_row = int(input("Player 2 - Ange rad (0, 1, 2 ): "))
    p2_col = int(input("Player 2 - Ange rad (0, 1, 2 ): "))
    if matrix[p2_row][p2_col] == " ":
        matrix[p2_row][p2_col] = "O"

