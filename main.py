# -*- coding: utf-8 -*-
from __future__ import print_function

import populateDict
import helperFunctions
import cPickle as pickle
import myPrint

myPrint.myPrint("progress","Starting")
bookRatings = populateDict.getBookRatingsDict('select * from "Ratings" where "ISBN" in (select "ISBN" from "Ratings" group by "ISBN" having count(*) >= 5) and "User-ID" in (select "User-ID" from "Ratings" group by "User-ID" having count(*) >= 5);')
myPrint.myPrint("progress","bookRatings Done")
bookSimilarityDict = helperFunctions.allSimilarity(bookRatings, helperFunctions.eucledianDistanceMetric, 10, 100)
myPrint.myPrint("progress","Calculations done, To start pickling")
pickle.dump(bookSimilarityDict,open("model.p","wb"),protocol = -1)
myPrint.myPrint("progress","Dumped")
