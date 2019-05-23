#!/usr/bin/env python3
from schrage import *


def carlier(permut_tasks,ub = 10000000000):
    a = 0
    b = 0
    c = -1

    tasks = copy.deepcopy(permut_tasks)
    u, pi = schrage(tasks) # line 2

    if u < ub: # line 3
        ub = u # line 4

    #count b line 6
    cpop = 0
    time_of_end_tasks = []
    for i in range(len(pi)):
        cpop = max(cpop, max(pi[i][0],cpop) + pi[i][1])
        time_of_end_tasks.append(cpop)
        if cpop + pi[i][2] == u:
            b = i

    #count a line 7
    sum_tasks = 0
    for i in range(b, -1, -1):
        sum_tasks +=pi[i][1]
        if u == sum_tasks + pi[i][0]+pi[b][2] and time_of_end_tasks[i-1] != pi[i][1]:
            a = i
            break

    #count c line 8
    for i in range(a, b+1):
        if pi[i][2] < pi[b][2]:
            c = i

    print("A: "+str(a)+"\tB: "+str(b)+"\tC: "+str(c))
    if c < 0:# line 9 
        return ub # line 10

    #count r_prim, q_prim i p_prim line 13
    p_prim = 0
    r_prim = pi[c+1][0]
    q_prim = pi[c+1][2]
    for i in range(c+1, b+1): # line 12 
        p_prim += pi[i][1]
        if r_prim > pi[i][0]:
            r_prim = pi[i][0]
        if q_prim > pi[i][2]:
            q_prim = pi[i][2]

    #Left child, change r time for critical task line 14
    old_pi_r_c = pi[c][0]
    pi[c][0]=max(pi[c][0], r_prim+p_prim)

    #set block of data with c line 14
    p_bis = 0
    r_bis = pi[c][0] 
    q_bis = pi[c][2]
    for i in range(c, b + 1):
        p_bis += pi[i][1]
        if r_bis > pi[i][0]:
            r_bis = pi[i][0]
        if q_bis > pi[i][2]:
            q_bis = pi[i][2]

    lb, O = schrage_pmtn(pi)# line 15
    lb = max(max(r_prim + q_prim + p_prim, r_bis+p_bis+q_bis),lb) # line 16
    if lb < ub: # line 17
        ub = carlier(pi, ub) # line 18
    pi[c][0] = old_pi_r_c # line 20

    #Right child, change q time for critical task
    old_pi_q_c = pi[c][2]  # line 20
    pi[c][2] = max(pi[c][2], q_prim + p_prim) #line 21

    #Prepare new block with critical task
    p_bis = 0
    r_bis = pi[c][0]
    q_bis = pi[c][2]
    for i in range(c, b + 1):
        p_bis += pi[i][1]
        if r_bis > pi[i][0]:
            r_bis = pi[i][0]
        if q_bis > pi[i][2]:
            q_bis = pi[i][2]

    lb, O = schrage_pmtn(pi) # line 22
    lb = max(max(r_prim + q_prim + p_prim, r_bis+p_bis+q_bis), lb) # line 23 
    if lb < ub: # line 24
        ub = carlier(pi, ub) # line 25 
    pi[c][2] = old_pi_q_c # line 27

    return ub 


