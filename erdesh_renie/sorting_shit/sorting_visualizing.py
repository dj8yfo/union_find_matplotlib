import random

class Sort_Visualized(object):

    class Inner_State(object):

        def __init__(self, visual_mass, list_of_affected_indexes):
            self.visual_y = list(visual_mass)
            self.affected_indexes = list(list_of_affected_indexes)

        def __repr__(self):
            return '\n' + str(self.visual_y) + '\n'


    def get_representation(self):
        return self.Inner_State(self.visual_mass, self.indexes_took_part_in_iterations)


    def __init__(self, mass):
        self.representations_of_states = []
        self.mass = mass
        self.indexes_took_part_in_iterations = set([])
        func = None
        if type(self.mass[0]) is str:
            func = ord
        elif type(self.mass[0]) is float:
            func = self.element
        else:
            func = int
        self.visual_mass = [func(element) for element in self.mass]
        self.snapshot_state()

    def __str__(self):
        result = '\n'
        result += 'list of elements:' + str(self.mass) + '\n'
        result += 'list of keys corresponding to elements:' + str(self.visual_mass) + '\n'
        result += 'list of indexes affected by comparisons/permutations:' + str(self.indexes_took_part_in_iterations) + '\n'
        return result

    def element(self, element):
        return element

    def snapshot_state(self, clear_indexes=True):
        self.representations_of_states.append(self.get_representation())
        if clear_indexes:
            self.indexes_took_part_in_iterations.clear()


    def sort(self):
        pass

    def less(self, index_v, index_w):
        self.indexes_took_part_in_iterations.add(index_v)
        self.indexes_took_part_in_iterations.add(index_w)
        return self.mass[index_v] < self.mass[index_w]

    def exch_int(self, massive, i_index, j_index):
        t = massive[i_index]
        massive[i_index] = massive[j_index]
        massive[j_index] = t

    def exch(self, i_index, j_index):
        self.indexes_took_part_in_iterations.add(i_index)
        self.indexes_took_part_in_iterations.add(j_index)
        self.exch_int(self.mass, i_index, j_index)
        self.exch_int(self.visual_mass, i_index, j_index)

    def show_state(self, plt, representation):
        plt.cla()
        affected_by_perm_x = representation.affected_indexes
        affected_by_perm_y = [representation.visual_y[i] for i in affected_by_perm_x]
        bars1 = plt.bar(affected_by_perm_x, affected_by_perm_y, color = 'y')

        not_affected_by_perm_x = [i for i in range(0, len(representation.visual_y)) if i not in representation.affected_indexes]
        not_affected_by_perm_y = [representation.visual_y[i] for i in not_affected_by_perm_x]
        bars2 = plt.bar(not_affected_by_perm_x, not_affected_by_perm_y, color = 'g')
        plt.cla()
        return bars1, bars2

# sort = Sort_Visualized('java sucks long uncut dicks at coding shit')
#
# sort1 =  Sort_Visualized([i**2*random.uniform(0.0, 1.0) for i in range(15)])
# print sort, sort1




