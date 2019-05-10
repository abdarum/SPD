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

    def clear(self):
        self.__init__()

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
        #t = 0 #time
        #t = self.sequence[0].r #i would like to remove it
        idx = Schrage.get_idx_of_min_task(l_not_ready_tasks, 'r')
        t = l_not_ready_tasks[idx].r
        new_task = task.Task(0,0,0,1000000000)
        current_task = task.Task()

        while(len(l_not_ready_tasks) or len(l_ready_tasks)):
            while(len(l_not_ready_tasks) != 0 and \
                    l_not_ready_tasks[Schrage.get_idx_of_min_task(l_not_ready_tasks, 'r')].r <= t):
                idx = Schrage.get_idx_of_min_task(l_not_ready_tasks, 'r')
                current_task = copy.deepcopy(l_not_ready_tasks[idx])
                l_ready_tasks.append(current_task)
                del l_not_ready_tasks[idx]
                if (current_task.q > new_task.q):
                    new_task.p  = t - current_task.r
                    t = current_task.r
                    if new_task.p > 0:
                        l_ready_tasks.append(current_task)

            if len(l_ready_tasks) == 0:
                idx = Schrage.get_idx_of_min_task(l_not_ready_tasks, 'r')
                t = l_not_ready_tasks[idx].r
            else:
                idx = Schrage.get_idx_of_max_task(l_ready_tasks, 'q')
                current_task = copy.deepcopy(l_ready_tasks[idx])
                del l_ready_tasks[idx]
                new_task = copy.deepcopy(current_task)
                t += current_task.p
                self.c_max = max(self.c_max, t + current_task.q)
        return self.c_max

    @staticmethod
    def get_idx_of_min_task(list_of_tasks, parameter):
        assert isinstance(list_of_tasks, list), "list_of_tasks must be list"
        min_idx = None
        for i in range(0,len(list_of_tasks)):
            if parameter == 'r':
                if min_idx == None or\
                        list_of_tasks[i].r < list_of_tasks[min_idx].r:
                    min_idx = i
            elif parameter == 'p':
                if min_idx == None or\
                        list_of_tasks[i].p < list_of_tasks[min_idx].p:
                    min_idx = i
            elif parameter == 'q':
                if min_idx == None or\
                        list_of_tasks[i].q < list_of_tasks[min_idx].q:
                    min_idx = i
            else:
                return None
        return min_idx

    @staticmethod
    def get_idx_of_max_task(list_of_tasks, parameter):
        assert isinstance(list_of_tasks, list), "list_of_tasks must be list"
        max_idx = None
        for i in range(0,len(list_of_tasks)):
            if parameter == 'r':
                if max_idx == None or\
                        list_of_tasks[i].r > list_of_tasks[max_idx].r:
                    max_idx = i
            elif parameter == 'p':
                if max_idx == None or\
                        list_of_tasks[i].p > list_of_tasks[max_idx].p:
                    max_idx = i
            elif parameter == 'q':
                if max_idx == None or\
                        list_of_tasks[i].q > list_of_tasks[max_idx].q:
                    max_idx = i
            else:
                return None
        return max_idx

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

