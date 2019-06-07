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
	zawartosc = plik.read().splitlines()  # kazda linia to inne zadanie
	data = [i.split() for i in zawartosc]  # każde zadanie to lista z trzema elementami
	dane = [list(map(int, dat)) for dat in data]  # zmiana string na int
	dane.pop(0)  # usuniecie liczby zadan bo nie bedzie juz potrzebne
	#dane.sort(key=operator.itemgetter(0))  # sortowanie względem r - czasu dostępności
	return dane



def main():
	
	#dane = [[0, 27, 78], [140, 7, 67], [14, 36, 54], [133, 76, 5]]
	
	solver = pywraplp.Solver('simple_mip_program', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	
	
	dane = wczytaj_plik("in50.txt")
	N = copy.deepcopy(dane) # zbior nieuszeregowany
	print(N)

	variablesMaxValue = 0
	for job in N:
		variablesMaxValue += job[0] + job[1] + job[2]
	
	# zmienne :
	# a l f y potrzebne do u s ta len ia k o l e jn o s c i :
	alfas = solver.MakeIntVarMatrix (len(N) ,
		len(N) , 0 , 1 ) 
		
	starts = sol v e r . MakeIntVarArray ( len(N) ,
		0 , variablesMaxValue ) 
		
	cmax = sol v e r . MakeIntVar ( 0 , variablesMaxValue , "cmax" )
	
	for i in range(0, len(N)):
		sol v e r . Add( s t a r t s [ i ] >= N[i][0] )
		
	for i in range(0, len(N)):
		sol v e r . Add(cmax >= (s t a r t s [ i ] + N[i][1] + N[i][2] ) )   
	
	for i in range(0, len(N)):
		for j in range(i+1, len(N)):
			job1 = N[i]
			job2 = N[j]
			
			sol v e r . Add( s t a r t s [ i ] + N[i][1] <= s t a r t s [ j ] +
				al f a s [ i , j ] * variablesMaxValue ) 
			sol v e r . Add( s t a r t s [ j ] + N[j][1] <= s t a r t s [ i ] +
				al f a s [ j , i ] * variablesMaxValue ) 
			sol v e r . Add( al f a s [ i , j ] + al f a s [ j , i ] == 1 )
	
	sol v e r . Minimize (cmax ) 
	Solver . Resul tS ta tus r e sul t S t a tu s = sol v e r . Solve ( ) 
	i f ( r e sul t S t a tu s != Solver . Resul tS ta tus .OPTIMAL):

		Console . WriteLine ( " Solver didn ’ t find optimal solu tion ! " ) 

	Console . WriteLine ( " Objec tive value = " + sol v e r . Objec tive ( ) . Value ( ) )
	
	
	
	#infinity = solver.infinity()
	

    # x and y are integer non-negative variables
	#x = solver.IntVar(0.0, infinity, 'x')
	
	#y = solver.IntVar(0.0, infinity, 'y')

	#print('Number of variables = ', solver.NumVariables())

    # x + 7 * y <= 17.5.
	#solver.Add(x + 7 * y <= 17.5)

    # x <= 3.5.
	#solver.Add(x <= 3.5)

	#print('Number of constraints = ', solver.NumConstraints())

    # Maximize x + 10 * y.
	#solver.Maximize(x + 10 * y)

	#result_status = solver.Solve()
    # The problem has an optimal solution.
	#assert result_status == pywraplp.Solver.OPTIMAL

    # The solution looks legit (when using solvers others than
    # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
	#assert solver.VerifySolution(1e-7, True)

	#print('Solution:')
	#print('Objective value = ', solver.Objective().Value())
	#print('x = ', x.solution_value())
	#print('y = ', y.solution_value())

	#print('\nAdvanced usage:')
	#print('Problem solved in %f milliseconds' % solver.wall_time())
	#print('Problem solved in %d iterations' % solver.iterations())
	#print('Problem solved in %d branch-and-bound nodes' % solver.nodes())


if __name__ == '__main__':
    main()