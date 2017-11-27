#==============================================================================
# Problem 5: Smallest multiple
#==============================================================================

def isSmallestMultiple(multiple):
    """
    multiple: an integer
    returns: True if multiple is the smallest multiple evenly divisible by the
    numbers in [1, 20], False otherwise
    """
    
    # if a number is divisible by these numbers,
    # it is divisible by all the numbers in [1, 20]
    numbers = [11, 13, 14, 16, 17, 18, 19, 20]
    
    # for each number in numbers
    for number in numbers:
        # if multiple is not divisible by number
        if multiple % number != 0:
            return False
    
    # number found, return True
    return True


# initial value of smallest multiple is 20 (say)
smallestMultiple = 20

while True:
    # if the number is found, break out of the loop
    if isSmallestMultiple(smallestMultiple):
        break
    
    # if not found, increment smallestMultiple by 20 (for faster execution)
    smallestMultiple += 20

# print final result
print("Answer:", smallestMultiple)