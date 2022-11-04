reizes = int(input())
for m in range(reizes):
    summa = 0
    summa_1 = 0
    izmeri = input()
    burti = len(izmeri)
    for i in range(burti):
        if izmeri[i] == "X":
            summa +=1
        elif izmeri[i] == "S" and summa > 0:
            summa = summa * -1
        elif izmeri[i] == "S":
            summa +=1
        elif izmeri[i] == "M":
            summa +=2
        elif izmeri[i] == "L":
            summa +=3
        elif izmeri[i] == " ":
            summa_1 = summa
            summa = 0
    #print(summa_1 , summa)
    if summa_1 > summa:
        print(">")
    elif summa_1 == summa:
        print("=")
    elif summa_1 < summa:
        print("<")
