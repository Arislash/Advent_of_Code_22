list = open('6_input.txt', 'r')
line = list.readline()
length = 0
sana = ""

#Parse the next 14 characters from input
for i in range(len(line)):
    word = ""
    #Length of the word we want to examine. 4 for first assigment and 14 for part 2
    word = line[i:i+14]
    #Make a new string out of unique characters in the string
    sana = "".join(set(word))
    #If there are no duplicates, the lengths are the same and that is the marker we are after
    if (len(sana) == len(word)):
        length += i + 14
        break

#Return position of the last marker character
print(length)