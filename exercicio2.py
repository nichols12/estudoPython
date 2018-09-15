#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
	Exercicio propostos:
	Execicio do capitulo 1 ao 5
	2 - Implemetar uma função que retorne verdadiro se o número for primo ( false caso contrário).
		Testar de 1 a 100. 

"""

def getPrimeNumbers(firstNumber, secondNumber):
	primeNumbers = []

	if firstNumber > secondNumber:
		return False

	for number in range(firstNumber,secondNumber):
		cont = 0
		for div in range(1,number):
			if number % div == 0:
				cont += 1
		if cont == 1:
			print(number)
			primeNumbers.append(number)
		else:
			print(False)
	print(primeNumbers)

getPrimeNumbers(1,100)
