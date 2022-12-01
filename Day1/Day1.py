import array

elf = 0
maxvalue = 0
topthree = [0] * 3

calories = open('input_1.txt', 'r')
for line in calories:
    if (line != "\n"):
        elf += int(line)
        if (elf > maxvalue):
            maxvalue = elf
            elf = 0
    else:
        elf = 0
print(f"Elf with most calories: {maxvalue}")
elf = 0

calories = open('input_1.txt', 'r')
for line in calories:
    if (line != "\n"):
        elf += int(line)
    else:
        if (elf > topthree[0]):
            topthree[2] = topthree[1]
            topthree[1] = topthree[0]
            topthree[0] = elf
            elf = 0
        else:
            if (elf > topthree[1]):
                topthree[2] = topthree[1]
                topthree[1] = elf
                elf = 0
            else:
                if (elf > topthree[2]):
                    topthree[2] = elf
                    elf = 0
        elf = 0
print(f"Combined calories of the 3 top elves: {topthree[0] + topthree[1] + topthree[2]}")