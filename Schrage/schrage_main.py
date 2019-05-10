#!/usr/bin/env python3
import schrage

if __name__ == '__main__':
    filename = "in100.txt"
    shr = schrage.Schrage()
    shr.load_file(filename)
    shr.show_sequence()
    print("\n\n\n")

    shr.schrage_s()
    print("\n\n\n")
    shr.show_sequence()
    print("\n"+str(shr.c_max))
    del shr
    #shr.clear()


    shr = schrage.Schrage()
    shr.load_file(filename)
    shr.schrage_ptmn()
    print("\n\n\n")
    print("Cmax "+str(shr.c_max))
