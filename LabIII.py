#!/usr/bin/env python
# -*- coding: UTF-8 -*-

intVector = [None] * 5
count = 0
while (count < 5):
    intVector[count] = count + 10
    count = count + 1	
for i in range(0,5):
    print(intVector[i])
stringVector = ["Zé","João","Tonho"]
for i in range (0,len(stringVector)):
    print(stringVector[i])

stringVector[0] = "Maria"
for i in range (0,len(stringVector)):
    print(stringVector[i])	 	
