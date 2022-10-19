n = int(input())
s = 0
i = 0
while i<n:
    a = int(input())
    if a%2 == 0:
        s = s+a/2
    else:
        s = s+a
    i += 1

print(s)

