a = int(input("Enter a number: "))
fact = 1
if a<0:
    print("It's a negative number")
    break
elif a==0:
    print("Factorial of 0 is: 1")
else:
    for i in range(1,a+1):
        fact *= i
print("Factorial:",fact)
