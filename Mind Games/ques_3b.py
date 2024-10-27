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

# Problem 3b
dp = [[[-1 for _ in range(101)] for _ in range(202)] for _ in range(202)]
exp = [[[-1 for _ in range(101)] for _ in range(202)] for _ in range(202)]

def expected_points(tot_rounds,na=1,nb=1):
    """
    Calculate the expected points that Alice can score after the total rounds,
    assuming she plays optimally.
    """
    if tot_rounds == 0:
        return 0
    if exp[int(2 * na)][int(2 * nb)][tot_rounds] != -1:
        return exp[int(2 * na)][int(2 * nb)][tot_rounds]

    payoff_matrix = [
        [[nb / (na + nb), 0, na / (na + nb)], [0.7, 0, 0.3], [5 / 11, 0, 6 / 11]],
        [[0.3, 0, 0.7], [1 / 3, 1 / 3, 1 / 3], [0.3, 0.5, 0.2]],
        [[6 / 11, 0, 5 / 11], [0.2, 0.5, 0.3], [0.1, 0.8, 0.1]]
    ]

    best_expected_points = float('-inf')  # Start with the lowest possible value
    best_strategies = [0, 0, 0]

    for strategy in range(3):
        current_expected_points = 0
        for i in range(3):
            current_expected_points += (payoff_matrix[strategy][i][0] * (1 + expected_points(tot_rounds - 1,na + 1, nb))) / 3
            current_expected_points += (payoff_matrix[strategy][i][1] * (0.5 + expected_points(tot_rounds - 1,na + 0.5, nb + 0.5))) / 3
            current_expected_points += (payoff_matrix[strategy][i][2] * (expected_points(tot_rounds - 1,na, nb + 1))) / 3
        
        if current_expected_points == best_expected_points:
            best_strategies[strategy] += 1 / 3
        elif current_expected_points > best_expected_points:
            best_expected_points = current_expected_points
            best_strategies = [0, 0, 0]
            best_strategies[strategy] = 1

    dp[int(2 * na)][int(2 * nb)][tot_rounds] = best_strategies
    exp[int(2 * na)][int(2 * nb)][tot_rounds] = best_expected_points
    return best_expected_points

def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice to maximize her points in future rounds
    given the current score of Alice (na), Bob (nb), and the total number of rounds (tot_rounds).
    
    Return a list [p1, p2, p3] representing probabilities for strategies.
    """
    if dp[int(2 * na)][int(2 * nb)][tot_rounds] != -1:
        return dp[int(2 * na)][int(2 * nb)][tot_rounds]
    
    expected_points(tot_rounds,na, nb)
    return dp[int(2 * na)][int(2 * nb)][tot_rounds]






