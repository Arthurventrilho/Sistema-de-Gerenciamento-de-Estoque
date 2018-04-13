#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:17:14 2018

@author: macbook
"""

#Remover item            
    elif Comando == 2:
        Nome_produto = input('Digite o nome do produto: ')
        
        #Verifica se o produto está no Dicionario
        if Nome_produto in Estoque:
            del Estoque[Nome_produto]
        else:
            print('Produto não encontrado')