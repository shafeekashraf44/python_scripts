input_string =[1,2,3,4,5]
target = int(input("Enter the target:"))
length = int(len(input_string))

for i in input_string:
    compare = (target - i)
    if all(variable in input_string for variable in [i, compare]):
         print(i,compare)
      
