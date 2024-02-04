# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:25:43 2019

@author: lafagev
"""

import sqlite3
def setup_tracks(db,data_file):
    #Create and populate the Tracks table with the data fro; the open file data_file
    data_file.readlines() 
    #Connect to the data base
    con=sqlite3.connect(db)
    #Create a cursor
    cur=con.cursor()
    
    #Create the Tracks table
    cur.execute('CREATE TABLE Tracks'+'(Title TEXT, id INTEGER, iTi;e INTEGER)')
    for line in data_file:
        data=line.strip().split(',')
        Title= 