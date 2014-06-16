
from random import randint as get_it

def shuffle_array(array):
    result = []
    shuffled_indices = []
    indices = range(0, len(array))
    while len(indices) > 0:
        permuted_index = get_it(0, len(indices) - 1)
        shuffled_indices.append(indices[permuted_index])
        del indices[permuted_index]

    for index in shuffled_indices:
        result.append(array[index])

    return result

class RandomConnectionBag(object):

    def __init__(self, n_elements, union_to_work_with = None):
        self.n_elements = n_elements
        self.set_of_provided = set([])
        self.next = 0,1
        self.union_to_work_with = union_to_work_with

        if self.union_to_work_with != None:
            self.start_element_index = n_elements/2
            self.radius = 1

        # print "ordered connections size: " + str(len(self.ordered_connections))
        # print ordered_connections

        # print self.random_order_connections
    def __len__(self):
        return self.n_elements*(self.n_elements-1)/2 - len(self.set_of_provided)

    def has_next(self):
        if self.__len__() > 0:
            return True
        else:
            return False

    def get_next_spiraled(self):
        from_element = self.start_element_index
        y_f, x_f = self.union_to_work_with.array.index_map(from_element)

        search = True
        to_element = None
        for radius in range(1, self.union_to_work_with.array.size()):
            if not search:
                break
            candidates_for_radius = []
            growing_radius = []
            for i in range(1, radius+1):
                for x_dif in range(-i, i+1):
                    for y_dif in range(-i, i+1):
                        to_element = None
                        y_s_candidate =  y_f + y_dif
                        x_s_candidate =  x_f + x_dif
                        try:
                            to_element = self.union_to_work_with.array.get_index_by_coords(x_s_candidate, y_s_candidate)
                        except:
                            to_element = None
                            continue
                        candidates_for_radius.append(to_element)
            next_candidate = None
            while len(candidates_for_radius) > 0:
                rand_index = get_it(0, len(candidates_for_radius) - 1)
                next_candidate =  candidates_for_radius[rand_index]
                if self.union_to_work_with.connected(from_element, next_candidate):
                    next_candidate =  None
                    del candidates_for_radius[rand_index]
                else:
                    break

            if next_candidate != None:
                search = False
                to_element = next_candidate

        if to_element != None:
            result = from_element, to_element
            self.start_element_index = to_element
        else:
            result =  0, 1
        return result






    def get_next_ordered(self):
        result = self.next
        x, y = result
        x = (x+1)%self.n_elements
        y = (y+1)%self.n_elements

        self.next = x,y
        return result

    def get_next(self):
        if self.__len__() > 0:
            x = get_it(0, self.n_elements -2)
            y = get_it(x+1, self.n_elements -1)
            while (x,y) in self.set_of_provided:
                x = get_it(0, self.n_elements - 2)
                y = get_it(x+1, self.n_elements -1)
            element = x, y
            self.set_of_provided.add(element)
            # print self.set_of_provided
            return element
        else:
            return None

# array = range(0, 21)

# print array
# print shuffle_array(array)

# bag = RandomConnectionBag(100)
# while bag.has_next():
#     print bag.get_next()
#
#
# print len(bag.set_of_provided)


