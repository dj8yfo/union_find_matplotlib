from UF import UF
class QuickFindUF(UF):

    def __init__(self, array):
        super(QuickFindUF, self).__init__(array)
        for index in range(0, len(self.array)):
            self.array.set(index, index)

    def find(self, p):
        return self.array.get(p)

    def union(self, p, q):
        ids_on_indexes = super(QuickFindUF, self).union(p, q)
        if ids_on_indexes != None:
            p_id, q_id = ids_on_indexes
        else:
            return None


        for i in range(0, len(self.array)):
            if self.array.get(i) == p_id:
                self.array.set(i, q_id)

        return p_id, q_id