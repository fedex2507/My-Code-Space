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

# Problem 1a
dp = [[-1 for _ in range(101)] for _ in range(101)]
dp[1][1]=1   

def calc_prob(alice_wins, bob_wins):
    a = alice_wins
    b = bob_wins

    if dp[a][b] != -1:
        return dp[a][b]

    if a==0 or b==0:
        return 0 

    dp[a][b] = mod_add(mod_multiply(mod_divide(b,mod_add(a, b-1)), calc_prob(a - 1, b)) , 
                mod_multiply(mod_divide(a,mod_add(a-1, b)), calc_prob(a, b - 1)))

    return dp[a][b]
    """
    Returns:
        The probability of Alice winning alice_wins times and Bob winning bob_wins times will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.
    """
    
# Problem 1b (Expectation)      
def calc_expectation(t):
    exp=0
    for i in range(1,t+1):
        exp=mod_add(exp,mod_multiply((2*i-t),calc_prob(i,t-i)))
    return exp
    """
    Returns:
        The expected value of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """

# Problem 1b (Variance)
def calc_variance(t):
    var=0
    exp=0
    for i in range(1,t+1):
        exp=mod_add(exp,mod_multiply(mod_multiply(2*i-t,2*i-t),calc_prob(i,t-i)))
    var=(exp-calc_expectation(t))%M
    return var
    """
    Returns:
        The variance of \sum_{i=1}^{t} Xi will be of the form p/q,
        where p and q are positive integers,
        return p.q^(-1) mod 1000000007.

    """
    

