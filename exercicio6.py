#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Exercicio propostos:
	Execicio do capitulo 1 ao 5
	6 - Crie uma Função que:
		* Receba uma lista de tuplas (dados), um inteiro(chave,zero por padrão igual) e um 
		booleano (rever, false por padrão).
		* Retorne dados ordenados pelo item indicado pela chave em ordem decrestente se reverso for verdadeiro
"""
def sortBy(lista, keyTuple=0, reverseTuple=False):
	def keyfunc(elem):
		return elem[keyTuple]

	return sorted(lista, key=keyfunc,reverse=reverseTuple)
	
print(sortBy([(1,3,4,5,6,),(2,4,5,6,1,5),(9,6,5,4,12,3)], 1))
print(sortBy([(1,3,4,5,6,),(2,4,5,6,1,5),(9,6,5,4,12,3)], 2))
print(sortBy([(1,3,4,5,6,),(2,4,5,6,1,5),(9,6,5,4,12,3)], 2,True))