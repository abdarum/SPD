#!/usr/bin/env python3
import copy
import operator
import time


#funkcja otwierajaca plik i przygotowująca data z pliku
def load_from_file(filename):
    plik = open(filename)
    file_in_string = plik.read().splitlines()  # kazda linia to inne zadanie
    data = [i.split() for i in file_in_string]  # każde zadanie to lista z trzema elementami
    data = [list(map(int, dat)) for dat in data]  # zmiana string na int
    data.pop(0)  # usuniecie liczby zadan bo nie bedzie juz potrzebne
    #data.sort(key=operator.itemgetter(0))  # sortowanie względem r - czasu dostępności
    return data

# dwa poniższe algorytmy dla złozoności obliczeniowej n^2
def schrage(data):
    l_not_ready_tasks = copy.deepcopy(data)  # zbior nieuszeregowany
    l_ready_tasks = [] # zbior gotowych do uszeregowania
    t = min(l_not_ready_tasks, key=operator.itemgetter(0))[0] #zmienna pomocnicza czas
    #t = 0 #zmienna pomocnicza czas
    Cmax = 0 #funkcja celu
    O = [] # czesciowa kolejnosc
    n = l_not_ready_tasks.index(min(l_not_ready_tasks, key=operator.itemgetter(0)))
    while len(l_not_ready_tasks) != 0 or len(l_ready_tasks) != 0:
        while len(l_not_ready_tasks) != 0 and  l_not_ready_tasks[n][0] <= t: # sprawdzamy najmniejszy czas przygotowania
            l_ready_tasks.append(l_not_ready_tasks.pop(n))
            if len(l_not_ready_tasks) != 0:
                n = l_not_ready_tasks.index(min(l_not_ready_tasks, key=operator.itemgetter(0)))
        if len(l_ready_tasks) == 0:
            t = l_not_ready_tasks[n][0]
        else:
            h = l_ready_tasks.index(max(l_ready_tasks, key=operator.itemgetter(2))) #wybor max dostarczenia
            e = l_ready_tasks.pop(h)
            #e.append(t)  # dodanie chwili rozpoczecia jako [3] elementu w e.
            t = t + e[1]
            Cmax = max(Cmax, t + e[2])
            O.append(e)
    l_not_ready_tasks = O
    return Cmax, O

def schrage_pmtn(data):
    l_not_ready_tasks=copy.deepcopy(data)
    l_ready_tasks = []
    O = []
    t = min(l_not_ready_tasks, key=operator.itemgetter(0))[0]  # zmienna pomocnicza czas
    Cmax = 0
    q0 = 999999999 # zgodnie z instrukcja ma być nieskończenie duze
    l = [0, 0, q0] # zadania aktualne
    n = l_not_ready_tasks.index(min(l_not_ready_tasks, key=operator.itemgetter(0)))

    while len(l_not_ready_tasks) != 0 or len(l_ready_tasks) != 0: # tak jak w podstawowym
        while len(l_not_ready_tasks) != 0 and l_not_ready_tasks[n][0] <= t:
            e = l_not_ready_tasks.pop(n) # zadanie gotowe do oddania
            l_ready_tasks.append(e)
            if len(l_not_ready_tasks) != 0:
                n = l_not_ready_tasks.index(min(l_not_ready_tasks, key=operator.itemgetter(0)))

            if e[2] > l[2]:  # porownanie czasow zadan i przerwanie
                l[1] = t - e[0]
                t = e[0]
                if l[1] > 0:
                    l_ready_tasks.append(l)  # kontynuacja przerwanego
        if len(l_ready_tasks) == 0: # reszta jak poprzednie
            t = l_not_ready_tasks[n][0]
        else:
            h = l_ready_tasks.index(max(l_ready_tasks, key=operator.itemgetter(2)))
            e = l_ready_tasks.pop(h)
            t = t + e[1]
            Cmax = max(Cmax, t + e[2])
            l = e
            O.append(e)
    l_not_ready_tasks = O
    return Cmax, O

