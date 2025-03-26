array = list(map(int,input("Enter values: ").split(",")))
max_array = 0
for i in range(len(array)):
    if array[i] > max_array:
        max_array = array[i]
print("Array: ",array)
print("Max:",max_array)
