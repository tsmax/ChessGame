import mechanic, ui


class Game:
    def __init__(self):
        self.mechanic_board = mechanic.Board(self)
        self.app = ui.App(self)
        self.window = self.app.window

    def check_move(self, move):
        columns = list('_abcdefgh')
        from_column, from_row, to_column, to_row = columns.index(move[0]), int(move[1]), columns.index(move[2]), int(move[3])
        return self.mechanic_board.move(from_column, from_row, to_column, to_row)


if __name__ == '__main__':
    game = Game()