#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arthur e Gianlucca

Exercício Programa: Sistema de Gerenciamento de Estoque
"""
#Dicionario
Estoque = {} 

ativador = False

print('Controle loja')
print('0 - Sair') 
print('1 - Adicionar loja')
print('2 - Remover loja')
print('3 - Entrar loja')


Selecao = int(input('Insira um numero:'))

while Selecao not in [0,1,2,3,4]:
    print('Comando invalido')
    print("")
    print('Controle loja')
    print('0 - Sair') 
    print('1 - Adicionar loja')
    print('2 - Remover loja')
    print('3 - Entrar loja')
    Selecao = int(input('Insira um numero:'))
 
while Selecao >= 0 and Selecao <4:
    
    if Selecao == 0:
        print('Até Mais!')
        break

    elif Selecao == 1:
         Nome_loja = input('Digite o nome da loja:')
         
         while Nome_loja in Estoque:
             print('Loja já cadastrada')
             Nome_loja = input('Digite o nome da loja:')
         Estoque[Nome_loja] = {}
         ativador = True
         
    elif Selecao == 2:
        if Estoque == {}:
            print('Não existe loja no Estoque')
            print('')
            print('')
        else:
            print('Essas são as lojas no Estoque:')
            for g in Estoque:
                print(g)
                Nome_loja = input('Digite o nome da loja:')
            del Estoque[Nome_loja]
            
            
#Menu inicial
print('Controle Estoque')
print('0 - Sair')
print('1 - Adicionar item')
print('2 - Remover item')
print('3 - Alterar item')
print('4 - Imprimir estoque')

#Comandos
Comando = int(input('Digite um numero: '))



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
            Preco = float(input('Digite o preco do produto: '))
            while Preco <= 0:
                print('Preco inicial tem que ser maior que zero')
                Preco = float(input('Digite o preco do produto: '))
                
            Estoque[Nome_produto] = {'Quantidade': Quantidade_inicial, 'Preco': Preco}
                
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
        
            print('')
            print('Controle Produto')
            print('0 - Sair')
            print('1 - Alterar Quantidade ')
            print('2 - Alterar Preco')
            print('3 - Alterar Quantidade e Preco')
            
            Escolha = int(input('Digite a sua escolha: '))
        
            while Escolha not in [0, 1, 2 ,3]:
                print('Escolha invalida')
                Escolha = int(input('Digite a sua escolha: '))
                 
            if Escolha == 0:
                print('Até Mais!')
                break
                
            if Escolha == 1:
                Quantidade = int(input('Digite a quantidade do produto: '))
                
                Estoque[Nome_produto]['Quantidade'] += Quantidade
                print('Novo estoque de {0}: {1}'.format(Nome_produto,
                Estoque[Nome_produto]['Quantidade']))
            
            if Escolha == 2:
                Preco = float((input('Digite o preco do produto: ')))
                Estoque[Nome_produto]['Preco'] += Preco
                print('Novo estoque de {0}: {1}'.format(Nome_produto,
                Estoque[Nome_produto]['Preco']))
            
            if Escolha == 3: 
                Quantidade = int(input('Digite a quantidade do produto: '))
                Preco = float((input('Digite o preco do produto: ')))
                Estoque[Nome_produto]['Quantidade'] += Quantidade
                Estoque[Nome_produto]['Preco'] += Preco
                print('Novo estoque de {0} : a quantidade é {1} e custa {2}'.
                      format(Nome_produto, Estoque[Nome_produto]['Quantidade'],
                             Estoque[Nome_produto]['Preco'])) 
            
        else:
            print('Produto não encontrado')
            
    #Imprimir Dicionario e parar o ciclo   
    elif Comando == 4:
        
        if Estoque == {}:
            print('Seu estoque está vazio!')
            
        else:
            print('')
            print('Impressao')
            print('0 - Sair')
            print('1 - Imprimir Valor monetário')
            print('2 - Imprimir Quantidade e Preco')
            
            
            Tipo_impressao = int(input('Faça sua escolha: '))
            
            while Tipo_impressao not in [0, 1, 2, 3]:
                print('Tipo de impressão inválido')
                Tipo_impressao = int(input('Faça sua escolha: '))
            
            if Tipo_impressao == 0:
                print('Até mais')
                break
            
            if Tipo_impressao == 1:
                valor_monetario = 0.0
                for g in Estoque:
                    valor_monetario += Estoque[g]['Quantidade']*Estoque[g]['Preco']
                print('O valor monetário do estoque é de R${0}'.format(valor_monetario))
                
            if Tipo_impressao == 2: 
                for e in Estoque:
                    print('{0}: {1}, {2}'.format(e, Estoque[e]['Quantidade'], 
                          Estoque[e]['Preco']))
            
                for f in Estoque:
                    if Estoque[f]['Quantidade'] < 0:
                        print('Cuidado, estoque {0} está negativo'.format(f))
                        
                
    
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
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        