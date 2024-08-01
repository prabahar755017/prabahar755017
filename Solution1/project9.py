lis = []
lis2 = []
a = int(input("entre the size of array"))
for i in range(a):
    b = int(input("enter the array1"))
    lis.append(b)
    print(lis)
for j in range(a):
    c = int(input("enter the array2"))
    lis2.append(c)
    print(lis2)

lis[b], lis2[c] = lis2[c], lis[b]
print(lis, lis2)