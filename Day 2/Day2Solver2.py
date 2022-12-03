with open("C:\\Users\\KristoMarleen\\Documents\\AoC_2022\\Day 2\\input2.txt") as f:
    f.seek(0)
    rawin = f.read()

a_val = 1
b_val = 2
c_val = 3

win_val = 6
tie_val = 3
bigArr = []
valueArr = []
holderList = []

sumValue = 0

# X - lose; Y - tie; Z - win // A - rock; B - paper; C - scissors

scores = rawin.split("\n")
for i in range(len(scores) - 1):
    bigArr.append(scores[i].replace(" ", ""))
    if bigArr[i][0] == "A" and bigArr[i][1] == "X":
        sumValue += c_val
    if bigArr[i][0] == "A" and bigArr[i][1] == "Y":
        sumValue += a_val + tie_val
    if bigArr[i][0] == "A" and bigArr[i][1] == "Z":
        sumValue += b_val + win_val

    if bigArr[i][0] == "B" and bigArr[i][1] == "X":
        sumValue += a_val
    if bigArr[i][0] == "B" and bigArr[i][1] == "Y":
        sumValue += b_val + tie_val
    if bigArr[i][0] == "B" and bigArr[i][1] == "Z":
        sumValue += c_val + win_val

    if bigArr[i][0] == "C" and bigArr[i][1] == "X":
        sumValue += b_val
    if bigArr[i][0] == "C" and bigArr[i][1] == "Y":
        sumValue += c_val + tie_val
    if bigArr[i][0] == "C" and bigArr[i][1] == "Z":
        sumValue += a_val + win_val

print(sumValue)
