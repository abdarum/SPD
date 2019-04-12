#/usr/bin/python3

#import built-in modules

import itertools
import time
import random
import math


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

def sortSecond(val): 
        return val[1]  

def comination_by_sum_of_time_in_machine(table):
    jobs = len(table)
    if jobs:
        machines = len(table[0])
        index_sorted = list()
        index_and_count_time = list()
        for j in range(0, jobs):
            sum_var = 0
            index_and_count_time.append(list({j}))
            for m in range(0, machines):
                sum_var += table[j][m]
            index_and_count_time[j].append(sum_var)
        index_and_count_time.sort(key = sortSecond, reverse=True)  
        #sortowanie jak u dr makuchowskiego
        for i in index_and_count_time:
            index_sorted.append(i[0])

        #print(index_and_count_time)
        return index_sorted

def combination_of_moveable_number(static_numbers, moveable_number):
    vector_of_combinations = list()
    for i in range(0,len(static_numbers)+1):
        tmp = list(static_numbers)
        tmp.insert(i, moveable_number)
        vector_of_combinations.append(tmp)
    return vector_of_combinations

def neh_function(table):
    sequence_original = comination_by_sum_of_time_in_machine(table)
    sequence = list({sequence_original[0]})

    for i in range(1, len(sequence_original)):
        tmp_sequence = list()
        tmp_sequence = combination_of_moveable_number(sequence, sequence_original[i])
        tmp_time = -1 #for the lowest time and it can not be negative
        tmp_time_idx = 0
        tmp = 0
        for k in range(0, len(sequence)+1):
            tmp = count_time(combination_to_data_table(tmp_sequence[k], table))
            if((tmp < tmp_time) or (tmp_time < 0)):
                tmp_time = tmp
                tmp_time_idx = k
            #print("\n k: "+str(k)+" tmp "+str(tmp)+" tmp_time "+str(tmp_time)+"\n")
        #print(tmp_sequence)
        #print("\n")
        sequence = tmp_sequence[tmp_time_idx]
        #print(sequence)
        #print("\n____________________________\n")
    return sequence


def random_change_sequence(sequence, number_of_change=10, percent_of_change=0):
    max_idx = len(sequence) - 1
    current_sequence = list(sequence)
    if percent_of_change > 0:
        number_of_change = int(percent_of_change*len(sequence))
    for i in range(0,number_of_change):
        rand_idx1 = random.randint(0, max_idx)
        rand_idx2 = rand_idx1
        while(rand_idx2 == rand_idx1):
            rand_idx2 = random.randint(0, max_idx)
        current_sequence[rand_idx1], current_sequence[rand_idx2] = current_sequence[rand_idx2], current_sequence[rand_idx1]
    return current_sequence

def simulated_annealing(table, start_sequence, cooling_parameter, 
		start_temperature, max_iteration_number=-1, 
                critical_temperature=0.1, insert_bool=False):
    max_idx = len(start_sequence) - 1
    current_iteration = 0
    current_temperature = start_temperature

    current_sequence = list(start_sequence)
    best_sequence = list(current_sequence)
    best_sequence_time = count_time(combination_to_data_table(best_sequence, table))
    while not (((max_iteration_number == -1) and (critical_temperature == -1)) or 
        ((current_iteration >= max_iteration_number) and (max_iteration_number > 0)) or
        ((current_temperature <= critical_temperature) and (critical_temperature > 0))):

        count_time_old = count_time(combination_to_data_table(current_sequence, table))
        #current_iteration = list(best_sequence) #nie wiem czy to jest dobrze i powinno być
        rand_idx1 = random.randint(0, max_idx)
        rand_idx2 = rand_idx1
        if insert_bool:
            #insert
            while(rand_idx2 == rand_idx1 or rand_idx2 == max_idx):
                rand_idx2 = random.randint(0, max_idx-1)
            removed_element = current_sequence.pop(rand_idx1)
            current_sequence.insert(rand_idx2, removed_element)
            #print("insert, "+str(len(current_sequence)))
        else:
            #swap
            while(rand_idx2 == rand_idx1):
                rand_idx2 = random.randint(0, max_idx)
            current_sequence[rand_idx1], current_sequence[rand_idx2] = \
                    current_sequence[rand_idx2], current_sequence[rand_idx1]
            #print("swap, "+str(len(current_sequence)))
        count_time_new = count_time(combination_to_data_table(current_sequence, table))
        probability = 0.0
        if count_time_new >= count_time_old:
            probability = math.exp((count_time_old-count_time_new)/current_temperature)
        else:
            probability = 1
            
        if probability < random.random():
            current_sequence[rand_idx1], current_sequence[rand_idx2] = current_sequence[rand_idx2], current_sequence[rand_idx1]

        current_temperature = current_temperature*cooling_parameter
        if count_time_new < best_sequence_time:
            best_sequence = list(current_sequence)
            best_sequence_time = count_time(combination_to_data_table(best_sequence, table))


        print("idx "+str(current_iteration)+" rand_1 "+str(rand_idx1)+" rand_2 "+str(rand_idx2)+"\n")
        print("probability "+str(probability)+" old_time "+str(count_time_old)+" new_time "+str(count_time_new)+" temp "+str(current_temperature)+"\n")
        current_iteration += 1
    return best_sequence


