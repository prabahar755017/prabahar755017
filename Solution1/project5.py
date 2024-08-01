m1 = int(input("enter the mark1:"))
m2 = int(input("enter the mark2:"))
m3 = int(input("enter the mark3:"))
m4 = int(input("enter the mark4:"))
m5 = int(input("enter the mark5:"))
avg = float(m1+m2+m3+m4+m5)/5
if avg >= 90:
    print("the student grade A")
elif 80 >= avg < 89:
    print("the grade is B")
elif 70 >= avg < 79:
    print("the student grade C")
elif 60 >= avg < 69:
    print("the student grade D")
elif 50 >= avg < 59:
    print("the student grade E")
else:
    print("failed")