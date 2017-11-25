#==============================================================================
# Problem 2: Even Fibonacci numbers
#==============================================================================

firstNum = 0
secondNum = 1
currentNum = 0
sumEvenFib = 0

# while current number is less than or equal to 4 million
while currentNum <= 4000000:
    # current number is sum of previous two numbers
    currentNum = firstNum + secondNum
    # if current number is even
    if currentNum % 2 == 0:
        # add it to the sum
        sumEvenFib += currentNum
    
    # update first and second numbers for next iteration
    firstNum = secondNum
    secondNum = currentNum

# print final result
print("Answer:", sumEvenFib)