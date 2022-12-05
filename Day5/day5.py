list = open('5_input.txt', 'r')
lines = list.readlines()

i = 1

#make list variables
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
list8 = []
list9 = []

#Make dictionaries to access list variables based on input number
boxcreate = {
    1 : list1,
    5 : list2,
    9 : list3,
    13 : list4,
    17 : list5,
    21 : list6,
    25 : list7,
    29 : list8,
    33 : list9
}

boxdict = {
    1 : list1,
    2 : list2,
    3 : list3,
    4 : list4,
    5 : list5,
    6 : list6,
    7 : list7,
    8 : list8,
    9 : list9
}

#Parse the box stacks from input
for line in lines:
    if (line[1] == "1"):
        break
    line = line.removesuffix('\n')
    i = 1
    for i in range(1,34,4):  
        if(i > len(line)): # Stop loop if i is out of bounds
            break
        if(line[i] != " "): # Stop from adding empty entries into list
                boxcreate[i].append(line[i])


#reverse the lists
for i in range(1, 10):
    boxdict[i].reverse()

src = 0
dest = 0
amount = 0
words = []
helplist = []

#Function to move around boxes within the lists based on the order parsed from input
for line in lines:
    if (line[0] == "m"):
        line = line.removesuffix('\n')
        words = line.split(' ')
        amount = int(words[1])
        src = int(words[3])
        dest = int(words[5])
        for i in range(amount):
#           boxdict[dest].append(boxdict[src].pop()) Part 1 function
            helplist.append(boxdict[src].pop())
        for i in range(amount):
            boxdict[dest].append(helplist.pop())

#print top box of each stack
print(f"{list1[-1]} + {list2[-1]} + {list3[-1]} + {list4[-1]} + {list5[-1]} + {list6[-1]} + {list7[-1]} + {list8[-1]} + {list9[-1]}")


