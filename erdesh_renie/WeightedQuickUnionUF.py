
from QuickUnionUF import QuickUnionUF
from QuickFindUF import QuickFindUF

class WeightedQuickUnionUF(QuickUnionUF):

    def __init__(self, array):
        super(WeightedQuickUnionUF, self).__init__(array)
        self.sz = []
        for index in range(0, len(array)):
            self.sz.append(1)


    def union(self, p, q):
        ids_on_indexes = super(QuickFindUF, self).union(p, q)
        if ids_on_indexes != None:
            rootP, rootQ = ids_on_indexes
        else:
            return None

        less_subtree_root_index = -1
        greater_subtree_root_index = -1
        if self.sz[rootP] < self.sz[rootQ]:
            less_subtree_root_index = rootP
            greater_subtree_root_index = rootQ
        else:
            less_subtree_root_index = rootQ
            greater_subtree_root_index = rootP

        self.array.set(less_subtree_root_index, greater_subtree_root_index)
        self.sz[greater_subtree_root_index] += self.sz[less_subtree_root_index]
        return rootP, rootQ
        # print self.sz



