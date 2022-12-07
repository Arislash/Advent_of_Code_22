#Make Folder Class
class Folder:
    def __init__(self, folderName, folderParent):
        self.name = folderName
        self.parent = folderParent
        self.child = None
        self.size = 0
    
    def setChild(self, folderChild):
        self.child = folderChild
        
    def setSize(self, folderSize):
        self.size = folderSize
        
    def __str__(self):
        return f"{self.name} size is {self.size}. Its located in {self.parent.name} and contains these items:"
        
    
#Make File Class
class File:
    def __init__(self, fileName, fileSize, fileParent):
        self.name = fileName
        self.size = fileSize
        self.parent = fileParent
        
    def __str__(self):
        return f"{self.name} Size is {self.size}. It is located in the folder {self.parent.name}"
        
     
     
list = open('7_input.txt', 'r')
lines = list.readlines()

fileTree = {}
currentFolder = None
previousFolder = None
currentPath = ""

#Find out if line is a command or a file
for line in lines:
    info = line.split()
    if (info[0] == "$"):
        if (info[1] == "cd"):
            #If traversing back to parent directory
            if (info[2] == ".."):
                currentPath = currentPath.removesuffix(currentFolder.name)
                currentPath = currentPath.removesuffix("/")
                previousFolder.size += currentFolder.size
                currentFolder = previousFolder
                previousFolder = currentFolder.parent
            else:
                #When making root folder, handle it differently to not have extra / characters in path
                if (info[2] == "/"):
                    currentPath = "/"
                    fileTree[currentPath] = Folder(info[2], currentFolder)
                    previousFolder = currentFolder
                    currentFolder = fileTree[currentPath]
                    fileTree[currentPath].parent = fileTree[currentPath]
                else:
                    #When making a new folder and then moving into it
                    currentPath += "/" + info[2]
                    fileTree[currentPath] = Folder(info[2], currentFolder)
                    previousFolder = currentFolder
                    currentFolder = fileTree[currentPath]
        #If command ls is used, that line can just be ignored and move to the next one
        else:
            continue
    #Since folders are already made with "$cd foldername" command, we can just ignore the "dir foldername" lines
    #This handles making files when not in the root directory. Otherwise we would end up with an extra "/" in path
    elif (info[0] != "dir"):
        if (currentPath != "/"):
            currentPath += "/" + info[1]
        else:
            #If in root, just add the name of the file to current path
            currentPath += info[1]
        #Create a new file to current path
        fileTree[currentPath] = File(info[1], int(info[0]), currentFolder)
        currentFolder.size += int(info[0])
        currentPath = currentPath.removesuffix(info[1])
        currentPath = currentPath.removesuffix("/")

#After list is done, traverse back to root while updating folder sizes with their items. 
while currentFolder != fileTree["/"]:
    currentPath 
    previousFolder.size += currentFolder.size
    currentFolder = previousFolder
    previousFolder = currentFolder.parent


folderlist = []
sizesum = 0
sum = 0
smallestFolder = []

#Find out which folders are below the size 100000
for i in fileTree:
    if(isinstance(fileTree[i], Folder)):
        sum += fileTree[i].size
        if(fileTree[i].size <= 100000):
            folderlist.append(fileTree[i].name)
            sizesum += fileTree[i].size
            
#Find out sizes of all folders that are above the minimum size requirement and make a list
for i in fileTree:
    if(isinstance(fileTree[i], Folder)):
        if(fileTree[i].size >= 7048086):
            smallestFolder.append(fileTree[i].size)

#Sort the list in descending order
smallestFolder.sort()

#First item is smallest folder above the required space
print(smallestFolder)