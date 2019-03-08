#/usr/bin/python3

#import built-in modules

import itertools


def permutation_and_c_time(permutation_list):
    table = list()
    permutation_table = list(itertools.permutations(permutation_list))
    for i in range(0,len(permutation_table)):
        table.append([])
        table[i].insert(0,0)
        table[i].append(permutation_table[i])
    return table

def count_time(table):
    jobs = len(table)
    if jobs>0:
        machines = len(table[0]) 
        c_time = [[0] * machines for i in range(jobs)]

        for j in range(0,jobs):
            for m in range(0,machines):
                if j==0:
                    for i in range(0,m+1):
                        c_time[j][m] += table[j][i] 
                elif m==0:
                    for i in range(0,j+1):
                        c_time[j][m] += table[i][m] 
                else:
                    c_time[j][m] = max(c_time[j][m-1], c_time[j-1][m])+table[j][m]      
        return(c_time[jobs-1][machines-1])




permutation_table = list()
data_table = list()

data_table = [[ 4, 5 ],[ 4, 1 ],[ 10, 4 ],[ 6, 10 ],[ 2, 3 ]]

print(count_time(data_table))

permutation_table = permutation_and_c_time([1, 2, 3, 4 ])
print(permutation_table)



