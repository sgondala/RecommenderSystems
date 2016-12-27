# -*- coding: utf-8 -*-

import numpy as np
import heapq
import math
import myPrint

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
    
def allSimilarity(ratings, distanceMetric, similarityListLength, iMax):
    """
    For each item in ratings, get most nearest items list of length similarityListLength
    """    
    itemList = ratings.keys()
    itemSimilarityDict = {}
    i = 0    
    for item1 in itemList:
        itemSimilarityList = []
        for item2 in itemList:
            if(item1 == item2):
                continue
            similarity = distanceMetric(ratings, item1, item2)
            if(len(itemSimilarityList) < similarityListLength):
                heapq.heappush(itemSimilarityList, (similarity, item2))
            elif(itemSimilarityList[0][0] < similarity):
                heapq.heappop(itemSimilarityList)
                heapq.heappush(itemSimilarityList, (similarity, item2))
        i += 1
        itemSimilarityList.sort(reverse=True)
        itemSimilarityDict[item1] = itemSimilarityList        
        if i%100 == 0:
            myPrint.myPrint("progress",str(i) + " of " + str(len(ratings)))
    return itemSimilarityDict