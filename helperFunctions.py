# -*- coding: utf-8 -*-

import numpy as np
import math

def eucledianDistanceMetric(ratings, user1, user2):
    """
    Similarity of 2 users based on their taste
    """
    booksList = np.union1d(np.array(ratings[user1].keys()),np.array(ratings[user2].keys()))
    totalSum = 0.0    
    for book in booksList:
        user1Rating = ratings[user1].get(book,0)
        user2Rating = ratings[user2].get(book,0)
        totalSum += (user1Rating - user2Rating)**2
    return 1/(1+math.sqrt(totalSum))
    
def allSimilarity(ratings, distanceMetric):
    itemList = ratings.keys()
    itemSimilarityDict = {}
    i = 0    
    for item1 in itemList:
        itemSimilarityDict[item1] = {}
        for item2 in itemList:
            if(item1 == item2):
                continue
            itemSimilarityDict[item1][item2] = distanceMetric(ratings, item1, item2)
        i += 1
        #print i
        if i == 10:
            return
    return itemSimilarityDict