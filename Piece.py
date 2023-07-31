class Piece():
    def __init__(self, value):
        self.state = 0
        self.value = value
        self.flag = 0


    #state.setter
    def open_piece(self):
        if not self.is_flagged():
            self.state = 1


    #state.getter
    def is_open(self):
        return self.state


    #flag.setter
    def set_flag(self, flag):
        self.flag = flag


    #flag.getter
    def is_flagged(self):
        return self.flag


    def get_value(self):
        return self.value

    #value.setter
    def set_value(self, value):
        self.value = value

    def increment(self):
        self.value += 1

    def is_mine(self):
        return (self.value < 0)

    def is_empty(self):
        return not self.value


    def __str__(self):
        # return f'{self.value}'
        piece_str = ''
        if self.state:
            piece_str = f'{self.value}'
        else:
            if self.flag:
                piece_str = 'M'
            else:
                piece_str = '*'

        return piece_str
