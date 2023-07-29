class Piece():
    def __init__(self, value):
        self.state = 0
        self.value = value
        self.flag = 0


    #state.setter
    def open_piece(self):
        self.state = 1


    #state.getter
    def get_state(self):
        return self.state


    #flag.setter
    def set_flag(self, flag):
        self.flag = flag


    #flag.getter
    def get_flag(self):
        return self.flag


    def get_value(self):
        return self.value

    #value.setter
    def set_value(self, value):
        self.value = value

    def increment(self):
        self.value += 1


    def __str__(self):
        return f'{self.state}'
