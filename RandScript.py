#!/usr/bin/python3

import sys
import random
import copy

def delete_first(arguments):
	deleted = copy.deepcopy(arguments)
	del deleted[0]
	return deleted
	
def choose(argu_del):
	ale = random.choice(argu_del)
	return ale
	
def comprueba_cero(argu_del):
	total_words = len(argu_del)
	zero        = (total_words==0)
	return zero

arguments=sys.argv
argu_del=delete_first(arguments)
void = comprueba_cero(argu_del)

if (void):
	print("Faltan argumentos")
else:
	chosen=choose(argu_del)
	argu_del=' '.join(argu_del)
	print("Valores posibles:",argu_del)
	print("Valor random: ",chosen)



