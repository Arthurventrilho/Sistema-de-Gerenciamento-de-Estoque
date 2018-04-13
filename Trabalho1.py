#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arthur e Gianlucca

Exercício Programa: Sistema de Gerenciamento de Estoque
"""


#Menu inicial
print('Controle Estoque')
print('0 - Sair')
print('1 - Adicionar item')
print('2 - Remover item')
print('3 - Alterar item')
print('4 - Imprimir estoque')

#Comandos
Comando = int(input('Digite um numero: '))

#Dicionario
Estoque = {} 

while Comando not in [0, 1, 2, 3, 4]:
    print(' Comando invalido' )
    print('')
    print('Controle Estoque')
    print('0 - Sair')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Alterar item')
    print('4 - Imprimir estoque')
    Comando = int(input('Digite um numero: '))

#Ciclo para adicionar produtos e quantidades no Dicionário
while Comando < 5 and Comando >= 0:

    #Sair e parar o ciclo
    if Comando == 0:   
        print('Até Mais!')
        break
    
    #Adicionar item
    elif Comando ==1:
        Nome_produto = input('Digite o nome do produto: ')
        
        #Verifica se o produto está no Dicionario
        if Nome_produto in Estoque:
            print('Produto já cadastrado')  
        else: 
            Quantidade_inicial = int(input('Digite a quantidade do produto: '))
            
            #Verifica se a quantidade é negativa ou positiva
            while Quantidade_inicial < 0:
                print('Quantidade inicial não pode ser negativa')
                Quantidade_inicial = int(input('Digite a quantidade do produto: '))
                
            print('') 
            
            #Verifica se o preco é negativo ou positivo
            preco = float(input('Digite o preco do produto: '))
            while preco <= 0:
                print('Preco inicial tem que ser maior que zero')
                preco = float(input('Digite o preco do produto: '))
                
            Estoque[Nome_produto] = {'Quantidade': Quantidade_inicial, 'preco': preco}
                
    #Remover item            
    elif Comando == 2:
        Nome_produto = input('Digite o nome do produto: ')
        
        #Verifica se o produto está no Dicionario
        if Nome_produto in Estoque:
            del Estoque[Nome_produto]
        else:
            print('Produto não encontrado')
            
    #Alterar item    
    elif Comando == 3:
        Nome_produto = input('Digite o nome do produto: ') 
        
        #Verifica se o produto está no Dicionario
        if Nome_produto in Estoque:
            Quantidade = int(input('Digite a quantidade do produto: '))
            Estoque[Nome_produto]['Quantidade'] += Quantidade
            print('Novo estoque de {0}: {1}'.format(Nome_produto,
              Estoque[Nome_produto]['Quantidade']))
        else:
            print('Produto não encontrado')
            
    #Imprimir Dicionario e parar o ciclo   
    elif Comando == 4:
        for e in Estoque:
            print('{0}:{1}'.format(e, Estoque[e]['Quantidade']))
            
    
    #Menu inicial
    print('')
    print('Controle Estoque')
    print('0 - Sair')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Alterar item')
    print('4 - Imprimir estoque')

    #Comandos
    Comando = int(input('Digite um numero: '))        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        