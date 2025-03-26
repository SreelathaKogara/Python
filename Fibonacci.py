a = int(input("Enter a number: "))
sum = 0
n1 = 0
n2 = 1
for i in range(a+1):
    print(n1)
    sum = n1+n2
    n1 = n2
    n2 = sum
