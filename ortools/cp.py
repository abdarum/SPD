# -*- coding: utf-8 -*-

from __future__ import print_function
from ortools.linear_solver import pywraplp
from ortools.sat.python import cp_model
import copy
import os

def wczytaj_plik(nazwa_pliku):
	plik = open(nazwa_pliku)
	zawartosc = plik.read().splitlines()  
	data = [i.split() for i in zawartosc]  
	dane = [list(map(int, dat)) for dat in data] 
	dane.pop(0) 
	return dane



def milp():
	solver = pywraplp.Solver('simple_mip_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	
	dane = wczytaj_plik("in0.txt")
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
	
	solver.Minimize(cmax) 
	result_status = solver.Solve()
	assert result_status == pywraplp.Solver.OPTIMAL	


	print('Solution:')
	print('Objective value = ', solver.Objective().Value())
	
	
	
def cp():
	model = cp_model.CpModel()
	
	dane = wczytaj_plik("in0.txt")
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
		starts.append(model.NewIntVar(0, variablesMaxValue, ""))
		for j in range(0, len(N)):
			alfas[-1].append(model.NewIntVar(0,1, ""))
	
	
	#starts = solver.MakeIntVar(len(N),0,variablesMaxValue) #nie ma tego w pythonie	
	#starts = solver.MakeIntVar(len(N),0,variablesMaxValue) #nie ma tego w pythonie	
		

	
	cmax = model.NewIntVar( 0, variablesMaxValue, "cmax")
	
	for i in range(0, len(N)):
		model.Add(starts[i] >= N[i][0] )
		
	for i in range(0, len(N)):
		model.Add(cmax >= (starts[i] + N[i][1] + N[i][2] ) )   
	
	for i in range(0, len(N)):
		for j in range(i+1, len(N)):
			job1 = N[i]
			job2 = N[j]
			
			model.Add(starts[i] + N[i][1] <= starts[j] +
				alfas[i][j] * variablesMaxValue ) 
			model.Add(starts[j] + N[j][1] <= starts[i] +
				alfas[j][i] * variablesMaxValue ) 
			model.Add(alfas[i][j] + alfas[j][i] == 1 )
	
	model.Minimize(cmax) 
	solver = cp_model.CpSolver()
	result_status = solver.Solve(model)
	assert result_status == cp_model.OPTIMAL	

	print('Solution:')
	print('Objective value = ', solver.ObjectiveValue())
	
	
if __name__ == '__main__':
	milp()
	cp()