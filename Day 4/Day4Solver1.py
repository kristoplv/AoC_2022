with open("C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 4\\input4.txt") as f:
    f.seek(0)
    rawin = f.read()
info = rawin.split("\n")
megaList = []
nUltra = []
fin = []
counter = 0
for item in info:
    try:
        megaList.append(item.split(","))
    except TypeError:
        break

for i in range(len(megaList)):
    try:
        nUltra.append(megaList[i][0].split(","))
        nUltra.append(megaList[i][1].split(","))
    except IndexError:
        break

for i in range(len(nUltra)):
    try:
        fin.append(nUltra[i][0].split("-"))
    except TypeError:
        break
for i in range(len(fin) - 1):
    try:
        if i % 2 == 0:
            index = 0
            if int(fin[i][0]) == int(fin[i + 1][0]) and int(fin[i][1]) == int(
                fin[i + 1][1]
            ):
                print("võrdsus kohal ", i / 2, " || ", fin[i], fin[i + 1])
                counter += 1
            else:
                if int(fin[i][0]) <= int(fin[i + 1][0]) and int(fin[i][1]) >= int(
                    fin[i + 1][1]
                ):
                    print(
                        "täidab positsioonil indeksiga ",
                        index,
                        " : ",
                        (i + 1) / 2,
                        "||",
                        fin[i],
                        "   ",
                        fin[i + 1],
                    )
                    counter += 1

        if i % 2 == 1:
            index = 1
            if int(fin[i][0]) == int(fin[i - 1][0]) and int(fin[i][1]) == int(
                fin[i - 1][1]
            ):
                print("võrdsus kohal ", i / 2, " || ", fin[i], fin[i - 1])
            else:
                if int(fin[i][0]) <= int(fin[i - 1][0]) and int(fin[i][1]) >= int(
                    fin[i - 1][1]
                ):
                    print(fin[i][0], "on väiksem/võrdne ", fin[i - 1][0])
                    print(
                        fin[i][1],
                        "on suurem/võrdne ",
                        fin[i - 1][1],
                        fin[i][1] >= fin[i - 1][1],
                    )
                    print(
                        "täidab positsioonil indeksiga ",
                        index,
                        " : ",
                        (i + 1) / 2,
                        "||",
                        fin[i - 1],
                        "   ",
                        fin[i],
                    )
                    counter += 1

    except IndexError:
        break
print(counter)
