def friend_second_besties(individual, bestie_dict):
    """generate the set of (strictly) second-order friends for 
    `individual`, based on the contents of `bestie_dict`"""

    # extract out friends of friends for each individual in
    # `individual_list`, by finding friends of each individual,
    # and friends of those friends, making sure that
    # degree of separation is strictly 2
    second_besties = set()
    if individual in bestie_dict:
        for bestie in bestie_dict[individual]:
            if bestie in bestie_dict:
                second_besties = second_besties.union(bestie_dict[bestie])

        # remove anyone who is a direct friend or the individual themself
        second_besties = second_besties.difference(
                            bestie_dict[individual].union(set([individual])))
    return sorted(second_besties)
    
