#original number 121
#Yes. given number is palindrome number

#original number 125
#No. given number is not palindrome number
def check_palindrome(reverse):
    num_1 = str(reverse)
    reverse_number = num_1[::-1]
    print("\nOriginal Number is ", num_1)

    if num_1 == reverse_number:
        print("Yes. Given number is palindrome number\n")
    else:
        print("No. Given number is not palindrome number\n")



check_palindrome(7888) #no
check_palindrome(7887) #yes
check_palindrome(7888) #no
check_palindrome(123) #no
check_palindrome(43234) #yes