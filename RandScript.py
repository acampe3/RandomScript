#!/usr/bin/python3

import sys
import random
import copy

def delete_first(arguments):
	deleted = copy.deepcopy(arguments)
	del deleted[0]
	return deleted;


arguments=sys.argv

if (len(arguments)==1):
	print("Faltan argumentos")
else:
	print(arguments)



