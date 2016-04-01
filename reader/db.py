#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sqlite3
from datetime import datetime

class DB(object):
    '''
    classdocs
    '''

    def __init__(self, username=None, password=None, hostname="localhost", port=None, dbname='mydb', filename='mydb.db'):
        '''
        Constructor
        '''
        self.username = username
        self.password = password
        self.hostname = hostname
        self.port = port
        self.filename  =  filename
        self.conn = sqlite3.connect(self.filename)
        self.cursor = self.conn.cursor()
        self.dbname = dbname
   
    def executeQuery(self, query):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor.execute('''%s''' % query)
        self.conn.close()      
    
    def insertSensorData(self, sensor_id, place_id, value):
        self.conn = sqlite3.connect(self.dbname)
        self.cursor.execute("""INSERT INTO sensor_measurement (sensor_id, place_id, value)
VALUES (?, ?, ?);""",(sensor_id, place_id, value))
        self.conn.close()
