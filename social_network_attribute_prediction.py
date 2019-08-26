from hidden import friend_besties, friend_second_besties
from collections import defaultdict


def predict_attribute(friends, feat_dict, feature):
    """predict the value of `feature` from the set `friends` based on the
    attributes in `feat_dict`"""

    # accumulator for attribute freqs
    val_count = defaultdict(int)

    # for each friend, add vote for relevant attribute if they have it
    for friend in friends:
        if friend in feat_dict and feature in feat_dict[friend]:
            val_count[feat_dict[friend][feature]] += 1

    # find the attributes with the highest frequency and return as
    # sorted list, assuming at least one attribute prediction made
    if val_count:
        max_count = 0
        for attribute, count in val_count.items():
            if count > max_count:
                att_list = [attribute]
                max_count = count
            elif count == max_count:
                att_list.append(attribute)
        return sorted(att_list)

    # if no users with relevant attribute, no prediction to be made
    else:
        return []
        
def friendly_prediction(unknown_user, features, bestie_dict, feat_dict):
    """predict the attributes of `unknown_user` for each feature in `features`,
    based on the social network in `bestie_dict` and user attribute data in
    `feat_dict`, and return the predictions in the form of a dictionary 
    of lists"""
    
    # dictionary of predictions for each feature
    predictions = {}

    # predict attribute for each feature based on besties, and failing that,
    # second besties
    for feature in features:
        besties_predict = predict_attribute(friend_besties(unknown_user,
                                            bestie_dict), feat_dict, feature)
        if besties_predict:
            predictions[feature] = besties_predict
        else:
            second_besties_predict = predict_attribute(friend_second_besties(
                unknown_user, bestie_dict), feat_dict, feature)
            predictions[feature] = second_besties_predict

    return predictions
    
        
    
