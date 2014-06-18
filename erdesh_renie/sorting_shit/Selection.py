from sorting_visualizing import Sort_Visualized
import random


class Selection(Sort_Visualized):

    def __init__(self, mass):
        super(Selection, self).__init__(mass)

    def sort(self):
        N = len(self.mass)

        for i in range(0, N):
            min = i
            for j in range(i+1, N):
                if self.less(j, min):
                    min = j
            self.exch(i, min)
            self.snapshot_state()



sort = Selection([i**2*random.uniform(0.0, 1.0) for i in range(100)])



