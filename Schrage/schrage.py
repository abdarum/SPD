#!/usr/bin/env python3

import task


class Schrage:
    def __init__(self):
        self.c_max = 0
        self.t = 0 #time
        self.new_task = task.Task()
        self.current_task = task.Task()
        self.l_not_ready_tasks = list()
        self.l_ready_tasks = list()
        self.sequence = list()
        self.n = 0

    def schrage_s(self): #standard shrage
        pass

    def schrage_ptmn(self): #shrage z przerwaniami
        pass

    def sort(self):
        tmp_task = task.Task()
        n = self.n
        while(n):
            n -= 1
            for i in range(0, n):
                if self.sequence[i].r > self.sequence[i+1].r:
                    self.sequence[i+1], self.sequence[i] = \
                            self.sequence[i], self.sequence[i+1] 

    def load_file(self, file_path):
        f = open(file_path, 'r')
        number_of_tasks = f.readline()
        while True:
            if number_of_tasks != "\n":
                break
            number_of_tasks = f.readline()
        number_of_tasks = number_of_tasks.rstrip("\n\r")
        number_of_tasks = number_of_tasks.split()
        number_of_tasks = int(number_of_tasks[0])

        self.n = number_of_tasks

        if number_of_tasks > 0:
            table = list()
            for i in range(0,number_of_tasks):
                line = f.readline()
                if line == "":
                    break
                line = line.rstrip("\n\r")
                line = line.split()
                tmp_task = task.Task(i, int(line[0]), int(line[1]), int(line[2]))
                self.sequence.append(tmp_task)
        f.close()

    def show_sequence(self):
        for i in self.sequence:
            i.print_task()

