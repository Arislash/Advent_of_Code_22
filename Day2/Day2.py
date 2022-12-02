#A = Rock
#B = Paper
#C = Scissors
#X = Rock, 1p
#Y = Paper, 2p
#Z = Scissors, 3p
#Loss = 0p
#Tie = 3p
#Win = 6p
totalpoints = 0
roundpoints = 0
points = 0
results = open('2_input.txt', 'r')
for line in results:
    x = line.split(' ')
    x[1] = x[1].removesuffix('\n')
    if (x[1] == "X"):
        points = 1
    if (x[1] == "Y"):
        points = 2
    if (x[1] == "Z"):
        points = 3
    
    match x[0]:
        case "A":
            if(x[1] == "X"):
                roundpoints = 3
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Y"):
                roundpoints = 6
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Z"):
                roundpoints = 0
                totalpoints = totalpoints + points + roundpoints
        case "B":
            if(x[1] == "X"):
                roundpoints = 0
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Y"):
                roundpoints = 3
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Z"):
                roundpoints = 6
                totalpoints = totalpoints + points + roundpoints
        case "C":
            if(x[1] == "X"):
                roundpoints = 6
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Y"):
                roundpoints = 0
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Z"):
                roundpoints = 3
                totalpoints = totalpoints + points + roundpoints
print(totalpoints)

roundpoints = 0
totalpoints = 0
points = 0

results = open('2_input.txt', 'r')
for line in results:
    x = line.split(' ')
    x[1] = x[1].removesuffix('\n')
    match x[0]:
        case "A":
            #x = Loss, Y = Draw, Z = Win
            if(x[1] == "X"):
                roundpoints = 0
                points = 3
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Y"):
                roundpoints = 3
                points = 1
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Z"):
                roundpoints = 6
                points = 2
                totalpoints = totalpoints + points + roundpoints
        case "B":
            if(x[1] == "X"):
                roundpoints = 0
                points = 1
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Y"):
                roundpoints = 3
                points = 2
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Z"):
                roundpoints = 6
                points = 3
                totalpoints = totalpoints + points + roundpoints
        case "C":
            if(x[1] == "X"):
                roundpoints = 0
                points = 2
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Y"):
                roundpoints = 3
                points = 3
                totalpoints = totalpoints + points + roundpoints
            if(x[1] == "Z"):
                roundpoints = 6
                points = 1
                totalpoints = totalpoints + points + roundpoints
                
print(totalpoints)