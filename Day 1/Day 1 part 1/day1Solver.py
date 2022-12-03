with open(
    "C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 1\\Day 1 part 1\\input.txt"
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
        print(elfCalCount, " Current elf cal count")
        print(elfnumber, "elf done")
        highs.append(elfCalCount)
        elfnumber += 1
        if elfCalCount > lastHighest:
            lastHighest = elfCalCount
        elfCalCount = 0
    else:
        elfCalCount += int(elves[i])

    i += 1

print(len(elves), " lines of info")
print("highest value is:", lastHighest)
