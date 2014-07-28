#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os, sys

#Este algoritmo foi criado para ver a lista de horarios de sua sala.
#Esta é a versão 1.0 com alguns bugs, melhore o código!
#v01 - Iago Augusto

#LISTA
segunda = ["Quimica", "Historia", "Portugues", "Espanhol", "Matematica"]
terca = ["Matematica", "Portugues", "Filosofia", "Quimica", "Portugues"]
quarta = ["Biologia", "Fisica", "Historia", "Sociologia", "Ingles"]
quinta = ["Matematica", "Geografia", "Geografia", "Biologia", "Portugues"]
sexta = ["Ingles", "Matematica", "Fisica", "Ed. Fisica", "Ed. Fisica"]
#FIM-LISTA

print """
>> Horarios Padre Clemente v0.1
"""
lista = input("Digite o dia que você deseja ver: ")

print "\nEis o seu horário:"
if lista == segunda:
	for segunda in enumerate(segunda):
		print segunda
elif lista == terca:
	for terca in enumerate(terca):
		print terca
elif lista == quarta:
	for quarta in enumerate(quarta):
		print quarta
elif lista == quinta:
	for quinta in enumerate(quinta):
		print quinta	
elif lista == sexta:
	for sexta in enumerate(sexta):
		print sexta

print "\nObrigado por consultar utilizando nosso programa!"
while lista:
  caracter = raw_input("Deseja sair s/n: ")
  if caracter == 's':
	  quit()
