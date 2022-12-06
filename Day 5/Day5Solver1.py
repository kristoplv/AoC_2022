with open("C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 5\\input5.txt") as f:
    f.seek(0)
    rawin = f.read(287).replace("[", ",").replace("]", ",").replace(" ", ",")
    f.seek(325)
    rawtext = (
        f.read()
        .replace("move ", "")
        .replace(" from ", "")
        .replace(" to ", "")
        .split("\n")
    )

mass2 = []
for item in rawtext:
    holder = []
    for i in range(len(item)):
        if len(item) > 3:
            if i < 1:
                holder.append(item[i] + item[i + 1])
            else:
                try:
                    holder.append(item[i + 1])
                except IndexError:
                    continue
        else:
            holder.append(item[i])
    mass2.append(holder)
print(mass2)
mass = []
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
info = rawin.split("\n")
for i in range(len(info)):
    col1.append(info[i][1])
    col2.append(info[i][5])
    col3.append(info[i][9])
    col4.append(info[i][13])
    col5.append(info[i][17])
    col6.append(info[i][21])
    col7.append(info[i][25])
    col8.append(info[i][29])
    col9.append(info[i][33])
col1 = list(filter((",").__ne__, col1))
col2 = list(filter((",").__ne__, col2))
col3 = list(filter((",").__ne__, col3))
col4 = list(filter((",").__ne__, col4))
col5 = list(filter((",").__ne__, col5))
col6 = list(filter((",").__ne__, col6))
col7 = list(filter((",").__ne__, col7))
col8 = list(filter((",").__ne__, col8))
col9 = list(filter((",").__ne__, col9))
mass.append(col1)
mass.append(col2)
mass.append(col3)
mass.append(col4)
mass.append(col5)
mass.append(col6)
mass.append(col7)
mass.append(col8)
mass.append(col9)
print(mass)
for i in range(len(mass2) - 1):
    j = 0
    for x in range(int(mass2[i][0])):
        if i > 490:
            print(i)
            print(mass2[i])
            print(mass[int(mass2[i][1]) - 1], "supplier")
        mass[int(mass2[i][2]) - 1].insert(0, mass[int(mass2[i][1]) - 1][x - j])
        del mass[int(mass2[i][1]) - 1][x - j]
        if i > 490:
            print(mass[int(mass2[i][2]) - 1], " receiver")
        j += 1
    if i == 500:
        for item in mass:
            print(item)
    """print(mass[int(mass2[i][1]) - 1])
    print(mass[int(mass2[i][2]) - 1])"""
for item in mass:
    print(item[0])
