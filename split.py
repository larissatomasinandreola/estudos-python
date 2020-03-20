# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:43:13 2020

@author: Larissa
"""

# Função para quebrar uma string por ponto e vírgula e mostrar na tela como
# quebra de linha
nomes = 'Alexsandro Felix;Larissa;Adriano'
print(nomes)
nomesQuebraPontoVirgula = nomes.split(';')
print(nomesQuebraPontoVirgula)
for nome in nomesQuebraPontoVirgula:
    print(nome)

    
    