def load_data_table_from_file(file_patch):
    f = open(file_patch, 'r')
    name_of_set = f.readline()
    while True:
        if name_of_set != "\n":
            break
        name_of_set = f.readline()


    name_of_set = name_of_set.rstrip("\n\r")
    number_of_jobs =  f.readline()
    number_of_jobs = int(number_of_jobs.rstrip("\n\r"))

    if number_of_jobs > 0:
        table = list()
        for i in range(0,number_of_jobs):
            line = f.readline()
            if line == "":
                break
            line = line.rstrip("\n\r")
            line = line.split(" ")
            line = [int(i) for i in line] 
            table.append(line)
    f.close()

    return table


'''
porównanie jonsona dla 3 maszyn o  różnej liczbie zadan 20 do 200 z neh

spd - qnech - makuchowski akceleracja
tablica zakończeń już jest ok
poszukać w linkach(do jego pdf) akceleracjii
porównać wersje przed akceleracji i po i wykres

4 modyfikacja najłatwiejsza
'''

#       main
permutation_table = list()
data_table = list()


#Combination of data to test, second is in PDF
#data_table = [[ 4, 5, 3],[ 4, 1, 2 ],[ 10, 4, 5 ],[ 6, 10, 1 ],[ 2, 3, 2 ]]
#data_table = [[ 4, 5 ],[ 4, 1 ],[ 10, 4 ],[ 6, 10 ],[ 2, 3 ]]
#data_table = [ [ 4, 1, 4],[ 4, 3, 3 ],[ 1, 2, 3],[ 5, 1, 3] ]

'''
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

print(combination_of_moveable_number(list({3,2,5}),1))


print("\n\n\n")

print(neh_function(data_table))

print(load_data_table_from_file("dane_tmp"))
'''

data_table = load_data_table_from_file("danedla200")

'''
jonson_table = list()
jonson_table_time = 0
neh_table = list()
neh_table_time = 0
start_time = time.time()
jonson_table = johnson_dla_3(data_table)
elapsed_time = time.time() - start_time
jonson_table_time = count_time(jonson_table)
print("Jonson combination: ")
print(jonson_table)
print("\nJonson optimum time: "+str(jonson_table_time)+"\t computing time:"+str(elapsed_time)+"\n")
'''

start_time = time.time()
#neh_table = combination_to_data_table(list({0,1,2,3,4,5,6,7}), data_table)
neh_table = combination_to_data_table(neh_function(data_table), data_table)
elapsed_time = time.time() - start_time
neh_table_time = count_time(neh_table)
print("NEH combination: ")
print(neh_table)
print("\nNEH optimum time: "+str(neh_table_time)+"\t computing time:"+str(elapsed_time)+"\n")

neh_sequence = neh_function(data_table)
changed_sequence = random_change_sequence(sequence=neh_sequence, percent_of_change=0.1)
neh_seq_time = count_time(combination_to_data_table(neh_sequence, data_table))
changed_seq_time = count_time(combination_to_data_table(changed_sequence, data_table))

start_time = 0
elapsed_time = 0

start_time = time.time()
after_annealing_seq = simulated_annealing(data_table, changed_sequence, 
        cooling_parameter=0.99, start_temperature=1000, max_iteration_number=1000, 
        critical_temperature=0.1, insert_bool=True)
elapsed_time = time.time() - start_time
after_annealing_seq_time = count_time(combination_to_data_table(after_annealing_seq, data_table))


print("neh time "+str(neh_seq_time)+" changed sequence time "+str(changed_seq_time)+" after annealing "+str(after_annealing_seq_time)+"\t computing time:"+str(elapsed_time)+"\n")


#print(simulated_annealing(data_table, neh_function(data_table), 0.95, 500, 50))
#print(count_time(combination_to_data_table(
#    simulated_annealing(data_table, neh_function(data_table), 0.95, 500, 50), data_table)))



