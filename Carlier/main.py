#!/usr/bin/env python3
from carlier import *



#"in50.txt", "in100.txt", "in200.txt", "data1.txt" 
#"data2.txt", "data3.txt", "data4.txt", "data5.txt", "data6.txt"


if __name__ == '__main__':
    #filename = "in50.txt"
    #filename = "in100.txt"
    #filename = "in200.txt"
    #filename = "data1.txt"
    filename = "data4.txt"
    input_single_file = load_from_file(filename)
    print("Input file: ",filename)

    '''
    c_max, O = schrage(input_single_file)
    print("c_max schrage = ", c_max)
    c_max, O= schrage_pmtn(input_single_file)
    print("c_max schrage_pmtn = ", c_max)
    '''
    c_max = carlier(input_single_file)
    print("c_max carlier = ", c_max)




