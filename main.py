import pygame
from game import TicTacToe
from ai_tictactoe import AITicTacToe
import sys
from button import Button

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')

# Create buttons for player selection
x_button = Button(screen, 200, 250, 200, 50, 'Play as X')
o_button = Button(screen, 200, 350, 200, 50, 'Play as O')
exit_button = Button(screen, 200, 450, 200, 50, 'Exit')

def show_menu():
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 74)
    text = font.render('Choose your side', True, (0, 0, 0))
    screen.blit(text, (100, 150))
    x_button.draw()
    o_button.draw()
    exit_button.draw()
    pygame.display.flip()

def main_menu():
    player = None
    while player not in ['X', 'O', 'Exit']:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if x_button.is_clicked(pygame.mouse.get_pos()):
                    player = 'X'
                elif o_button.is_clicked(pygame.mouse.get_pos()):
                    player = 'O'
                elif exit_button.is_clicked(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
        
        show_menu()
    return player

# Main loop
running = True
while running:
    player = main_menu()
    if player == 'Exit':
        running = False
        break

    game = TicTacToe(screen, player)
    ai = AITicTacToe(game.board, player)

    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game.game_over:
                    if game.reset_button.is_clicked(pygame.mouse.get_pos()):
                        game = TicTacToe(screen, player)  # Reset the game instance
                        ai = AITicTacToe(game.board, player)  # Reset the AI instance
                    elif game.menu_button.is_clicked(pygame.mouse.get_pos()):
                        game_running = False
                    elif game.exit_button.is_clicked(pygame.mouse.get_pos()):
                        running = False
                        game_running = False
                elif not game.game_over:
                    game.handle_click(pygame.mouse.get_pos())

        if not game.game_over and game.current_player != player:
            ai_move = ai.find_best_move()
            game.handle_ai_move(ai_move)

        # Draw the game
        game.draw()

        # Update the display
        pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
