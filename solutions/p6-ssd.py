#==============================================================================
# Problem 6: Sum square difference
#==============================================================================

def sumOfSquares(number):
    """
    number: number upto which sum of squares is required
    returns: sum of squares of all the natural numbers upto number
    """
    
    return (number * (number + 1) * (2 * number + 1)) / 6


def squareOfSum(number):
    """
    number: number upto which square of the sum is required
    returns: square of the sum of all the natural numbers upto number
    """
    
    return ((number * (number + 1)) / 2)**2


print("Answer:", squareOfSum(100) - sumOfSquares(100))