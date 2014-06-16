from QuickFindUF import QuickFindUF


class QuickUnionUF(QuickFindUF):

    def __init__(self, array):
        super(QuickUnionUF, self).__init__(array)


    def find(self, p):
        while p != self.array.get(p):
            p = self.array.get(p)
        return p

    def union(self, p, q):
        ids_on_indexes = super(QuickFindUF, self).union(p, q)
        if ids_on_indexes != None:
            p_id, q_id = ids_on_indexes
        else:
            return None

        self.array.set(p_id, q_id)
        return p_id, q_id

