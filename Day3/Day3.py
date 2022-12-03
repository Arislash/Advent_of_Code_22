total = 0
points = 0

list = open('3_input.txt', 'r')
lines = list.readlines()

#-----FIRST TASK-----

#Split the string into half
for line in lines:
    line = line.removesuffix('\n')
    length = len(line)
    half = length / 2
    first = line[:int(length-half)]
    second = line[int(half):]


#Find the common character
    for c in first:
        index = second.find(c)
        character = second[index]
        if index != -1:
            break
    
#Calculate total value of common characters
    if character.isupper():
        points = ord(character) - 38
        total = points + total
    if character.islower():
        points = ord(character) - 96
        total = points + total
print(f"Total value of points: {total}")

#---- SECOND TASK ------


list = [""] * 3
i = 0
badge = ""
total = 0
points = 0
#Group 3 lines into an list of strings
for line in lines:
    line = line.removesuffix('\n')
    list[i] = line
    i = i + 1
    if i == 3:
        i = 0
        #Find out what the common character between 3 strings is
        for c in list[0]:
            index = list[1].find(c)
            if index != -1:
                character = list[1][index]
                index = list[2].find(character)
                if index != -1:
                    badge = list[2][index]
                    break
        #Calculate total value of common characters
        if badge.isupper():
            points = ord(badge) - 38
            total = points + total
        if badge.islower():
            points = ord(badge) - 96
            total = points + total
print(f"Total value of Badges: {total}")