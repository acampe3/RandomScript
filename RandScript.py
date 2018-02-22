#!/usr/bin/python3

import sys
import random
import copy

def delete_first(arguments):
	deleted = copy.deepcopy(arguments)
	del deleted[0]
	return deleted;
	
def choose(argu_del):
	ale=random.choice(argu_del)
	return ale;


arguments=sys.argv
argu_del=delete_first(arguments)

if (len(arguments)==1):
	print("Faltan argumentos")
else:
	chosen=choose(argu_del)
	argu_del=' '.join(argu_del)
	print("Valores posibles:",argu_del)
	print("Valor random: ",chosen)



