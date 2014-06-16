from QuickUnionUF import QuickUnionUF
from QuickFindUF import QuickFindUF


class RankedQuickUnionUF(QuickUnionUF):

    def __init__(self, array, add_Redundant = True):
            super(RankedQuickUnionUF, self).__init__(array)
            self.add_redundant = add_Redundant
            self.rank = []
            self.display_rank = []
            self.max_display_rank = 0
            for index in range(0, len(array)):
                self.rank.append(0)
                self.display_rank.append(0)
            self.component = []
            for index in range(0, len(array)):
                self.component.append(index)

    def __str__(self):
        result = super(QuickFindUF,self).__str__()
        self.print_2d(self.component, "Component")
        self.print_2d(self.rank, 'Rank')

        print 'Array'
        for y in range(0, self.array.size()):
                            line = ''
                            for x in range(0, self.array.size()):
                                elem = x, y
                                index = self.array.get_index_by_coords(x, y)
                                line += str(elem) + '[' + str(index) + ']'
                            print line

        return result

    def print_2d(self, some_array, label):
        print label

        for y in range(0, self.array.size()):
                    line = ''
                    for x in range(0, self.array.size()):
                        index = self.array.get_index_by_coords(x, y)
                        line += str(some_array[index]) + ' '
                    print line
        print ''


    def union(self, p, q):
        ids_on_indexes = super(QuickFindUF, self).union(p, q)

        if ids_on_indexes != None:
            rootP, rootQ = ids_on_indexes
        else:
            return None

        if self.rank[rootP] < self.rank[rootQ]:
            self.array.set(rootP, rootQ)
            if self.display_rank[p] == self.display_rank[q]:
                self.bring_component_tree_up(rootQ)
            self.redefine_component_membership(rootP, rootQ)
        elif self.rank[rootP] > self.rank[rootQ]:
            self.array.set(rootQ, rootP)
            if self.display_rank[p] == self.display_rank[q]:
                            self.bring_component_tree_up(rootP)
            self.redefine_component_membership(rootQ, rootP)
        else:
            self.array.set(rootQ, rootP)
            self.rank[rootP] += 1
            self.bring_component_tree_up(rootP)
            self.redefine_component_membership(rootQ, rootP)



    def redefine_component_membership(self, old_root, new_root):
        for i in range(0, len(self.array)):
            if self.component[i] == old_root:
                self.component[i] = new_root

    def bring_component_tree_up(self, rootTree):
        for i in range(0, len(self.array)):
            if self.component[i] == rootTree:
                self.display_rank[i] += 1
