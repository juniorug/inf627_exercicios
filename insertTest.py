#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from db import DB

db = DB(None, None, "localhost", None, 'mydb')
db.insertSensorData(1, 1, 39)
print("inserted")
