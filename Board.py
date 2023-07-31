import Piece
import random

class Board():
    def __init__(self, row, col, mine_count):
        self.row = row
        self.col = col
        self.mine_count = mine_count
        self.layout = []
        self.reveal_count = 0
        self.size = row * col

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
            r = random.randint(0, self.size - 1)

            while r in mine_indeces:
                r = random.randint(0, self.size - 1)

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


    def get_layout(self):
        return self.layout


    # return < 0 is mine
    def get_piece_at(self, row, col):
        return self.layout[row][col]


    # Changes piece state to 1
    def reveal_piece(self, row, col):
        self.layout[row][col].open_piece()
        self.reveal_count += 1


    def all_revealed(self):
        return 1 if self.reveal_count == self.size - self.mine_count else 0


    def chain_open(self, row_idx, col_idx):
        current_piece = self.get_piece_at(row_idx, col_idx)

        if not current_piece.is_empty():
            current_piece.open_piece()
            return

        current_piece.open_piece()

        for i in (-1, 0 , 1):
            for j in (-1, 0, 1):
                if ((j + col_idx >= 0 and j + col_idx < self.col) and (i + row_idx >= 0 and i + row_idx < self.row) and
                    not (i == 0 and j == 0)):
                    neighbor_piece = self.get_piece_at(row_idx + i, col_idx + j)
                    if not neighbor_piece.is_open() and not neighbor_piece.is_mine():
                        self.chain_open(row_idx + i, col_idx + j)


    def flag_piece(self, row, col):
        piece = self.get_piece_at(row, col)
        if piece.is_flagged():
            piece.set_flag(0)
            self.mine_count += 1
        else:
            piece.set_flag(1)
            self.mine_count -= 1


    def __str__(self):
        board_str = ''
        out_str = ''
        output = 'out.csv'
        for row in self.layout:
            for i, piece in enumerate(row):
                if i == len(row) - 1:
                    board_str += f'{piece}\n'
                    out_str += f'{piece.get_value()}\n'
                else:
                    board_str += f'{piece}, '
                    out_str += f'{piece.get_value()}, '

        f = open(output, 'w')
        f.write(out_str)
        f.close()

        return f'Board Info\nDimensions: {self.row}x{self.col}\nMines Left: {self.mine_count}\n\n{board_str}'

