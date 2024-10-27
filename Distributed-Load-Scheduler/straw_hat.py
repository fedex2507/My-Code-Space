'''
    This file contains the class definition for the StrawHat class.
'''
import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Initializes the StrawHat treasury with m crewmates.
        '''
        self.crewmates = heap.Heap(lambda x, y: x.size < y.size, [crewmate.CrewMate() for _ in range(m)])
        self.treasures = []
    
    def add_treasure(self, treasure):
        '''
        Adds a treasure to the crewmate with the least current load.
        '''
        # Write your code here
        # Find the crewmate with the least load
        self.treasures.append(treasure)
        min_load_crewmate = self.crewmates.extract()
        #Add the treasure to the crewmate's heap
        min_load_crewmate.add_treasure(treasure)
        # Reinsert the updated crewmate back into the crewmate heap
        self.crewmates.insert(min_load_crewmate)
        pass
    
    def get_completion_time(self):
        '''
        Processes all the treasures and returns the list of treasures in the order of their completion.
        '''
        completion_list = []
        if len(self.treasures) < len(self.crewmates.heap):
            for i in range (len(self.treasures)):
                self.treasures[i].completion_time = self.treasures[i].arrival_time + self.treasures[i].size
                completion_list.append(self.treasures[i])
            completion_list.sort(key=lambda t: t.id)
            return completion_list

        for crewmate in self.crewmates.heap:
            crewmate.process_treasure(completion_list)

        # Sort the completion list based on treasure ID for final output
        completion_list.sort(key=lambda t: t.id)
        return completion_list
        pass

    # You can add more methods if required


