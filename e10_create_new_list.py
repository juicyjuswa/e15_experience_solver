

first_list = [10, 20, 25, 30, 35]
second_list = [40, 45, 60, 75, 90]


new_list = []
for loop in first_list:
    if loop % 2 == 1:
        new_list.append(loop)

for loop in second_list:
    if loop % 2 == 0:
        new_list.append(loop)

print("GIVEN")
print("first_list = [10, 20, 25, 30, 35]\nsecond_list = [40, 45, 60, 75, 90]\n")
print("result list: ", new_list)







#result list shoul be = [25, 35, 40, 60, 90]: