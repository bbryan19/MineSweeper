import Piece
import random

class Board():
    def __init__(self, row, col, mine_count):
        self.row = row
        self.col = col
        self.mine_count = mine_count
        self.layout = []
        size = row * col

        # Create all board pieces
        for i in range(self.col):
            piece_row = []
            for i in range(self.row):
                piece = Piece.Piece(0)
                piece_row.append(piece)
            self.layout.append(piece_row)

        # Generate random mines
        mine_indeces = []
        for i in range(mine_count):
            r = random.randint(0, size - 1)

            while r in mine_indeces:
                r = random.randint(0, size - 1)

            mine_indeces.append(r)
        # print(mine_indeces)

        # Set mine_count amount of random mines
        for idx in mine_indeces:
            col_idx = idx % self.row
            row_idx = (idx - col_idx) // self.row
            # print(row_idx, col_idx)
            self.layout[row_idx][col_idx].set_value(-1)


        for row_idx, piece_row in enumerate(self.layout):
            for col_idx, piece in enumerate(piece_row):
                if piece.get_value() != -1:
                    # Determine if each neighbor of each piece is mine or not mine
                    for i in (-1, 0 , 1):
                        for j in (-1, 0, 1):
                            if ((j + col_idx >= 0 and j + col_idx < col) and (i + row_idx >= 0 and i + row_idx < row) and
                                not (i == 0 and j == 0)):
                                if self.layout[row_idx + i][col_idx + j].value == -1:
                                    self.layout[row_idx][col_idx].increment()



    def __str__(self):
        board_str = ''
        for row in self.layout:
            for i, value in enumerate(row):
                if i == len(row) - 1:
                    board_str += f'{value}\n'
                else:
                    board_str += f'{value}, '

        return f'Board Info\nDimensions: {self.row}x{self.col}\nMine Total: {self.mine_count}\n\n{board_str}'

