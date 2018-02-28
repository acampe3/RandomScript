#!/usr/bin/python3

import sys
import random
import copy

#Params: arguments passed in main script
#Return: deleted argument 0
#This function delete argument 0, that is name of script
def delete_first(arguments):
	deleted = copy.deepcopy(arguments)
	del deleted[0]
	return deleted

#Params: argu_del, arguments with name of script deleted
#Return: ale, one argument randomly 
#This function randomize an string for return only 1
def choose(argu_del):
	ale = random.choice(argu_del)
	return ale

#Params: argu_del, arguments with name of script deleted
#Return: zero, a sentence that equals length of string to 0
#This function make a sentence that equals length of string to 0
def comprueba_cero(argu_del):
	total_words = len(argu_del)
	zero        = (total_words==0)
	return zero

#Params: cero_palabras, a sentence for do an if-else
#		 argu_del, arguments with name of script deleted
#Return: error, exit code
#		 chosen, argument chosed randomly or error message
#This function take an argument randomly or error message and exit code 1 or 0
def check(cero_palabras,argu_del):
	
	error  = 1
	chosen = ""
	
	if(cero_palabras):
		error  = 1
		chosen = "Faltan Argumentos"
	else:
		error  = 0
		chosen = choose(argu_del)
	
	return  error, chosen


#Main struct if we use this code like a script declare all of variables
#and print error message or argument random
#convert exit code in 0 or 1
if __name__ == '__main__':
	arguments     = sys.argv
	argu_del      = delete_first(arguments)
	cero_palabras = comprueba_cero(argu_del)
	error, chosen = check(cero_palabras, argu_del)

	print(chosen)
	sys.exit(error)



