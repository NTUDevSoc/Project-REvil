import fileinput

def intToDate(num):
    dates = {
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun"
    }
    return dates[num]

def main():
    # Use in conjunction with https://onlineasciitools.com/convert-ascii-to-arbitrary-base
    # Because I'm too lazy to write one myself lmao

    lines = [line.rstrip('\n') for line in fileinput.input("numInput.txt")]

    for num in lines:
        dateStr = ""
        for charNumber in num:
            number = int(charNumber)
            dateStr += intToDate(number)
        print(dateStr)

main()