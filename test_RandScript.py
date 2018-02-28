import random
import RandScript

def test_del_First_none():
	main_script =  ["pruebav2.py"]
	ref         =  []
	res         =  RandScript.delete_first(main_script)
	assert res  == ref


def test_del_First_copy():
	linecom        =  ["pruebav2.py", "a","b"]
	ref            =  ["a","b"]
	res            =  RandScript.delete_first(linecom)
	assert linecom == ["pruebav2.py","a","b"]
	assert res     == ref


def test_comprueba_cero():
	params      = []
	zero_params = RandScript.comprueba_cero(params)
	assert zero_params


def test_check():
	words      = ["a","b","c"]
	zero       = (len(words)==0)
	ref_chosen = "a"
	ref_error  = 0
	random.seed(1)
	
	res_error, res_chosen =  RandScript.check(zero, words)
	assert res_error      == ref_error
	assert res_chosen     == ref_chosen
	




	
