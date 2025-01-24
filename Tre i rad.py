import pygame
import sys

matrix = [[" ", " "," "], 
          [" ", " "," "],
          [" ", " "," "]]


__author__  = "Ott Rudolf Pöld"
__version__ = "2.0.0"
__email__   = "Ott.Pold@elev.ga.ntig.se"

pygame.init()

width, height = 300, 300
line_color = (10, 10, 10)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

def draw_board():
    screen.fill((255, 255, 255))
    for row in range(1, 3):
        pygame.draw.line(screen, line_color, (0, row * 100), (300, row * 100), 5)
    for col in range(1, 3):
        pygame.draw.line(screen, line_color, (col * 100, 0), (col * 100, 300), 5)


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

def main():
    player_turn = 'X'
    draw_board()
    pygame.display.update()

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

if __name__ == "__main__":
    main()