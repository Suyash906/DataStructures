class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.rows = [0 for _ in range(n)]
        self.cols = [0 for _ in range(n)]
        self.main_diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        
        self.rows[row] += 1 if player == 1 else -1
        self.cols[col] += 1 if player == 1 else -1
        
        if row == col:
            self.main_diagonal += 1 if player == 1 else -1
        
        if row+col == self.n-1:
            self.anti_diagonal +=  1 if player == 1 else -1
        
        # print(self.anti_diagonal)
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.main_diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
