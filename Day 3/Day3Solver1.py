import textwrap

with open("C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 3\\input3.txt") as f:
    f.seek(0)
    rawin = f.read()
megaCount = []
ordCount = []
split_info = rawin.split("\n")
for item in split_info:
    try:
        holder = textwrap.wrap(item, int((len(item) / 2)))
        checkedLetters = []
        for i in range(len(holder[0])):
            count = 0
            letter = ""
            for t in range(len(holder[0])):
                if holder[0][i] == holder[1][t] and holder[1][t] not in checkedLetters:
                    print(holder[0], holder[1], holder[0][i], holder[1][t], i, t)
                    checkedLetters.append(holder[1][t])
                    if holder[0][i].islower():
                        print(holder[0][i])
                        ordCount.append(ord(holder[0][i]) - 96)
                    elif holder[0][i].isupper():
                        print(holder[0][i])
                        ordCount.append(ord(holder[0][i]) - 38)
    except ValueError:
        break
print(ordCount)
max = 0
for i in range(0, len(ordCount)):
    max += ordCount[i]
print(max)
print(len(ordCount))
"""for t in range(len(item)):
        for c in range(t + 1, len(item)):
            if item[t] == item[c]:
                print(item[t], item[c])
                mainCount += 1
        if mainCount > 1:
            megaCount.append(mainCount)
        mainCount = 1
    megaCount.append("break")
    print(item + " - " + str(mainCount) + " kordust")"""
