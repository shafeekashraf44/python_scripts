list_1 =[1,2,3,4,5]
list_2 =[5,6,7,8,9,10]
merged=[]
rm_duplicates=[]
merged = list_1+list_2
print(merged)
for num in merged:
    if num not in rm_duplicates:
        rm_duplicates.append(num)
print(rm_duplicates)