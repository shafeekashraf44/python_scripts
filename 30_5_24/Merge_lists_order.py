list_1 = [1,2,7,4,5]
list_2 = [6,7,1,3,9]
order = []
final_list = list_1 + list_2
smallest = min(final_list)
order.append(smallest)
for num in final_list:
    if (smallest < num):
        smallest = num
        order.append(smallest)
print(order)
