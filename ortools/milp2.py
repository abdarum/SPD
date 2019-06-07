# -*- coding: utf-8 -*-

from __future__ import print_function
from ortools.linear_solver import pywraplp
import copy
import os

class RPQ_Job:
	def __init__(self, nr, r, p, q):
		self.nr = nr
		self.r = r
		self.p = p
		self.q = q

def wczytaj_plik(nazwa_pliku):
	plik = open(nazwa_pliku)
	zawartosc = plik.read().splitlines()  
	data = [i.split() for i in zawartosc]  
	dane = [list(map(int, dat)) for dat in data] 
	dane.pop(0) 
	return dane



def main():
	
	
	solver = pywraplp.Solver('simple_mip_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	
	
	dane = wczytaj_plik("in50.txt")
	N = copy.deepcopy(dane) #
	print(N)

	variablesMaxValue = 0
	for job in N:
		variablesMaxValue += job[0] + job[1] + job[2]
	
	#alfas = solver.MakeIntVar(len(N), len(N), 0, 1) #nie ma tego w pythonie	
	alfas = list()
	starts = list()
	for i in range(0, len(N)):
		alfas.append(list())
		starts.append(solver.IntVar(0, variablesMaxValue, ""))
		for j in range(0, len(N)):
			alfas[-1].append(solver.IntVar(0,1, ""))
	
	
	#starts = solver.MakeIntVar(len(N),0,variablesMaxValue) #nie ma tego w pythonie	
	#starts = solver.MakeIntVar(len(N),0,variablesMaxValue) #nie ma tego w pythonie	
		

	
	cmax = solver.IntVar( 0, variablesMaxValue, "cmax")
	
	for i in range(0, len(N)):
		solver.Add(starts[i] >= N[i][0] )
		
	for i in range(0, len(N)):
		solver.Add(cmax >= (starts[i] + N[i][1] + N[i][2] ) )   
	
	for i in range(0, len(N)):
		for j in range(i+1, len(N)):
			job1 = N[i]
			job2 = N[j]
			
			solver.Add(starts[i] + N[i][1] <= starts[j] +
				alfas[i][j] * variablesMaxValue ) 
			solver.Add(starts[j] + N[j][1] <= starts[i] +
				alfas[j][i] * variablesMaxValue ) 
			solver.Add(alfas[i][j] + alfas[j][i] == 1 )
	
	print("test")
	
	solver.Minimize(cmax) 
	print("test2")
	result_status = solver.Solve()
	print("test3")
	assert result_status == pywraplp.Solver.OPTIMAL	
	print("test4")

	print('Solution:')
	print('Objective value = ', solver.Objective().Value())
	
if __name__ == '__main__':
    main()