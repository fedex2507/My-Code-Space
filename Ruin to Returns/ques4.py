def stationary_distribution(p, q, r, N):
    """
    Calculate the stationary distribution of the Markov chain.

    Parameters:
    p : list of size N+1, where 0 < p[i] < 1, probability of price increase
    q : list of size N+1, where 0 < q[i] < 1, probability of price decrease
    r : list of size N+1, where r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock

    Returns:
    list : A list of size N+1 containing the stationary distribution
    """
    stationary_list = [1] * (N + 1)  # Initialize the stationary distribution list with all ones
    total = 1  # Initialize the total to 1 for normalization

    # Calculate the stationary distribution using recursive formula
    for i in range(1, N + 1):
        stationary_list[i] = p[i - 1] * stationary_list[i - 1] / q[i]  # Compute the next element
        total += stationary_list[i]  # Update the total sum

    k = 1 / total  # Calculate the normalization constant

    # Normalize the stationary distribution
    for i in range(N + 1):
        stationary_list[i] = k * stationary_list[i]  # Multiply each element by k to normalize

    return stationary_list  # Return the normalized stationary distribution

def expected_wealth(p, q, r, N):
    """
    Calculate the expected wealth of the gambler in the long run.

    Parameters:
    p : list of size N+1, where 0 < p[i] < 1, probability of price increase
    q : list of size N+1, where 0 < q[i] < 1, probability of price decrease
    r : list of size N+1, where r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock

    Returns:
    float : The expected wealth of the gambler in the long run
    """
    stationary = stationary_distribution(p, q, r, N)  # Get the stationary distribution
    expected_wealth = 0  # Initialize the expected wealth

    # Calculate the expected wealth using the stationary distribution
    for i in range(N + 1):
        expected_wealth += i * stationary[i]  # Add the contribution from each state

    return expected_wealth  # Return the expected wealth

def expected_time(p, q, r, N, a, b):
    """
    Calculate the expected time required for the price to reach b, starting from a.

    p : List of length N+1, where 0 < p[i] < 1, representing the probability of a price increase
    q : List of length N+1, where 0 < q[i] < 1, representing the probability of a price decrease
    r : List of length N+1, defined as r[i] = 1 - p[i] - q[i], representing the probability that the price stays the same
    N : Integer, maximum price level
    a : Integer, initial price level
    b : Integer, target price level
    """
    # If starting price is already the target, return 0 immediately
    if a == b:
        return 0
    
    # Initialize array to store expected times for each price level
    h = [0] * (N + 1)
    
    # Use previous values to check for convergence during iteration
    prev_h = [float('inf')] * (N + 1)
    h[b] = 0  # No steps needed if already at target price

    # Iteratively calculate expected times until they converge
    while True:
        prev_h = h.copy()
        
        # Compute expected time at each price level except the target
        for i in range(N + 1):
            if i == b:
                continue

            # Calculate expected time to reach target from the current level
            step_count = 1.0  # Always takes at least one step
            if i < N:
                step_count += p[i] * prev_h[i + 1]
            if i > 0:
                step_count += q[i] * prev_h[i - 1]
            
            h[i] = step_count / (1.0 - r[i])  # Update h[i] based on probabilities
        
        # Check for convergence across all levels
        if all(abs(h[i] - prev_h[i]) < 1e-10 for i in range(N + 1)):
            break

    # Round up the result at start price to get an integer answer
    ans = h[a]
    # rounded_ans = int(ans) if ans == int(ans) else int(ans) + 1
    # return rounded_ans
    return ans