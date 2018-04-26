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
    
    print()
    print('Controle loja')
    print('0 - Sair') 
    print('1 - Adicionar loja')
    print('2 - Remover loja')
    print('3 - Entrar loja')
    
    Selecao = int(input('Insira um numero:'))
    
    while Selecao not in [0,1,2,3]:
        print('Comando invalido')
        print()
        print(20*'<>')
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
             print('Loja já cadastrada')
             print()
             print(20*'<>')
             Nome_loja = input('Digite o nome da loja:')
             
         Estoque[Nome_loja] = {}

    elif Selecao == 2:
        if Estoque == {}:
            print()
            print('Não existem lojas no Estoque')
            print()
            print(20*'<>')

        else:
            print('Essas são as lojas no Estoque:')
            for lojas in Estoque:
                print(lojas)
            Nome_loja = input('Digite o nome da loja:')
            if Nome_loja in Estoque:
                del Estoque[Nome_loja]
            else:
                print()
                print('Comando invalido')
                print()
                print(20*'<>')
                    
    elif Selecao == 3:
        if Estoque == {}:
            print()
            print('Não existem lojas no Estoque')
            print()
            print(20*'<>')
        else:
            print()
            print('Essas sao as lojas:')
            for lojas in Estoque:
                print('{0}'.format(lojas))

            Nome_loja = input('escolha uma loja:')
            
            while Nome_loja not in Estoque:
                print()
                print('loja inexistente')
                print()
                print(20*'<>')
                Nome_loja = input('escolha uma loja:')


            tela_loja = True
            
            #Ciclo para adicionar produtos e quantidades no Dicionário
            while tela_loja:
    
                #Menu inicial
                print("")
                print('Controle Estoque')
                print('0 - Voltar as lojas')
                print('1 - Adicionar item') 
                print('2 - Remover item')
                print('3 - Alterar item')
                print('4 - Imprimir estoque')
                
                #Comandos
                Comando = int(input('Digite um numero: '))
            
                while Comando not in [0, 1, 2, 3, 4]:
                    print()
                    print('Comando invalido' )
                    print()
                    print(20*'<>')
                    print()
                    print('Controle Estoque')
                    print('0 - Voltar as lojas')
                    print('1 - Adicionar item')
                    print('2 - Remover item')
                    print('3 - Alterar item')
                    print('4 - Imprimir estoque')
                    Comando = int(input('Digite um numero: '))

                #Sair e parar o ciclo
                if Comando == 0:   
                    tela_loja = False
                    break
        
                #Adicionar item
                elif Comando == 1:
                    Nome_produto = input('Digite o nome do produto: ')
            
            #Verifica se o produto está no Dicionario
                    if Nome_produto in Estoque[Nome_loja]:
                        print('Produto já cadastrado')
                        print()
                        print(20*'<>')
                    else:
                        print()
                        Quantidade_inicial = int(input('Digite a quantidade do produto: '))
                
                        #Verifica se a quantidade é negativa ou positiva
                        while Quantidade_inicial <= 0:
                            print('Quantidade inicial tem que ser maior que zero')
                            Quantidade_inicial = int(input('Digite a quantidade do produto: '))
                        print()
                            
                        #Verifica se o preco é negativo ou positivo
                        Preco = float(input('Digite o preco do produto: '))
                        while Preco <= 0:
                            print('Preco inicial tem que ser maior que zero')
                            Preco = float(input('Digite o preco do produto: '))
                        print() 
                        print(20*'<>')    
                        Estoque[Nome_loja][Nome_produto] = {'Quantidade': Quantidade_inicial, 'Preco': Preco}
                    
                #Remover item            
                elif Comando == 2:
                    if Estoque[Nome_loja] == {}:
                        print()
                        print('Nao ha produtos')
                        print()
                        print(20*'<>')
                    else:
                        print()
                        print('Esses são os produtos da loja: ')
                        for produtos in Estoque[Nome_loja]:
                            print(produtos)
                        Nome_produto = input('Digite o nome do produto: ')
                        
                #Verifica se o produto está no Dicionario
                        if Nome_produto in Estoque[Nome_loja]:
                            del Estoque[Nome_loja][Nome_produto]
                            print()
                            print('Estoque atualizado')
                            print()
                            print(20*'<>')
                            
                        else:
                            print()
                            print('Produto não encontrado')
                            print()
                            print(20*'<>')
                        
                        print()
                #Alterar item    
                elif Comando == 3:
                    if Estoque[Nome_loja] == {}:
                        print()
                        print('Não há produtos')
                        print()
                        print(20*'<>')
                        
                        
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
                                print()
                                print(20*'<>')
                                Escolha = int(input('Digite a sua escolha: '))
                     
                            if Escolha == 0:
                                print()
                                print(20*'<>')
                                
                            if Escolha == 1:
                                Quantidade = int(input('Digite a quantidade do produto: '))
                    
                                Estoque[Nome_loja][Nome_produto]['Quantidade'] += Quantidade
                                print()
                                print('Novo estoque de {0}: {1}'.format(Nome_produto,
                                Estoque[Nome_loja][Nome_produto]['Quantidade']))
                                print()
                                print(20*'<>')
                
                            if Escolha == 2:
                                Preco = float((input('Digite o preco do produto: ')))
                                Estoque[Nome_loja][Nome_produto]['Preco'] += Preco
                                print()
                                print('Valor de {0} alterado para: R${1:.2f}'.format(Nome_produto,
                                Estoque[Nome_loja][Nome_produto]['Preco']))
                                print()
                                print(20*'<>')
                
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
                                print(20*'<>')
                
                        else:
                            print()
                            print('Produto não encontrado')
                            print()
                            print(20*'<>')
                    
                
                #Imprimir Dicionario e parar o ciclo   
                elif Comando == 4:
            
                    if Estoque == {}:
                        print('Seu estoque está vazio!')
                        print()
                        print(20*'<>')
                
                    else:
                        print()
                        print('Impressao')
                        print('0 - Voltar')
                        print('1 - Imprimir Valor monetário')
                        print('2 - Imprimir Quantidade e Preco')
                        print()
                
                
                        Tipo_impressao = int(input('Faça sua escolha: '))
                
                        while Tipo_impressao not in [0, 1, 2, 3]:
                            print()
                            print('Tipo de impressão inválido')
                            print()
                            print(20*'<>')
                            print()
                            Tipo_impressao = int(input('Faça sua escolha: '))
                
                        if Tipo_impressao == 0:
                            print()
                            print(20*'<>')
                           
                        if Tipo_impressao == 1:
                            valor_monetario = 0.0
                            for g in Estoque[Nome_loja]:
                                valor_monetario += Estoque[Nome_loja][g]['Quantidade']*Estoque[Nome_loja][g]['Preco']
                            print()
                            print('O valor monetário do estoque é de R${0}'.format(valor_monetario))
                            print()
                            print(20*'<>')
                    
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
                            print(20*'<>')
        
with open("Arquivo.txt",'w') as arquivo:
    conteudo = json.dumps(Estoque)
    
    arquivo.write(conteudo)
