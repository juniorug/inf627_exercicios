#!/usr/bin/env python
# -*- coding: UTF-8 -*-

quente = 40
frio = 10

while(True):
    atual = int(input("Digite a temperatura: "))
    print("Atual tem valor: %d" % atual)

    if( atual == frio ):
        print("FRIO")
    elif( atual == quente ):
        print("Quente")
    elif((atual > frio) and (atual < quente)):
        print ("normal")
    else:
        print("Temperatura Extrema")
