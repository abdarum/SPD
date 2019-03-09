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


def auto_permutation(data):
    return(permutation_and_c_time(range(0,len(data))))


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
                    c_time[j][m] = max(c_time[j][m-1], 
                            c_time[j-1][m])+table[j][m]      
        return(c_time[jobs-1][machines-1])


def combination_to_data_table(combination, data):
    out_table = list()
    for c in combination:
        out_table.append(data[c])
    return out_table


def all_combination_count(table, data):
    for i in range(0,len(table)):
        table[i][0] = count_time(
                combination_to_data_table(table[i][1],data))
    return(table)


def return_the_best_combination(table):
    table = sorted(table,key=lambda l:l[0])
    if len(table)>0:
        return(table[0][0], table[0][1])





#       main
permutation_table = list()
data_table = list()

data_table = [[ 4, 5, 3],[ 4, 1, 2 ],[ 10, 4, 5 ],[ 6, 10, 1 ],[ 2, 3, 2 ]]
#data_table = [[ 4, 5 ],[ 4, 1 ],[ 10, 4 ],[ 6, 10 ],[ 2, 3 ]]
print(data_table)

print(count_time(data_table))

print(combination_to_data_table((4,1,2,3,0), data_table))



#permutation_table = permutation_and_c_time([0,1, 2])
permutation_table  = auto_permutation(data_table)
print(permutation_table)

print("\n\n\n\n")

print(all_combination_count(permutation_table, data_table))

print("\n\n\n\n")

print(return_the_best_combination(permutation_table))
