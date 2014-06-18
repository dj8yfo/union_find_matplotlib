from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from Grid import Grid

class GraphicGrid(object):
    colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    colours_redundant = [el + '--' for el in colours]

    def __init__(self, grid=None, union_find = None, **kwargs):
        self.grid = grid
        if grid != None:
            self.info = grid.State_info(grid, union_find)
        if kwargs.has_key('representations'):
            self.representations = kwargs['representations']
        if kwargs.has_key('zlim'):
            self.zlim = kwargs['zlim']
        else:
            self.zlim = None


    def update_frame(self, framedata, patches, lines, redundant_lines,  axes):
        result = self.update_figures(self.representations[framedata], patches, lines, redundant_lines, axes)
        return result


    def update_figures(self, representation, patches, lines, redundant_lines,  helper_axes):
        xes = [-1]*(representation.dimension**2)
        yes = [-1]*(representation.dimension**2)
        zes = [0]*(representation.dimension**2)
        if len(representation.z_s) > 0:
            zes = representation.z_s

        c = [0]*(representation.dimension**2)

        if len(representation.colours) > 0:
            c = representation.colours

        for index in range(0, representation.dimension ** 2):
                    y, x = self.grid.index_map(index)
                    xes[index] = x
                    yes[index] = y

        helper_axes.cla()
        helper_axes.grid(False)
        if self.zlim != None:
            helper_axes.set_zlim3d([0.0, self.zlim])
        patches = helper_axes.scatter(xes, yes, zes, c=c, s=2.8)

        lines = []
        for connection in representation.connections:
                    points = list(connection)

                    x_f, y_f =  points[0]
                    x_s, y_s = points[1]

                    zf_index, zs_index = self.grid.get_index_by_coords(x_f, y_f), self.grid.get_index_by_coords(x_s, y_s)
                    z_f = zes[zf_index]
                    z_s = zes[zs_index]
                    component_num = c[zf_index]
                    colour = GraphicGrid.colours[component_num%len(GraphicGrid.colours)]
                    lines.append(helper_axes.plot([x_f, x_s], [y_f, y_s], [z_f, z_s], colour, linewidth=0.55))

        redundant_lines = []
        for connection in representation.redundant_connections:
                    points = list(connection)

                    x_f, y_f =  points[0]
                    x_s, y_s = points[1]

                    zf_index, zs_index = self.grid.get_index_by_coords(x_f, y_f), self.grid.get_index_by_coords(x_s, y_s)
                    z_f = zes[zf_index]
                    z_s = zes[zs_index]
                    component_num = c[zf_index]
                    colour = GraphicGrid.colours_redundant[component_num%len(GraphicGrid.colours_redundant)]
                    redundant_lines.append(helper_axes.plot([x_f, x_s], [y_f, y_s], [z_f, z_s], colour, linewidth=0.55))
        return patches, lines, redundant_lines


    def drawGrid_alt(self):
        representation = self.info.get_represantation()
        fig = plt.figure(figsize=(16,9), dpi=200)
        ax = plt.axes(projection='3d')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('3D Test')
        patches = ax.scatter(0, 0, 0)
        lines = ax.plot([0, 1], [0, 1], [0, 1], linewidth=0.55)
        redundant = ax.plot([0, 1], [0, 1], [0, 1], linewidth=0.55)
        self.update_figures(representation, patches, lines, redundant, ax)

        plt.show()

gridishe = GraphicGrid(Grid(5), representations=[])






# grid = Grid(5)
# element = 1, 6
# grid.connections.add(element)
# element = 1, 7
# grid.connections.add(element)
# element = 6, 7
# grid.redundant_connections.add(element)
#
# graphical =  GraphicGrid(grid)
# graphical.drawGrid()


