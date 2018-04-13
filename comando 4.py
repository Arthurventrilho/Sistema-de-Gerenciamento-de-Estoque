#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:21:27 2018

@author: gian.napolitano
"""

#Imprimir Dicionario e parar o ciclo   
    elif Comando == 4:
        for e in Estoque:
            print('{0}:{1}'.format(e, Estoque[e]['Quantidade']))