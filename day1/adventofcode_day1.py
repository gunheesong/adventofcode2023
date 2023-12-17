f = open("day1_ex.txt", "r")
final = 0
for x in f:
    num1 = 0
    num2 = 0
    for i in x:
        if i.isdigit():
            num1 = i
            break
    for j in x[::-1]:
        if j.isdigit():
            num2 = j
            break
    result = int(num1 + num2)
    #print(type(result))
    final+= result
    

print(final) 
