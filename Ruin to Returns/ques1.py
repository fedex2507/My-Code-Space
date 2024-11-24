def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if p == 0.5:
        # When probabilities are equal, win probability is proportionate to rounds won
        return k / N
    factor = q / p
    # Formula for win probability when p and q are different
    return (1 - factor ** k) / (1 - factor ** N)

def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if p <= q:
        # If losing probability q is equal to or greater than winning probability p
        return 0
    # Win probability with diminishing returns over large rounds
    return 1 - (q / p) ** k

def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if p == 0.5:
        # Simplified formula for equal win and lose probability
        return k * (N - k)
    factor = q / p
    diff = q - p
    const = (1 - factor ** N)
    numerator = N*(1 - (factor ** k)) + (k * const)
    denominator = diff * const
    # Expected game duration when p and q differ
    return numerator / denominator








