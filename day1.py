calibrationValues = []

while True:
    try:
        allDigits = ""
        line = input()
        for element in line:
            if element.isdigit():
                allDigits += element
        if len(allDigits) == 1: 
            calibrationValues.append((int)(allDigits+allDigits))
        else:
            calibrationValues.append((int)(allDigits[0] + allDigits[-1]))
    except EOFError:
        break

print(sum(calibrationValues))
