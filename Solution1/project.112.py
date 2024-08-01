lis = []
num = int(input("enter the array size"))
for i in range(num):
    a = int(input())
    lis.append(a)
    print(lis)
lis.sort(reverse=True)
print(lis)
