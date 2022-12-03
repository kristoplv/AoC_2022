import textwrap

with open("C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 3\\input3.txt") as f:
    f.seek(0)
    rawin = f.read()
megaCount = []
ordCount = []
lastList = []
split_info = rawin.split("\n")
counter = 0
for i in range(len(split_info)):
    counter += 1
    megaCount.append(split_info[i])
    if counter == 3:
        ordCount.append(megaCount)
        megaCount = []
        counter = 0

for item in ordCount:
    bannedList = []
    for i in range(0, len(item[0])):
        for t in range(0, len(item[1])):
            for s in range(0, len(item[2])):
                if (
                    item[0][i] == item[1][t] == item[2][s]
                    and item[1][t] not in bannedList
                    and item[2][s] not in bannedList
                ):
                    print(item[0][i], item[1][t], item[2][s])
                    print(item[0], item[1], item[2])
                    bannedList.append(item[1][t])
                    if item[0][i].islower():
                        print(item[0][i])
                        lastList.append(ord(item[0][i]) - 96)
                    elif item[0][i].isupper():
                        print(item[0][i])
                        lastList.append(ord(item[0][i]) - 38)
    print(item)
print(sum(lastList))
