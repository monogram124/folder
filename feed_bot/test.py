def plusOne(dig):
    digS = ""
    new_dig = []
    for num in dig:
        digS += str(num)
    
    digNum = int(digS) + 1

    for num in str(digNum):
        new_dig.append(int(num))
    
    return new_dig

print(plusOne([1, 2, 3, 4]))