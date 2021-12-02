f = open("input.txt", "r")

commands = []
for x in f:
    commands.append(x)

depth = 0
horizontal = 0

for x in commands:
    command, length = x.split(' ')
    if command.startswith('f'):
        horizontal += int(length)
    if command.startswith('d'):
        depth += int(length)
    if command.startswith('u'):
        depth -= int(length)

print(depth*horizontal)
