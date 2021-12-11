from board import Board

f = open("input.txt", "r")

called = f.readline()
called_numbers = [int(x) for x in called.split(',')]
print(called_numbers)

f.readline()

count = 0
numbers = []
boards = []
for x in f:
    if count < 5:
        numbers.extend([int(num) for num in x.split()])
        count += 1
    elif count == 5:
        board1 = Board(numbers)
        boards.append(board1)
        numbers = []
        count = 0
print(numbers)
boards.append(Board(numbers))
print(len(boards))

winner = False
for cur_num in called_numbers:
    if winner:
        break
    for b in boards:
        b.mark(cur_num)
        if b.is_winner():
            winner = True
            print("Winner " + str(b.calc_score()))
            break
