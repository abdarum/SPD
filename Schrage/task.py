#!/usr/bin/env python3

class Task:
    def __init__(self, nr=0, r=0, p=0, q=0):
        self.nr = nr
        self.r = r
        self.p = p
        self.q = q
    
    def print_task(self):
        #print("Task: "+str(self.nr)+"\t R: "+str(self.r)+\
        #        "\t P: "+str(self.p)+"\t Q: "+str(self.q))
        print(' Task: {:5d} | R: {:6d} | P: {:6d} | Q: {:6d}|').format(\
            self.nr, self.r, self.p, self.q)
