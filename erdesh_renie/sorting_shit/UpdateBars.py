import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.container import BarContainer

class BarUpdate(object):

    def __init__(self, ax, representations):
        self.representations = representations
        self.ax = ax

        first_repro = self.representations[0]
        self.bars = ax.bar(range(0, len(first_repro.visual_y)), first_repro.visual_y,color = 'g')
        print self.bars.get_children()


    def set_state(self, repre):
        list_inner = self.bars.get_children()

        for x_index in range(0, len(repre.visual_y)):
            list_inner[x_index].set_height(repre.visual_y[x_index])

        affected_by_perm_x = repre.affected_indexes
        not_affected_by_perm_x = [i for i in range(0, len(repre.visual_y)) if i not in repre.affected_indexes]

        green = (0.0, 0.5, 0.0, 1.0)
        light_green = (0.0, 0.5, 0.0, 0.5)
        for x_index in affected_by_perm_x:
            list_inner[x_index].set_facecolor(light_green)
        for x_index in not_affected_by_perm_x:
            list_inner[x_index].set_facecolor(green)


    def init(self):
        self.set_state(self.representations[0])
        return self.bars

    def __call__(self, i):
        self.ax.cla()
        effective_index = i%len(self.representations)
        self.set_state(self.representations[effective_index])
        return self.bars















