import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = [1,1] 
        self.results = [1,0]           
        self.opp_play_styles = [1,1]  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 2a here.
         
        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        """ 
        if self.results[-1]==0:
            return 1
        elif self.results[-1]==0.5:
            return 0
        elif self.results[-1]==1:
            if (len(self.results)-self.points)*11>6*len(self.results):
                return 0
            else:
                return 2
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
        pass

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = [1,1]
        self.results = [0,1]          
        self.opp_play_styles = [1,1]
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """ 
        self.past_play_styles.append(own_style)
        self.results.append(result)
        self.opp_play_styles.append(opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    
    #Moves
    Bob_move = bob.play_move()
    Alice_move = alice.play_move()
    #Probability of moves
    prob=payoff_matrix[Alice_move][Bob_move]
    #Result for Bob
    result=np.random.choice([0,0.5,1], p=prob)
    bob.observe_result(Bob_move,Alice_move,result)
    alice.observe_result(Alice_move,Bob_move,1-result)
    payoff_matrix[0][0] = [(bob.points)/(bob.points+alice.points),0,(alice.points)/(bob.points+alice.points)]
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """ 
    


def monte_carlo(num_rounds):
    payoff_matrix=[ [(0.5, 0, 0.5), ( 7/10 , 0, 3/10 ), ( 5/11 , 0, 6/11 )],
                  [( 3/10 , 0, 7/10 ), ( 1/3 , 1/3 , 1/3 ) ,( 3/10 , 1/2 , 1/5 )],
                  [( 6/11 , 0, 5/11 ), ( 1/5 , 1/2 , 3/10 ), ( 1/10 , 4/5 , 1/10 )]]
    alice = Alice()
    bob = Bob()
    for i in range (num_rounds) :
        simulate_round(alice,bob,payoff_matrix)
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    pass
    

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=pow(10,5))
