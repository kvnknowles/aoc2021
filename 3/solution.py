f = open("input.txt", "r")

commands = []
for x in f:
    commands.append(x)

result = []
for x in range(len(commands[0])-1):
    result.append(0)
for line in commands:
    for x in range(len(line)-1):
        result[x] += int(line[x])

total = []
mid = len(commands)/2
for x in result:
    if x >= mid:
        total.append('1')
    else:
        total.append('0')

first = ''.join(total)
a = int(first ,2)
print(a)

other = ''.join('1' if x == '0' else '0' for x in first)
b = int(other, 2)

print a*b
