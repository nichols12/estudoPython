#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Exercicio propostos:
	Execicio do capitulo 1 ao 5
	3 - Implementar uma função que receba uma lista de listas de comprimeos quaisquer e retorner 
		de uma dimensão
"""
def oneLevelLists(lista):
	newList = []
	for item in lista:
		if type(item) is list:
			newList += oneLevelLists(item)
		else:
			newList.append(item)
	return newList

print( oneLevelLists([1,2,3,4,4,[1,2,3,4,],2,3,[7,8,[5,6]]]))