#!/usr/bin/env python3

import task
import copy


class Schrage:
    def __init__(self):
        self.c_max = 0
        self.t = 0 #time
        self.new_task = task.Task()
        self.sequence = list()
        self.n = 0

    def schrage_s(self): #standard shrage
        self.sort()
        t = self.sequence[0].r
        self.c_max = 0
        i = 0
        l_ready_tasks = list()
        l_not_ready_tasks = copy.deepcopy(self.sequence)

        while(len(l_not_ready_tasks) or len(l_ready_tasks)):
            while(len(l_not_ready_tasks) and \
                    l_not_ready_tasks[0].r <= t):
                tmp_task = l_not_ready_tasks[0]
                l_ready_tasks.append(tmp_task)
                del l_not_ready_tasks[0]
            if len(l_ready_tasks) == 0:
                t = l_not_ready_tasks[0].r
            else:
                tmp_max_q = 0
                it = 0
                for k in range(0, len(l_ready_tasks)):
                    if (l_ready_tasks[k].q > tmp_max_q):
                        tmp_max_q = l_ready_tasks[k].q
                        it = k

                tmp_task = l_ready_tasks[it]
                self.sequence[i] = tmp_task
                del l_ready_tasks[it]
                t += self.sequence[i].p

                self.c_max = max(self.c_max, t + self.sequence[i].q);

                i += 1

        self.show_sequence()
                




    def schrage_ptmn(self): #shrage z przerwaniami
        self.sort()
        self.c_max = 0
        l_ready_tasks = list()
        l_not_ready_tasks = list(self.sequence)
        t = 0 #time
        t = self.sequence[0].r #i would like to remove it
        new_task = task.Task(0,0,0,1000000000)
        current_task = task.Task()

        while(len(l_not_ready_tasks) or len(l_ready_tasks)):
            while(len(l_not_ready_tasks) != 0 and l_not_ready_tasks[0].r <= t):
                current_task = l_not_ready_tasks[0]
                l_ready_tasks.append(current_task)
                del l_not_ready_tasks[0]
                if (current_task.q > new_task.q):
                    new_task.p  = t - current_task.r
                    t = current_task.r
                    if new_task.p > 0:
                        l_ready_tasks.append(current_task)

            if len(l_ready_tasks) == 0:
                t = l_not_ready_tasks[0].r
            else:
                tmp_max_q = 0
                it = 0
                for k in range(0, len(l_ready_tasks)):
                    if (l_ready_tasks[k].q > tmp_max_q):
                        tmp_max_q = l_ready_tasks[k].q
                        it = k

                current_task = l_ready_tasks[it]
                del l_ready_tasks[it]
                new_task = current_task
                t += current_task.p
                self.c_max = max(self.c_max, t + current_task.q)
        return self.c_max



    def sort(self):
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

