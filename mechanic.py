class Board:
    def __init__(self, game):
        self.game = game
        self.board = [[Rook(1, 8, 'white'), Knight(2, 8, 'white'), Bishop(3, 8, 'white'), Queen(4, 8, 'white'),
                       King(5, 8, 'white'), Bishop(6, 8, 'white'), Knight(7, 8, 'white'), Rook(8, 8, 'white')],
                      [Pawn(i, 7, 'white') for i in range(1, 9)],
                      [None for _ in range(8)], [None for _ in range(8)],
                      [None for _ in range(8)], [None for _ in range(8)],
                      [Pawn(i, 2, 'black') for i in range(1, 9)],
                      [Rook(1, 7, 'black'), Knight(2, 7, 'black'), Bishop(3, 7, 'black'), Queen(4, 7, 'black'),
                       King(5, 7, 'black'), Bishop(6, 7, 'black'), Knight(7, 7, 'black'), Rook(8, 7, 'black')]]
        self.current_turn_color = 'white'
        self.history_of_moves = []

    def print_board(self):
        order_figures = [self.board[i][j] for i in range(7, -1, -1) for j in range(8)]
        while None in order_figures:
            order_figures[order_figures.index(None)] = '  '
        print("""
+——+——+——+——+——+——+——+——+
|{}|{}|{}|{}|{}|{}|{}|{}|   8
+——+——+——+——+——+——+——+——+
|{}|{}|{}|{}|{}|{}|{}|{}|   7
+——+——+——+——+——+——+——+——+
|{}|{}|{}|{}|{}|{}|{}|{}|   6
+——+——+——+——+——+——+——+——+
|{}|{}|{}|{}|{}|{}|{}|{}|   5
+——+——+——+——+——+——+——+——+
|{}|{}|{}|{}|{}|{}|{}|{}|   4
+——+——+——+——+——+——+——+——+
|{}|{}|{}|{}|{}|{}|{}|{}|   3
+——+——+——+——+——+——+——+——+
|{}|{}|{}|{}|{}|{}|{}|{}|   2
+——+——+——+——+——+——+——+——+
|{}|{}|{}|{}|{}|{}|{}|{}|   1
+——+——+——+——+——+——+——+——+
 1  2  3  4  5  6  7  8
""".format(*order_figures))

    def move(self, from_column: int, from_row: int, to_column: int, to_row: int):
        # TODO: реализвоать рокировку
        if not self.check_move(from_column, from_row, to_column, to_row):
            return False
        else:
            self.board[to_row - 1][to_column - 1] = self.board[from_row - 1][from_column - 1]
            self.board[from_row - 1][from_column - 1] = None
            self.current_turn_color = 'white' if self.current_turn_color == 'black' else 'black'
            self.print_board()
            return True

    def check_move(self, from_column: int, from_row: int, to_column: int, to_row: int):
        if False in [1 <= i <= 8 for i in (from_column, from_row, to_column, to_row)]:
            return False
        from_cell_figure = self.board[from_row - 1][from_column - 1]
        if from_cell_figure is None:
            return False
        if from_cell_figure.color != self.current_turn_color:
            return False
        if not from_cell_figure.possibility_of_move(self.board, from_column, from_row, to_column, to_row,
                                                    self.history_of_moves):
            return False
        if not self.possibility_of_move_pin(from_column, from_row, to_column, to_row):
            return False
        return True

    def possibility_of_move_pin(self, from_column: int, from_row: int, to_column: int, to_row: int):
        # TODO: реализовать проверку на связку
        return True

    def check_end(self):
        # TODO: реализовать проверку на конец игры (мат, пат, ничья)
        return False


class Figure:
    def __init__(self, column, row, color):
        self.column = column
        self.row = row
        self.color = color


class Pawn(Figure):
    def __str__(self):
        if self.color == 'white':
            return 'P '
        elif self.color == 'black':
            return 'p '

    def possibility_of_move(self, current_board, from_column, from_row, to_column, to_row, history_of_moves):
        # TODO: реализовать взятие на проходе
        if self.color == 'white':
            if not (1 <= to_row - from_row <= 2):
                return False

            if to_row - from_row == 2:
                if from_row != 2:
                    return False
                if from_column != to_column:
                    return False
                if (current_board[to_row - 2][from_column - 1] is not None) or (
                        current_board[to_row - 1][from_column - 1] is not None):
                    return False
                return True

            if from_column == to_column:
                print(current_board)
                if current_board[to_row - 1][from_column - 1] is not None:
                    return False
                return True

            to_cell = current_board[to_row - 1][to_column - 1]
            if to_cell is None:
                return False
            if to_cell.color != 'black':
                return False
            return True

        if self.color == 'black':
            if not (1 <= from_row - to_row <= 2):
                return False

            if from_row - to_row == 2:
                if from_row != 7:
                    return False
                if from_column != to_column:
                    return False
                if (current_board[to_row - 1][from_column - 1] is not None) or (
                        current_board[to_row - 1][from_column - 1] is not None):
                    return False
                return True

            if from_column == to_column:
                if current_board[to_row - 1][from_column - 1] is not None:
                    return False
                return True

            to_cell = current_board[to_row - 1][to_column - 1]
            if to_cell is None:
                return False
            if to_cell.color != 'white':
                return False
            return True


class Bishop(Figure):
    def __str__(self):
        if self.color == 'white':
            return 'B '
        elif self.color == 'black':
            return 'b '


class Knight(Figure):
    def __str__(self):
        if self.color == 'white':
            return 'KN'
        elif self.color == 'black':
            return 'kn'


class Rook(Figure):
    def __str__(self):
        if self.color == 'white':
            return 'R '
        elif self.color == 'black':
            return 'r '


class Queen(Figure):
    def __str__(self):
        if self.color == 'white':
            return 'Q '
        elif self.color == 'black':
            return 'q '


class King(Figure):
    def __str__(self):
        if self.color == 'white':
            return 'K '
        elif self.color == 'black':
            return 'k '

