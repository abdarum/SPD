#/usr/bin/python3

#import built-in modules

import itertools


def permutation_and_c_time(permutation_list):
    table = list() #Table consist permutations
    #Make permutations
    permutation_table = list(itertools.permutations(permutation_list)) 
    for i in range(0,len(permutation_table)):
        table.append([]) #Add empty row to table
        table[i].insert(0,0) #As first element insert 0, it will be time value
        table[i].append(permutation_table[i]) #Add permutation to row
    return table


def auto_permutation(data):
    #It makes permutation depends of number of maschines
    return(permutation_and_c_time(range(0,len(data)))) 


def count_time(table):
    #As argument it recive table with machines and jobs in fixed order
    jobs = len(table)
    if jobs>0:
        machines = len(table[0]) 
        #Create 2D martix filled 0 of size machines by jobs
        #Matrix will keep temporary count time values
        c_time = [[0] * machines for i in range(jobs)]

        for j in range(0,jobs):
            for m in range(0,machines):
                if j==0:
                    #If it is first job
                    for i in range(0,m+1):
                        c_time[j][m] += table[j][i] 
                elif m==0:
                    #If it is first machine
                    for i in range(0,j+1):
                        c_time[j][m] += table[i][m] 
                else:
                    c_time[j][m] = max(c_time[j][m-1], 
                            c_time[j-1][m])+table[j][m]      
        #Return last element of matrix(this is complete time of tasks)
        return(c_time[jobs-1][machines-1])


def combination_to_data_table(combination, data):
    #Function return matrix of jobs and machines sorted in combination order
    out_table = list()
    for c in combination:
        out_table.append(data[c])
    return out_table


def all_combination_count(table, data):
    #Function count time for each combination and automatically convert table
    # with machines and jobs
    for i in range(0,len(table)):
        table[i][0] = count_time(
                combination_to_data_table(table[i][1],data))
    #It return final table with counted time
    return(table)



def return_the_best_combination(table):
    #Function sort table by the time(lowest time is at the [0] element)
    table = sorted(table,key=lambda l:l[0])
    if len(table)>0:
        #Return min time value and permutation for it
        return(table[0][0], table[0][1])


def full_cycle_of_finding_the_best_combination(table):
    #It make all, you have to put in only table with machines and jobs
    #Recive table, return the fastest combination time and combination
    return_table = list()
    return_table = auto_permutation(table)
    return_table = all_combination_count(return_table, table)
    combination = return_the_best_combination(return_table)
    time = combination[0]
    combination = combination[1]
    print(combination_to_data_table(combination, table))
    print("Time: "+str(time)+" Combination: "+str(combination))
    return(return_the_best_combination(return_table))

def johnson_dla_2(table_import, table_3_import=list()): #johnsons algorithm for 2 machines
    table = list(table_import)
    table_3 = list(table_3_import)
    lista1 = []
    lista2 = []
    while len(table) > 0:
        min1 = 0
        min2 = 0
        for i in range(0, len(table)):
            #print(i)
            #print(table)
            if table[i][0] < table[min1][0]:
                min1 = i
            if table[i][1] < table[min2][1]:
                min2 = i
        if (table[min1][0] < table[min2][1]) | (table[min1][0] == table[min2][1]):
            if len(table_3):
                lista1.append(table_3[min1])
                del table_3[min1]
            else:
                lista1.append(table[min1])
            del table[min1]
        else:
            if len(table_3):
                lista2.insert(0, table_3[min2])
                del table_3[min2]
            else:
                lista2.insert(0, table[min2])
            del table[min2]
    return lista1+lista2

def johnson_dla_3(table): #johnsons algoritm for 3 machines
    lista3 = []
    for i in range(0, len(table)):
        suma_1_2 = table[i][0] + table[i][1]
        suma_2_3 = table[i][1] + table[i][2]
        lista3.append([suma_1_2, suma_2_3])
        #print(suma_1_2)
        #print(suma_2_3)
    return johnson_dla_2(lista3, table)



#       main
permutation_table = list()
data_table = list()


#Combination of data to test, second is in PDF
data_table = [[ 4, 5, 3],[ 4, 1, 2 ],[ 10, 4, 5 ],[ 6, 10, 1 ],[ 2, 3, 2 ]]
#data_table = [[ 4, 5 ],[ 4, 1 ],[ 10, 4 ],[ 6, 10 ],[ 2, 3 ]]
#Print table with data
print(data_table)

#Display time for this configuration
print(count_time(data_table))

#Test
#print(combination_to_data_table((4,1,2,3,0), data_table))

permutation_table  = auto_permutation(data_table)
print(permutation_table)

print("\n\n\n\n")

print(all_combination_count(permutation_table, data_table))

print("\n\n\n\n")

print(return_the_best_combination(permutation_table))

print("\n\n\n Johnson\n\n\n")
#print(johnson_dla_2(data_table))
#print(count_time(johnson_dla_2(data_table)))
print(johnson_dla_3(data_table))
print(count_time(johnson_dla_3(data_table)))

print("\n\n\n")


print("\ntest of one function\n")
full_cycle_of_finding_the_best_combination(data_table)
#sprawdzenie
