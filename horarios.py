#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os, sys

#Iago Augusto - Plunter Apps // www.plunter.com
#This algorithm is free to edit and anyone can improve it
#Why I use enumerate? Because this range can show the number of class, you know? like 0 - Math, 1 - Biology
#My list is in Portuguese because my school are in Brazil.
#Just change it!

#LISTA
segunda = ["Quimica", "Historia", "Portugues", "Espanhol", "Matematica"]
terca = ["Matematica", "Portugues", "Filosofia", "Quimica", "Portugues"]
quarta = ["Biologia", "Fisica", "Historia", "Sociologia", "Ingles"]
quinta = ["Matematica", "Geografia", "Geografia", "Biologia", "Portugues"]
sexta = ["Ingles", "Matematica", "Fisica", "Ed. Fisica", "Ed. Fisica"]
#FIM-LISTA

print "\n>> Horários Escolares v0.2 - Plunter Apps"

done = False
while not done:

	lista = input("\nDigite o dia que você deseja ver: ")

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
