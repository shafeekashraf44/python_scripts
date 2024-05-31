n = int(input("Enter the limit:"))
fibonacci =[0,1]
while (len(fibonacci) < n):
    next_number = fibonacci[-2]+fibonacci[-1]
    print(next_number)
    fibonacci.append(next_number)
print(fibonacci)