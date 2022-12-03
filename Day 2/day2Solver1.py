with open("C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 2\\input2.txt") as f:
    f.seek(0)
    rawin = f.read()

x_val = 1
y_val = 2
z_val = 3

win_val = 6
tie_val = 3
bigArr = []
valueArr = []

sumValue = 0

# X - rock; Y - paper; Z - scissors // A - rock; B - paper; C - scissors

scores = rawin.split("\n")
for i in range(len(scores)):
    bigArr.append(scores[i].replace(" ", ""))
    try:
        if bigArr[i][0] == "A":
            valueArr.append(bigArr[i].replace("A", "X"))
        elif bigArr[i][0] == "B":
            valueArr.append(bigArr[i].replace("B", "Y"))
        elif bigArr[i][0] == "C":
            valueArr.append(bigArr[i].replace("C", "Z"))
    except IndexError:
        break
for i in range(len(valueArr)):
    # X values
    if valueArr[i][0] == valueArr[i][1] and valueArr[i][0] == "X":
        sumValue += x_val + tie_val
    elif valueArr[i][0] == "X" and valueArr[i][1] == "Y":
        sumValue += y_val + win_val
    elif valueArr[i][0] == "X" and valueArr[i][1] == "Z":
        sumValue += z_val

    # Y values
    elif valueArr[i][0] == valueArr[i][1] and valueArr[i][0] == "Y":
        sumValue += y_val + tie_val
    elif valueArr[i][0] == "Y" and valueArr[i][1] == "X":
        sumValue += x_val
    elif valueArr[i][0] == "Y" and valueArr[i][1] == "Z":
        sumValue += z_val + win_val

    # Z values
    elif valueArr[i][0] == valueArr[i][1] and valueArr[i][0] == "Z":
        sumValue += z_val + tie_val
    elif valueArr[i][0] == "Z" and valueArr[i][1] == "X":
        sumValue += x_val + win_val
    elif valueArr[i][0] == "Z" and valueArr[i][1] == "Y":
        sumValue += y_val
print(sumValue)
