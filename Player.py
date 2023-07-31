class Player:
    def __init__(self, name):
        self.name = name


    def play(self, board):
        dead = 0
        win = 0
        while not dead and not win:
            print(board)
            # Take user input and make move
            print()
            move = input("Your move: ").split(',')

            if move[0] == 'flag':
                if not board.get_piece_at(int(move[1]), int(move[2])).is_open():
                    board.flag_piece(int(move[1]), int(move[2]))
                else:
                    print("Cannot Flag Opened Piece")
            else:
                move_row = int(move[0])
                move_col = int(move[1])

                current_piece = board.get_piece_at(move_row, move_col)

                if not current_piece.is_open():
                    board.reveal_piece(move_row, move_col)

                # if player chooses mine --> dead = 1
                if current_piece.is_mine():
                    dead = 1
                    print("YOU'VE STRUCK A MINE")

                if current_piece.is_empty() and not current_piece.is_flagged():
                    board.chain_open(move_row, move_col)

                # if player finds all mines by revealing every square that is not a mine --> win = 1
                if board.all_revealed():
                    win = 1
                    print("YOU FOUND ALL THE MINES")

        print(board)


    def __str__(self):
        return f'{self.name}'