"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))  
    
def game_duration(p, q, k, t, W):
    """
    Return the expected number of rounds the gambler will play before quitting.

    Parameters:
    p : float
        Probability of winning a round (0 < p < 1).
    q : float
        Probability of losing a round (q = 1 - p).
    k : int
        Starting wealth of the gambler.
    t : int
        Minimum wealth level; the gambler will quit if they reach t.
    W : int
        Maximum wealth threshold; the gambler quits if their wealth reaches k + W.

    Returns:
    float
        Expected number of rounds the gambler will play before reaching t or k + W.
    """    
    # Helper function to calculate expected rounds recursively, given current wealth `x`.
    def helper(x):
        # Initialize the result variable to store intermediate results
        result = None
        
        # Base case: if wealth reaches the maximum threshold (k + W), stop the game
        if x == k + W:
            return 1  # Only 1 round left since the gambler quits upon reaching the threshold

        # Recursive case: calculate the expected rounds by considering the probability of winning
        # and advancing to the next round
        else:
            result = (p * helper(x + 1) + 1) / q

        # Return the expected rounds for the current state
        return result

    # Call the helper function starting from initial wealth `k`
    expected_rounds = helper(k)
    
    # Scale the expected rounds by the difference between initial wealth and quit threshold
    return expected_rounds * (k - t)