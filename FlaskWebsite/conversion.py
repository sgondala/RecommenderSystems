# -*- coding: utf-8 -*-
import psycopg2

#TODO - Make it prepared statements


def getBookNameFromISBN(isbn):
    """
    Self explanatory
    """
    conn = psycopg2.connect(database='sashank',user='sashank',password='x',host='localhost')
    cur = conn.cursor()
    statement = 'select * from "Books" where "ISBN"=\'' + isbn + '\';'
    cur.execute(statement)
    a = cur.fetchone()
    conn.close()    
    if a == None:
        return "-1"
    else:
        return a[1]
        
def getIsbnFromBookName(bookName):
    """
    Self explanatory
    """
    conn = psycopg2.connect(database='sashank',user='sashank',password='x',host='localhost')
    cur = conn.cursor()
    statement = 'select * from "Books" where "Book-Title"=\'' + bookName + '\';'
    cur.execute(statement)
    a = cur.fetchone()
    conn.close()    
    if a == None:
        return "-1"
    else:
        return a[0]