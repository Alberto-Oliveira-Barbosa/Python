#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 07:28:32 2018

@author: Alberto Oliveira Barbosa
"""
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

n = 0
while (True):
    n = input('\nDigite um valor para calcular o seu fatorial ou S para sair\n')

    if(n.upper()[0] == 'S'): break

    if(n.isnumeric()):
        resultado = int(fatorial(int(n)))
        print('Fatorial de %s é %d' % (n, resultado))
    elif(n != 'S'):
        print('Opção incorreta\n')
