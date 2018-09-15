#!/usr/bin/env python3

"""
	Exercicio propostos:
	Execicio do capitulo 1 ao 5
	1 - Implementar duas funções:
		* Uma que converta temperatura em graus Ceulsius para Fahrenheit
		* Outra que conver temperatura em graus Fahrenheit para Celsius
		obs: Lembrando que : F = 9C / 5 + 32

"""

def celsiusToFahrenheit(celsius):
	try:
		_celsius = int(celsius)
	except Exception as e:
		print('valor passado não é um numero')
		return false

	return int(9 * _celsius / 5 + 32)

def fahrenheitToCelsius(fah):
	try:
		_fah = int(fah)
	except Exception as e:
		print('valor passado não é um numero')
		return false

	return int((_fah - 32) /1.8)

print ("celsius para fahrenheit 0 F:%d" % celsiusToFahrenheit(0))
print ("celsius para fahrenheit 10 F:%d" % celsiusToFahrenheit(10))
print ("celsius para fahrenheit 50 F:%d" % celsiusToFahrenheit(50))
print ("celsius para fahrenheit 100 F:%d" % celsiusToFahrenheit(100))

print ("fahrenheit para celsius 0 C:%d" % fahrenheitToCelsius(0))
print ("fahrenheit para celsius 10 C:%d" % fahrenheitToCelsius(10))
print ("fahrenheit para celsius 50 C:%d" % fahrenheitToCelsius(50))
print ("fahrenheit para celsius 100 C:%d" % fahrenheitToCelsius(100))