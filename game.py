import pygame
from button import Button

class TicTacToe:
    def __init__(self, screen, player):
        self.screen = screen
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 'X'
        self.player = player
        self.game_over = False
        self.winner = None
        self.reset_button = Button(screen, 250, 300, 100, 50, 'Restart')
        self.menu_button = Button(screen, 250, 360, 130, 50, 'Main Menu')
        self.exit_button = Button(screen, 250, 420, 100, 50, 'Exit')

    def draw_lines(self):
        for row in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), (0, row * 200), (600, row * 200), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (row * 200, 0), (row * 200, 600), 5)

    def draw_figures(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == 'X':
                    pygame.draw.line(self.screen, (0, 0, 0), (col * 200 + 55, row * 200 + 55),
                                     (col * 200 + 145, row * 200 + 145), 15)
                    pygame.draw.line(self.screen, (0, 0, 0), (col * 200 + 145, row * 200 + 55),
                                     (col * 200 + 55, row * 200 + 145), 15)
                elif self.board[row][col] == 'O':
                    pygame.draw.circle(self.screen, (0, 0, 0), (col * 200 + 100, row * 200 + 100), 45, 15)

    def handle_click(self, pos):
        if not self.game_over:
            row = pos[1] // 200
            col = pos[0] // 200
            if self.board[row][col] is None:
                self.board[row][col] = self.current_player
                if self.check_winner():
                    self.game_over = True
                elif self.check_draw():
                    self.game_over = True
                    self.winner = "Draw"
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            if self.reset_button.is_clicked(pos):
                self.reset()

    def handle_ai_move(self, move):
        if move != (-1, -1):
            self.board[move[0]][move[1]] = self.current_player
            if self.check_winner():
                self.game_over = True
            elif self.check_draw():
                self.game_over = True
                self.winner = "Draw"
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] is not None:
                self.winner = self.board[row][0]
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] is not None:
                self.winner = self.board[0][col]
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] is not None:
            self.winner = self.board[0][0]
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] is not None:
            self.winner = self.board[0][2]
            return True

        return False

    def check_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    return False
        return True

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.draw_lines()
        self.draw_figures()
        if self.game_over:
            font = pygame.font.Font(None, 74)
            if self.winner == "Draw":
                text = font.render('Draw!', True, (250, 0, 0))
            else:
                text = font.render(f'{self.winner} wins!', True, (250, 0, 0))
            self.screen.blit(text, (200, 200))  # Move the text up
            self.reset_button.draw()
            self.menu_button.draw()
            self.exit_button.draw()

    def reset(self):
        self.board = [[None] * 3 for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
