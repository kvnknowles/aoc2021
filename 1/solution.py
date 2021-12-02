def print_increase_count(numbers):
    increase_count = 0
    previous = 10000000
    for i in numbers:
        if i > previous:
            increase_count += 1
        previous = i

    print(increase_count)

f = open("input.txt", "r")

numbers = []
for x in f:
    numbers.append(int(x))
print_increase_count(numbers)

sliding_numbers = []
starting = 0
for x in range(len(numbers) - 2):
    sliding_numbers.append(numbers[starting]+numbers[starting+1]+numbers[starting+2])
    starting += 1

print_increase_count(sliding_numbers)
