a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a>b and a>c:
    print("{} is greater.".format(a))
elif b>a and b>c:
    print("{} is greater.".format(b))
else:
     print("{} is greater.".format(c))
