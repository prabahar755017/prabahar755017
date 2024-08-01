lis = []
num = int(input("enter the array size"))
for i in range(num):
    a = int(input())
    lis.append(a)
    print(lis)
b=[]
for n in lis:
    if n % 2 == 0:
        print("the even number in given lis in", n)
        b.append(n)
print(len(b))
