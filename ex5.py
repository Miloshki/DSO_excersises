#Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)
string = input('Input a string: ')
string_s = string[slice(None, None, -1)]
print("Forwards: " + string + ", Backwards: " + string_s)
if string_s == string:
    print('YES! This is a Palindrome')
elif string_s != string:
    print('No, This is not a Palindrome')
