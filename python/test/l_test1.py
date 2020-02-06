#!/usr/local/bin/python3

#!/usr/local/bin/python3

# Write a program which prints out all numbers between 1 and 100. When the program would print out a number exactly divisible by 4, 
# print "Linked" instead. When it would print out a number exactly divisible by 6, print "In" instead. 
# When it would print out a number exactly divisible by both 4 and 6, print "LinkedIn" instead.

# NOTE: my original solution used range(100) which starts at zero
# which isn't really what the question asked.
# The other thing to clarify is whether "between" is inclusive or not
# I assumed it was inclusive and let the interviewer know that

def return_numbers(num):
    if (num % 4 == 0) and (num % 6 == 0):
        return ("LinkedIn")
    elif (num % 4 == 0):
        return ("Linked")
    elif (num % 6 == 0):
        return ("In")
    else:
        return

if __name__ == "__main__":
    for i in range(1,101):
        result = return_numbers(i)
        if result:
            print(result)
