# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 23:18:55 2016

@author: sashank
"""

import psycopg2

def getUserRatingsDict():
    """
    Takes the Ratings DB and converts it into dict for easy analysis
    """
    userRatings = {}
    conn = psycopg2.connect(database='sashank',user='sashank',password='x',host='localhost')
    cur = conn.cursor()
    cur.execute('SELECT * from "Ratings";')
    for row in cur:
        user = row[0]
        bookId = row[1]
        ratingGiven = row[2]
        if user not in userRatings:
            userRatings[user] = {}
        userRatings[user][bookId] = ratingGiven
    conn.close()
    return userRatings
    
#userRatings = getUserRatingsDict()
#a = 10