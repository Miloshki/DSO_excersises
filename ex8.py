#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#Take this opportunity to think about how you can use functions.
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

#Ask how many fib numbers

def fibo(n):
    #print(f"Fibo of {n}")
    if n in [0, 1]:
        #print(f"Adding {n}")
        return n
    return fibo(n-1) + fibo(n-2)

numbers = int(input('how many fibonnaci numbers do you wish to generate: '))



f = [fibo(n) for n in range(numbers)]

print(f)




