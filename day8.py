# Part 1

# Find the value of Accumulator before an execution is ran a SECOND time

instructions = open("Advent_of_code_2020\\day8.txt", "r").read().split("\n")

not_second_time = True
index = 0
accumulator = 0
indexs = set()

while not_second_time == True:
    if index not in indexs:
        indexs.add(index)
    else:
        not_second_time = False
        print(f"Accumulator = {accumulator}")
        break

    _input =instructions[index]
    command = _input.split()[0]
    nextline = _input.split()[1]

    if command == "nop":
        index += 1
    elif command == "acc":
        if nextline[0] == "+":
            accumulator += int(nextline[1:])
        elif nextline[0] == "-":
            accumulator -= int(nextline[1:])
        index += 1
    elif command == "jmp":
        if nextline[0] == "+":
            index += int(nextline[1:])
        elif nextline[0] == "-":
            index -= int(nextline[1:])

# Part 2
# We need to change the command to try and get to the end of the program.
# However we only need to change the NOP and JMP commands around

brute_force = True
position = 0
accumulator = 0
instruction_index = set()

while brute_force:
    if position not in instruction_index:
        instruction_index.add(position)
    else:
        not_second_time = False
        print(f"Accumulator = {accumulator}")
        break

    _input =instructions[position]
    command = _input.split()[0]
    nextline = _input.split()[1]

    if command == "nop":
        position += 1
    elif command == "acc":
        if nextline[0] == "+":
            accumulator += int(nextline[1:])
        elif nextline[0] == "-":
            accumulator -= int(nextline[1:])
        position += 1
    elif command == "jmp":
        if nextline[0] == "+":
            position += int(nextline[1:])
        elif nextline[0] == "-":
            position -= int(nextline[1:])