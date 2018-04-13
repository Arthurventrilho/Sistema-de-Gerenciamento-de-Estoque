#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 09:20:16 2018

@author: gian.napolitano
"""

#Adicionar item
    elif Comando ==1:
        Nome_produto = input('Digite o nome do produto: ')
        
        #Verifica se o produto está no Dicionario
        if Nome_produto in Estoque:
            print('Produto já cadastrado')  
        else: 
            Quantidade_inicial = int(input('Digite a quantidade do produto: '))
            
            #Verifica se a quantidade é negativa ou positiva
            if Quantidade_inicial < 0:
                print('Quantidade inicial não pode ser negativa')
                Quantidade_inicial = int(input('Digite a quantidade do produto: '))
                Estoque[Nome_produto] = {'Quantidade': Quantidade_inicial}
            else:
                Estoque[Nome_produto] = {'Quantidade': Quantidade_inicial}