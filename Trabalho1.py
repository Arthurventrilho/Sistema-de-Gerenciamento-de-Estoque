#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Arthur e Gianlucca

Exercício Programa: Sistema de Gerenciamento de Estoque
"""
import json

with open ("Arquivo.txt",'r') as arquivo:
    conteudo = arquivo.read()
    Estoque = json.loads(conteudo)

    
tela_empresa = True
 
while tela_empresa:
    
    print('Controle loja')
    print('0 - Sair') 
    print('1 - Adicionar loja')
    print('2 - Remover loja')
    print('3 - Entrar loja')
    
    Selecao = int(input('Insira um numero:'))
    
    while Selecao not in [0,1,2,3]:
        print('Comando invalido')
        print()
        print('Controle loja')
        print('0 - Sair') 
        print('1 - Adicionar loja')
        print('2 - Remover loja')
        print('3 - Entrar loja')
        
        Selecao = int(input('Insira um numero:'))
    
    if Selecao == 0:
        print('Até Mais!')
        tela_empresa = False

    elif Selecao == 1:
         Nome_loja = input('Digite o nome da loja:')
         
         while Nome_loja in Estoque:
             print()
             print('Loja já cadastrada')
             print()
             Nome_loja = input('Digite o nome da loja:')
             
         Estoque[Nome_loja] = {}

    elif Selecao == 2:
        if Estoque == {}:
            print()
            print('Não existe loja no Estoque')
            print()
        else:
            print('Essas são as lojas no Estoque:')
            for lojas in Estoque:
                print()
                print(lojas)
                print()
                Nome_loja = input('Digite o nome da loja:')
                if Nome_loja in Estoque:
                    del Estoque[Nome_loja]
                else:
                    print()
                    print('Comando invalido')
                    print()
                    
    elif Selecao == 3:
        if Estoque == {}:
            print()
            print('Não existem lojas no Estoque')
            print()
        else:
            print()
            print('Essas sao as lojas:')
            print()
            for lojas in Estoque:
                print('{0}'.format(lojas))

            Nome_loja = input('escolha uma loja:')
            
            while Nome_loja not in Estoque:
                print()
                print('loja inexistente')
                print()
                Nome_loja = input('escolha uma loja:')


            tela_loja = True
            
            #Ciclo para adicionar produtos e quantidades no Dicionário
            while tela_loja:
    
                #Menu inicial
                print("")
                print("")
                print('Controle Estoque')
                print('0 - Voltar as lojas')
                print('1 - Adicionar item') 
                print('2 - Remover item')
                print('3 - Alterar item')
                print('4 - Imprimir estoque')
                print()
                #Comandos
                Comando = int(input('Digite um numero: '))
            
                while Comando not in [0, 1, 2, 3, 4]:
                    print(' Comando invalido' )
                    print('')
                    print('Controle Estoque')
                    print('0 - Voltar as lojas')
                    print('1 - Adicionar item')
                    print('2 - Remover item')
                    print('3 - Alterar item')
                    print('4 - Imprimir estoque')
                    print()
                    Comando = int(input('Digite um numero: '))

                #Sair e parar o ciclo
                if Comando == 0:   
                    tela_loja = False
                    break
        
                #Adicionar item
                elif Comando == 1:
                    print()
                    Nome_produto = input('Digite o nome do produto: ')
                    print()
            
            #Verifica se o produto está no Dicionario
                    if Nome_produto in Estoque[Nome_loja]:
                        print()
                        print('Produto já cadastrado')
                        print()
                    else: 
                        Quantidade_inicial = int(input('Digite a quantidade do produto: '))
                
                        #Verifica se a quantidade é negativa ou positiva
                        while Quantidade_inicial <= 0:
                            print()
                            print('Quantidade inicial não pode ser negativa')
                            print()
                            Quantidade_inicial = int(input('Digite a quantidade do produto: '))
                            print()
                            
                        #Verifica se o preco é negativo ou positivo
                        print()
                        Preco = float(input('Digite o preco do produto: '))
                        print()
                        while Preco <= 0:
                            print()
                            print('Preco inicial tem que ser maior que zero')
                            Preco = float(input('Digite o preco do produto: '))
                            print()
                        Estoque[Nome_loja][Nome_produto] = {'Quantidade': Quantidade_inicial, 'Preco': Preco}
                    
                #Remover item            
                elif Comando == 2:
                    if len(Estoque[Nome_loja]) == {}:
                        print()
                        print('Nao ha produtos')
                        print('')
                    else:
                        print()
                        print('Esses são os produtos da loja: ')
                        print()
                        for produtos in Estoque[Nome_loja]:
                            print(produtos)
                        Nome_produto = input('Digite o nome do produto: ')
                        
                #Verifica se o produto está no Dicionario
                        if Nome_produto in Estoque[Nome_loja]:
                            del Estoque[Nome_loja][Nome_produto]
                            print()
                            print('Estoque atualizado')
                        else:
                            print()
                            print('Produto não encontrado')
                            print()
                        
                        print()
                #Alterar item    
                elif Comando == 3:
                    if len(Estoque[Nome_loja]) == 0:
                        print()
                        print('Não há produtos')
                        print('')
                        ativador = False
                        
                    else:
                        print()
                        print('Esses são os produtos da loja: ')
                        for produtos in Estoque[Nome_loja]:
                            print(produtos)
                            print()
                        
                        Nome_produto = input('Digite o nome do produto: ') 
            
                        #Verifica se o produto está no Dicionario
                        if Nome_produto in Estoque[Nome_loja]:
            
                            print('')
                            print('Controle Produto')
                            print('0 - Voltar')
                            print('1 - Alterar Quantidade ')
                            print('2 - Alterar Preco')
                            print('3 - Alterar Quantidade e Preco')
                            print()
                
                            Escolha = int(input('Digite a sua escolha: '))
            
                            while Escolha not in [0, 1, 2 ,3]:
                                print()
                                print('Escolha invalida')
                                Escolha = int(input('Digite a sua escolha: '))
                     
                            if Escolha == 0:
                                print()
                                
                                
                    
                            if Escolha == 1:
                                Quantidade = int(input('Digite a quantidade do produto: '))
                    
                                Estoque[Nome_loja][Nome_produto]['Quantidade'] += Quantidade
                                print()
                                print('Novo estoque de {0}: {1}'.format(Nome_produto,
                                Estoque[Nome_loja][Nome_produto]['Quantidade']))
                                print()
                
                            if Escolha == 2:
                                Preco = float((input('Digite o preco do produto: ')))
                                Estoque[Nome_loja][Nome_produto]['Preco'] += Preco
                                print()
                                print('Valor de {0} alterado para: R${1:.2f}'.format(Nome_produto,
                                Estoque[Nome_loja][Nome_produto]['Preco']))
                                print()
                
                            if Escolha == 3: 
                                Quantidade = int(input('Digite a quantidade do produto: '))
                                Preco = float((input('Digite o preco do produto: ')))
                                Estoque[Nome_loja][Nome_produto]['Quantidade'] += Quantidade
                                Estoque[Nome_loja][Nome_produto]['Preco'] += Preco
                                print()
                                print('Novo estoque de {0} : a quantidade é {1} e custa {2:.2f}'.
                                format(Nome_produto, Estoque[Nome_loja][Nome_produto]['Quantidade'],
                                Estoque[Nome_loja][Nome_produto]['Preco'])) 
                                print()
                
                        else:
                            print()
                            print('Produto não encontrado')
                            print()
                    
                
                #Imprimir Dicionario e parar o ciclo   
                elif Comando == 4:
            
                    if Estoque == {}:
                        print('Seu estoque está vazio!')
                        print()
                
                    else:
                        print('')
                        print('Impressao')
                        print('0 - Sair')
                        print('1 - Imprimir Valor monetário')
                        print('2 - Imprimir Quantidade e Preco')
                        print()
                
                
                        Tipo_impressao = int(input('Faça sua escolha: '))
                
                        while Tipo_impressao not in [0, 1, 2, 3]:
                            print()
                            print('Tipo de impressão inválido')
                            print()
                            Tipo_impressao = int(input('Faça sua escolha: '))
                
                        if Tipo_impressao == 0:
                            print()
                            print('Até mais')
                            print()
                            break
                
                        if Tipo_impressao == 1:
                            valor_monetario = 0.0
                            for g in Estoque[Nome_loja]:
                                valor_monetario += Estoque[Nome_loja][g]['Quantidade']*Estoque[Nome_loja][g]['Preco']
                            print()
                            print('O valor monetário do estoque é de R${0}'.format(valor_monetario))
                            print()
                    
                        if Tipo_impressao == 2: 
                            for e in Estoque[Nome_loja]:
                                print()
                                print('{0}: Quantidade: {1}, Preco {2}'.format(e, Estoque[Nome_loja][e]['Quantidade'], Estoque[Nome_loja][e]['Preco']))
                                print()
                                
                            for f in Estoque[Nome_loja]:
                                if Estoque[Nome_loja][f]['Quantidade'] < 0:
                                    print()
                                    print('Cuidado, estoque de {0} está negativo'.format(f))
                                    print()
        
with open("Arquivo.txt",'w') as arquivo:
    conteudo = json.dumps(Estoque)
    
    arquivo.write(conteudo)
