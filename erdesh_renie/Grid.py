from random import randint
import RankedQuickUnionUF





class Grid(object):

    class State_info(object):
            def __init__(self, grid_object, union_find = None):
                self.outer =  grid_object
                self.dimension = grid_object.size()
                self.connections = set([])
                self.redundant_connections = set([])
                self.colours = []
                self.z_s = []
                self.union_find = union_find
                self.max_display_rank = 0

            def __str__(self):
                result = ''
                result += str(self.outer) + '\n'
                result += str(self.dimension) + '\n'
                result += str(self.connections) + '\n'
                result += str(self.redundant_connections) + '\n'
                result += str(self.colours) + '\n'
                result += str(self.z_s) + '\n'
                return result

            def get_represantation(self, get_max_rank=False):
                self.colours = []

                self.z_s = []
                if self.union_find != None and type(self.union_find) == RankedQuickUnionUF.RankedQuickUnionUF:
                    for i in range(0, self.dimension**2):
                        self.z_s.append(self.union_find.display_rank[i])

                    for i in range(0, self.dimension**2):
                        self.colours.append(self.union_find.component[i])

                    if get_max_rank:
                        for i in range(0, self.dimension**2):
                            if self.union_find.display_rank[i] > self.max_display_rank:
                                self.max_display_rank = self.union_find.display_rank[i]

                # print self.z_s

                connection_types_links = {'connections':[self.outer.connections, self.connections], 'redundant_conn':[self.outer.redundant_connections, self.redundant_connections]}
                for key in connection_types_links:
                    connection_types_links[key][1].clear()
                    for first_elem, second_element in connection_types_links[key][0]:
                        y_f, x_f = self.outer.index_map(first_elem)
                        y_s, x_s = self.outer.index_map(second_element)
                        first_added = x_f, y_f
                        second_added = x_s, y_s
                        set_element = first_added, second_added
                        connection_types_links[key][1].add(set_element)
                return self

    def __init__(self, N):
            self.grid = []

            for i_row in range(0, N):
                row = []
                for i_col in range(0, N):
                    # row.append(randint(1, N))
                    row.append(0)
                self.grid.append(row)
            self.connections = set([])
            self.redundant_connections = set([])

    def index_map(self, index):
        size = len(self.grid)
        if index < 0 or index >=size**2:
            raise "Index out of grid scope:" , index
        actual_row = index / size
        actual_col = index % size
        return actual_row, actual_col

    def get_index_by_coords(self, x, y):
        size = len(self.grid)
        if x < 0 or x >= size or y < 0 or y >=size:
            raise 'inputs x, y - [%d, %d]' % (x, y)
        index = size * y + x
        if index < 0 or index >= size**2:
            raise 'Index [%d] out of range [0, %d] for inputs x, y - [%d, %d]' % (index, size**2 -1, x, y)
        return index

    def get(self, index):
        i, j = self.index_map(index)
        return self.grid[i][j]

    def set(self, index, value):
        i, j = self.index_map(index)
        self.grid[i][j] = value

    def size(self):
        return len(self.grid)

    def  __str__(self):
        result = ''
        for i in range(0, len(self.grid)):
            result = result + "%60s" % str(self.grid[i]) + '\n'
        # print self.connections
        # print self.redundant_connections
        result += 'connections number:' + str(len(self.connections))
        result += '\nredundant connections number:' + str(len(self.redundant_connections) - len(self.connections))
        result += '\n'
        return result

    def __len__(self):
        size = len(self.grid)
        return size**2


grid = Grid(10)

index =  grid.get_index_by_coords(3, 0)
print index






