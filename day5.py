import string


file = open('day5Files\input.txt', 'r')
content = file.read()
codeList = content.split()

seatID = []


def determinate_half(minNumber, maxNumber, letter):
    if letter in ["B", "R"]:
        return int(maxNumber-(maxNumber-minNumber)/2), int(maxNumber)
    if letter in ["F", "L"]:
        return int(minNumber), int(minNumber+(maxNumber-minNumber)/2)


for code in codeList:
    maxRow = 127
    minRow = 0
    minColumn = 0
    maxColumn = 7
    for letter in code[:7]:
        minRow, maxRow = determinate_half(minRow, maxRow, letter)
    for letter in code[7:]:
        minColumn, maxColumn = determinate_half(minColumn, maxColumn, letter)
    seatID.append(int(maxRow) * 8 + int(maxColumn))

print(max(seatID))
mySeat = [seat for seat in range(max(seatID)+1) if seat not in seatID]
print(mySeat)
