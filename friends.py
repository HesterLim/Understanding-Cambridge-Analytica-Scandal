def get_friendly_dict(friend_list):
    """ Accept a list of reciprocal friendship links between individuals and
    return a dictionary of degree-one friends of each individual in a social 
    network. """
    
    # first, we'll get all the individuals name using union set and put it into
    # unique_name list
    unique_name_list = set()
    for friend in range(1, len(friend_list)):
        unique_name = set(friend_list[friend - 1]) | set(friend_list[friend])
        if unique_name not in unique_name_list:
            unique_name_list.update(unique_name)

    # second, we'll get the 1st degree friend by iterating in the tuple of a 
    # list and then add them into a set (new_friend_set) if it is not the given 
    # individual before adding into a dicitionary.
    new_bestie_friend_dict = {}
    for name in unique_name_list:
        new_friend_set = set()
        for name_friend_list in range(len(friend_list)):
            if name in friend_list[name_friend_list]:
                for inside_friend in friend_list[name_friend_list]:
                    if inside_friend != name:
                        new_friend_set.add(inside_friend)
        new_bestie_friend_dict[name] = new_friend_set
        
    return new_bestie_friend_dict

