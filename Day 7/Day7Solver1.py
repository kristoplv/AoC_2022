with open("C:\\Users\Marleen\\OneDriveUUS\\OneDrive\\Dokumendid\\AoC_2022\\Day 7\\input7.txt") as f:
    f.seek(0)
    rawin = f.read().split("\n")
fileHierarchy =[]
for i in range(len(rawin)):
    if i < 12 and rawin[i][0] != "$":
        fileHierarchy.append(rawin[i])
    ## NO MORE THAN 100 000
print(fileHierarchy)
