pairs = 0
overlaps = 0

list = open('4_input.txt', 'r')
lines = list.readlines()
list.close()

numbers1 = ""
numbers2 = ""
#Task 1 & 2
#Split the string into half
for line in lines:
    numbers1 = ""
    numbers2 = ""
    line = line.removesuffix('\n')
    ranges = line.split(",")
    #Put ranges into seperate variables
    first = ranges[0].split("-")
    second = ranges[1].split("-")
    #Turn them into a range
    range1 = range(int(first[0]), int(first[1])+1)
    range2 = range(int(second[0]), int(second[1])+1)
    #Make them into a set
    numbers1 = set(range1)
    numbers2 = set(range2)
    #Check if one set contains the other fully
    if numbers1.issubset(numbers2):
        pairs += 1
    elif numbers2.issubset(numbers1):
        pairs +=1   
    result = False
    #Check if there is any overlap between sets
    result = bool(numbers1 & numbers2)
    if result:
        overlaps += 1
print(f"Amount of ranges fully contained in the other: {pairs}")
print(f"Amount of ranges that overlapped: {overlaps}")