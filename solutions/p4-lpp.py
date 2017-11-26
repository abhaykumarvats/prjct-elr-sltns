#==============================================================================
# Problem 4: Largest palindrome product
#==============================================================================

def isPalindrome(number):
    """
    number: an integer
    returns: True if number is palindrome, False otherwise
    """
    
    # helper variables
    temp = number
    reverse = 0
    
    # start reversing the number
    while temp:
        reverse = (reverse * 10) + (temp % 10)
        temp //= 10
    
    #  if the number is palindrome, return True
    if reverse == number:
        return True
    
    # return False
    return False

# helper variable
largestProduct = 0

for firstNumber in range(100, 1000):
    for secondNumber in range(firstNumber + 1, 1000):
        product = firstNumber * secondNumber
        if product > largestProduct and isPalindrome(product):
            largestProduct = product
            # for future use
            first = firstNumber
            second = secondNumber

print(first, "*", second, "=", largestProduct)