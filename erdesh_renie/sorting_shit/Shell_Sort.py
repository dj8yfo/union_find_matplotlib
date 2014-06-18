from sorting_visualizing import Sort_Visualized

class Shell_Sort(Sort_Visualized):

    def __init__(self, mass):
        super(Shell_Sort, self).__init__(mass)

    def sort(self):
        N = len(self.mass)
        h = 1
        while h < N/3:
            h = 3*h + 1

        while h >=1:
            for i in range(h, N):
                j = i
                while j >= h and self.less(j, j-h):
                    self.exch(j, j-h)
                    j -=h
                self.snapshot_state(False)
            h =  h/3
            self.snapshot_state()


