#==============================================================================
# Problem 12: Highly divisible triangular number
#==============================================================================

# helper variables
divisors = 0
naturalNumber = 0
triangleNumber = 0

# loop until desired triangle number is found
while divisors < 501:
    # current natural number
    naturalNumber += 1
    # current triangle number
    triangleNumber += naturalNumber
    # reset divisors to zero
    divisors = 0
    
    # for each number from 1 to square root of triangle number
    for number in range(1, int(triangleNumber**0.5) + 1):
        # if the number is a factor
        if not (triangleNumber % number):
            # increment divisors by two,
            # because "triangleNumber / number" is also a factor
            divisors += 2
    
    # if current triangle number is a perfect square,
    # decrement divisors by one, square root got added two times
    if int(triangleNumber**0.5) == triangleNumber**0.5:
        divisors -= 1

# print final result
print("Answer:", triangleNumber)