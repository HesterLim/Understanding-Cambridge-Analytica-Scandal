# DO NOT DELETE/EDIT THIS LINE OF CODE, AS IT IS USED TO PROVIDE ACCESS TO
# THE FUNCTIONS FROM Q2 AND Q3
from hidden import friend_besties, friend_second_besties

def besties_coverage(individuals, bestie_dict, relationship_list):
    
    """ Accepts variables as below as input:-
    1. individuals which is a list of individuals, each in the form of string 
    ID
    2. bestie_dict which is a dictionary of sets of friends of each individual 
    in 
    the social network
    3. relationship_list which is a list of functions defining relationships in 
    the 
    social network, selected from friends_besties and friend_second_besties.
    
    Return the proportion of total connected nodes over total network size 
    within 
    the social network."""
    
    # first, we'll take a person name in individuals, 
    # we'll initialise connect_individual as 1 since that person by 
    # himself is already 1 connection. we'll also set the network size 
    # as the total individuals in the social network.
    for individual in individuals:
        connect_individuals = 1
        network_size = len(bestie_dict.keys())
        
        # second, we'll check if that person exist in the social network.
        # Then, add up all the connected individuals to that person to count 
        # the proportion of network coverage
        if individual in bestie_dict.keys():
            if relationship_list == []:
                proportion_network = connect_individuals / network_size
                return proportion_network
            else:
                for besties in relationship_list:
                    connect_individuals += len(besties(individual, 
                                                             bestie_dict)) 
                    
                    proportion_network = connect_individuals / network_size
                return proportion_network
        else:
            return []
        
    
        
    
