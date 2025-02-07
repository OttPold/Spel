import pygame
import sys
import random

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
        
def handle_game_result(result):
    print(result)
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def handle_human_move(row, col, current_player):
    matrix[row][col] = current_player
    new_player = 'O' if current_player == 'X' else 'X'
    
    draw_board()
    draw_marks()
    display_board()
    pygame.display.update()
    
    result = check_board()
    if result:
        handle_game_result(result)
    return new_player

def handle_computer_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if matrix[r][c] == " "]
    if empty_cells:
        r, c = random.choice(empty_cells)
        matrix[r][c] = 'O'
        
        draw_board()
        draw_marks()
        display_board()
        pygame.display.update()
        
        result = check_board()
        if result:
            handle_game_result(result)

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
                    game_loop(vs_computer=False) # pvp
                elif pvc_button.collidepoint(x, y):
                    game_loop(vs_computer=True) # pvc

def game_loop(vs_computer=False):
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
                if vs_computer and player_turn != 'X':
                    continue  
                
                x, y = event.pos
                col, row = x // 100, y // 100
                if matrix[row][col] == " ":
                    player_turn = handle_human_move(row, col, player_turn)
                    
                    if vs_computer and player_turn == 'O':
                        handle_computer_move()
                        player_turn = 'X'



if __name__ == "__main__":
    main_menu()