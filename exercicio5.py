#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Exercicio propostos:
	Execicio do capitulo 1 ao 5
	5 - Escreva um função que:
		* Receba uma frase como parametro.
		* Retorne uma nova frase com cada palavra com as letras invertidas
"""
def reverseWords(phrase):
	arrayPhrase = phrase.split(' ')
	newPhrase = []
	for word in arrayPhrase:
		newPhrase.append(word[::-1])
	print(' '.join(newPhrase))
	
reverseWords('cara se isso der certo de primeira vai ser foda')
""" deu certo de primeira!!!"""