with open("C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 6\\input6.txt") as f:
    f.seek(0)
    rawin = f.read()
supermegaList = []
for i in range(len(rawin)):
    superList = []
    if i >= 13:
        for a in range(0, 14):
            superList.append(rawin[i - a])
    superList.append(i + 1)
    supermegaList.append(superList)
iterationNumber = 0
print(supermegaList)
for i in range(len(supermegaList)):
    if len(set(supermegaList[i])) == 15:
        print("hooray on ", supermegaList[i][14])
print(iterationNumber)
