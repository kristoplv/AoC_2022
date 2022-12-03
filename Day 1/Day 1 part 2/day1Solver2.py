with open(
    "C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 1\\Day 1 part 2\\input.txt"
) as f:
    f.seek(0)
    rawin = f.read()

elves = rawin.split("\n")
i = 0
lastHighest = 0
elfCalCount = 0
elfnumber = 1
highs = []
while i < len(elves):
    if elves[i] == "":
        elfnumber += 1
        if elfCalCount > lastHighest:
            lastHighest = elfCalCount
            highs.append(lastHighest)
        elfCalCount = 0
    else:
        elfCalCount += int(elves[i])

    i += 1
highs.sort(reverse=True)
print(len(elves), " lines of info")
print(sum(highs[:3]))
print("highest value is:", lastHighest)
