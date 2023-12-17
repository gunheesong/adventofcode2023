f = open("day2.txt", "r")
word_to_digit = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10
    }

final = 0

for i in f:
    start = len(i)
    end = -1
    firstnum = 5
    lastnum = 5
    
    for k, v in word_to_digit.items():
        idx = i.find(k)
        
        if idx != -1 and idx < start:
            start = idx
            firstnum = v
        idx = i.rfind(k)
        if idx != -1 and idx > end:
            end = idx
            lastnum = v
    #if firstnum in word_to_digit:
    #    i = i.replace(firstnum, str(word_to_digit[firstnum]))
    #if lastnum in word_to_digit:
    #    i = i.replace(lastnum, str(word_to_digit[lastnum]))
    num1 = 0
    num2 = 0
    
    for letter in i:
        if letter.isdigit():
            num1 = letter
            break
    for j in i[::-1]:
        if j.isdigit():
            num2 = j
            break
        
    first_digit = 0
    last_digit = 0 
    if start > i.find(num1):
        first_digit = num1
    else:
        first_digit = firstnum
    if i.rfind(num2) > end:
        last_digit = num2
    else:
        last_digit = lastnum

    final += int(str(first_digit) + str(last_digit))
print(final)