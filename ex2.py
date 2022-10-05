#Ask the user for a number.
#Depending on whether the number is even or odd, print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when divided by 2?

print("Hello there, We will find whether your number is even or odd")
# Ask User for a number
num = int(input('Number in question: '))
num_eo = num/2
num_d = (num_eo).is_integer()
# use an if statement to determining whether the number sis divisible by 2
print(num_d)

if num%4 == 0:
    print("This is divisible by 4")

    # If is, print even
    #If isnt, print odd