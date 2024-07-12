class AITicTacToe:
    def __init__(self, board, player):
        self.board = board
        self.ai_player = 'O' if player == 'X' else 'X'
        self.human_player = player

    def is_moves_left(self):
        for row in self.board:
            for cell in row:
                if cell is None:
                    return True
        return False

    def evaluate(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2]:
                if self.board[row][0] == self.ai_player:
                    return 10
                elif self.board[row][0] == self.human_player:
                    return -10

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                if self.board[0][col] == self.ai_player:
                    return 10
                elif self.board[0][col] == self.human_player:
                    return -10

        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == self.ai_player:
                return 10
            elif self.board[0][0] == self.human_player:
                return -10

        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == self.ai_player:
                return 10
            elif self.board[0][2] == self.human_player:
                return -10

        return 0

    def minimax(self, depth, is_max):
        score = self.evaluate()

        if score == 10 or score == -10:
            return score

        if not self.is_moves_left():
            return 0

        if is_max:
            best = -1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.ai_player
                        best = max(best, self.minimax(depth + 1, not is_max))
                        self.board[i][j] = None
            return best
        else:
            best = 1000
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] is None:
                        self.board[i][j] = self.human_player
                        best = min(best, self.minimax(depth + 1, not is_max))
                        self.board[i][j] = None
            return best

    def find_best_move(self):
        best_val = -1000
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    self.board[i][j] = self.ai_player
                    move_val = self.minimax(0, False)
                    self.board[i][j] = None
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move
