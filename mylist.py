#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import os, sys

#Iago Augusto - Plunter Apps // www.plunter.com
#Terminal list - horarios.py improved!
#Este é um algoritmo de listas que precisa ser melhorado!
#Bom, existem várias maneiras de uso. No meu caso utilizei para ver meus horarios escolares.
#Mas existem certas versões e implementações de loops que podem ser úteis!
#Por que horarios de escola? Pq eu fico até tarde usando meu terminal linux(programando e brincando)
#E quando eu vou dormir, ou preciso estudar e acabo esquecendo as aulas de amanhã, acabo dando uma olhada por um simples comando.

#LISTA
segunda = ["Quimica", "Historia", "Portugues", "Espanhol", "Matematica"]
terca = ["Matematica", "Portugues", "Filosofia", "Quimica", "Portugues"]
quarta = ["Biologia", "Fisica", "Historia", "Sociologia", "Ingles"]
quinta = ["Matematica", "Geografia", "Geografia", "Biologia", "Portugues"]
sexta = ["Ingles", "Matematica", "Fisica", "Ed. Fisica", "Ed. Fisica"]
#FIM-LISTA

print """\n>> Terminal Lists v0.3 - Plunter Apps
"""

done = False
while not done:

	lista = input("\nDigite o dia que você deseja ver: ")

	print "\nEis o seu horário:"
	if lista == segunda:
			print segunda
	elif lista == terca:
		print terca
	elif lista == quarta:
		print quarta
	elif lista == quinta:
		print quinta
	elif lista == sexta:
		print sexta
