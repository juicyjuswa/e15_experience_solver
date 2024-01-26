def reverse_integer(user_input):
    final_value = ""
    while user_input > 0:
        last_digit = user_input % 10
        final_value += str(last_digit) + " "
        user_input = user_input // 10
    return final_value

user_input = int(input("Input a Number: "))
print(reverse_integer(user_input))