#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os, sys

#Iago Augusto - Plunter Apps // www.plunter.com
#Use a lista para memorizar ou consultar coisas enquanto usa o terminal.

#The-list
segunda = ["Quimica", "Historia", "Portugues", "Espanhol", "Matematica"]
terca = ["Matematica", "Portugues", "Filosofia", "Quimica", "Portugues"]
quarta = ["Biologia", "Fisica", "Historia", "Sociologia", "Ingles"]
quinta = ["Matematica", "Geografia", "Geografia", "Biologia", "Portugues"]
sexta = ["Ingles", "Matematica", "Fisica", "Ed. Fisica", "Ed. Fisica"]

#The-function
def print_1(lista):
	for each_item in lista:
		print(each_item)

print """\n>> Terminal Lists v0.5 - Plunter Apps
"""
#main-loop
done = False
while not done:

	lista = input("\nDigite o dia que você deseja ver: ")

	print "\nEis o seu horário:"
	if lista == segunda:
		print_1(segunda)
	elif lista == terca:
		print_1(terca)
	elif lista == quarta:
		print_1(quarta)
	elif lista == quinta:
		print_1(quinta)
	elif lista == sexta:
		print_1(sexta)
