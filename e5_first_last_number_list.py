def first_last_number(lists):
    print("The list are the following ", lists)

    first_number = lists[0]
    last_number = lists[-1]

    if first_number == last_number:
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
print("The result is", first_last_number(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("The result is", first_last_number(numbers_y))