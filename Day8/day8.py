list = open('8_input.txt', 'r')
lines = list.readlines()

#Initialize nested list to keep track of trees in the forest
forest = []

#Populate the nested list
for r, line in enumerate(lines):
    forest.append([])
    line = line.removesuffix('\n')
    for c in range(len(line)):
        forest[r].append(int(line[c]))
print(forest)

visible = 0
currentTree = 0
currentVisible = 0

maxVision = 0
totalVision = 0

#This function is used to calculate the amount of visibility each tree has
for r in range(len(forest)):
    for c in range(len(forest[r])):
        #If the current tree is on the edge, add +1 to visibility and move on to the next tree
        if ((r == 0) or (c == 0) or (c == int(len(forest[r]))-1) or (r == int(len(forest))-1)):
            visible += 1
            continue
        #Variable to keep track of when a tree is found to be visible to the edge
        #When found, moves on to next tree since being visible to multiple edges is not relevant
        #This is disabled during the 2nd assignment since we need to calculate visibility on all sides
        currentVisible = visible

        leftVision = 1
        rightVision = 1
        upVision = 1
        downVision = 1
        
        #Calculate visibility to the right
        for i in range(c+1,len(forest[r])):
            if (forest[r][c] > forest[r][i]):
                if (i == int(len(forest[r]))-1):
                    visible += 1
                    break
                else:
                    rightVision += 1
            else:
                break
      #  if (currentVisible != visible):
      #      continue
        
        #Calculate visibility to the left
        for i in range(c-1,-1,-1):
            if (forest[r][c] > forest[r][i]):
                if (i == 0):
                    visible += 1
                    break
                else:
                    leftVision += 1
            else:
                break
            
      #  if (currentVisible != visible):
      #      continue
        #Calculate visibility downvards            
        for j in range(r+1,len(forest)):
            if(forest[r][c] > forest[j][c]):
                if (j == int(len(forest))-1):
                    visible += 1
                    break
                else:
                    downVision += 1
            else:
                break
            
      #  if (currentVisible != visible):
      #      continue            
        #Calculate visibility upwards    
        for j in range(r-1, -1 ,-1):
            if(forest[r][c] > forest[j][c]):
                if (j == 0):
                    visible += 1
                    break
                else:
                    upVision += 1
            else:
                break
        #Figure out the total amount of vision, and see if its more on that tree than the current best    
        totalVision = (rightVision * leftVision * upVision * downVision)
        if (totalVision > maxVision):
            maxVision = totalVision
        
#Because the code is modified to currently print max vision, it would need the continue statements to work for part one task
print(maxVision)
