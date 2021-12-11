class Board():
    def __init__(self, board_input):
        self.board_input = board_input
        self.last_called = -1

    def get_potential_rows(self):
        row1 = slice(0, 5)
        row2 = slice(5, 10)
        row3 = slice(10, 15)
        row4 = slice(15, 20)
        row5 = slice(20, 25)
        return [self.board_input[row1], self.board_input[row2], self.board_input[row3], self.board_input[row4],
                self.board_input[row5]]

    def get_potential_columns(self):
        column1 = slice(0, 25, 5)
        column2 = slice(1, 25, 5)
        column3 = slice(2, 25, 5)
        column4 = slice(3, 25, 5)
        column5 = slice(4, 25, 5)
        return [self.board_input[column1], self.board_input[column2], self.board_input[column3],
                self.board_input[column4], self.board_input[column5]]

    def get_potential_winners(self):
        return self.get_potential_rows() + self.get_potential_columns()

    def mark(self, number_called):
        if number_called in self.board_input:
            index = self.board_input.index(number_called)
            self.board_input[index] = 'x'
        self.last_called = number_called

    def is_winner(self):
        return ['x', 'x', 'x', 'x', 'x'] in self.get_potential_winners()

    def calc_score(self):
        sum = 0
        for x in self.board_input:
            if x != 'x':
                sum += int(x)
        return sum * self.last_called
