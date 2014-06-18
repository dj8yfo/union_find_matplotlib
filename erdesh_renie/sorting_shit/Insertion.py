from sorting_visualizing import Sort_Visualized


class Insertion(Sort_Visualized):

    def __init__(self, mass):
        super(Insertion, self).__init__(mass)

    def sort(self):
        N = len(self.mass)

        for i in range(1, N):
            j = i
            while j > 0 and self.less(j, j-1):
                self.exch(j, j-1)
                j -= 1
            self.snapshot_state()