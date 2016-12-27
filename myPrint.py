# -*- coding: utf-8 -*-

def myPrint(fileName, string):
    """
    Prints in a file, as soon as the function is called
    """
    f = open(fileName, "a")
    print >> f, string
    f.close()