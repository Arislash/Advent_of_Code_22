import array

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
print(total)

#---- SECOND TASK ------


array = [""] * 3
i = 0
badge = ""
total = 0
points = 0
#Group 3 lines into an array of strings
for line in lines:
    if i < 3:
        line = line.removesuffix('\n')
        array[i] = line
        i = i + 1
    else:
        i = 0
        #Find out what the common character between 3 strings is
        #Is this broken?
        for c in array[0]:
            index = array[1].find(c)
            if index != -1:
                character = array[1][index]
                index = array[2].find(character)
                if index != -1:
                    badge = array[2][index]
                    print(badge)
                    break
        #Calculate total value of common characters
        #Or maybe this?
        if character.isupper():
            points = ord(badge) - 38
            total = points + total
        if character.islower():
            points = ord(badge) - 96
            total = points + total
print(total)