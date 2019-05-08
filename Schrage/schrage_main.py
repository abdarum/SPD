#!/usr/bin/env python3
import schrage

if __name__ == '__main__':
    shr = schrage.Schrage()
    shr.load_file("in100.txt")
    shr.show_sequence()
    print("\n\n\n")
    shr.sort()
    shr.show_sequence()
