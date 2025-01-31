import pygame
import sys

matrix = [[" ", " "," "], 
          [" ", " "," "],
          [" ", " "," "]]


__author__  = "Ott Rudolf Pöld"
__version__ = "4.0.0"
__email__   = "Ott.Pold@elev.ga.ntig.se"

pygame.init()

width, height = 300, 300
line_color = (10, 10, 10)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic-Tac-Toe")

x_img = pygame.image.load('x.png')
o_img = pygame.image.load('o.png')
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(o_img, (80, 80))

def draw_board():
    screen.fill((255, 255, 255))
    for row in range(1, 3):
        pygame.draw.line(screen, line_color, (0, row * 100), (300, row * 100), 5)
    for col in range(1, 3):
        pygame.draw.line(screen, line_color, (col * 100, 0), (col * 100, 300), 5)

def draw_marks():
    for row in range(3):
        for col in range(3):
            if matrix[row][col] == 'X':
                screen.blit(x_img, (col * 100 + 10, row * 100 + 10))
            elif matrix[row][col] == 'O':
                screen.blit(o_img, (col * 100 + 10, row * 100 + 10))

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

def main_menu():
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    title_text = font.render("Tic-Tac-Toe", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(width//2, 50))
    screen.blit(title_text, title_rect)

    pvp_button = pygame.Rect(50, 100, 200, 50)
    pygame.draw.rect(screen, (0, 200, 0), pvp_button)
    pvp_text = font.render("Player vs Player", True, (0, 0, 0))
    pvp_text_rect = pvp_text.get_rect(center=pvp_button.center)
    screen.blit(pvp_text, pvp_text_rect)

    #kmr adda detta vs computer sak senare
    pvc_button = pygame.Rect(30, 160, 240, 50)
    pygame.draw.rect(screen, (0, 0, 200), pvc_button)
    pvc_text = font.render("Player vs Computer", True, (0, 0, 0))
    pvc_text_rect = pvc_text.get_rect(center=pvc_button.center)
    screen.blit(pvc_text, pvc_text_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pvp_button.collidepoint(x, y):
                    pvp_game()
                elif pvc_button.collidepoint(x, y):
                    pvc_game()

                
def pvp_game():
    player_turn = 'X'
    draw_board()
    draw_marks()
    display_board()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // 100, y // 100
                if matrix[row][col] == " ":
                    matrix[row][col] = player_turn
                    player_turn = 'O' if player_turn == 'X' else 'X'
                    draw_board()
                    draw_marks()
                    display_board()
                    pygame.display.update()

                    result = check_board()
                    if result:
                        print(result)
                        pygame.time.wait(2000)
                        pygame.quit()
                        sys.exit()



if __name__ == "__main__":
    main_menu()