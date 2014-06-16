class UF(object):
    def __init__(self, array):
        self.array = array
        self.count = len(array)
        self.add_redundant = True

    def get_managed_array(self):
        return self.array

    def __str__(self):
        result =  str(self.array)
        result += "components count: " + str(self.count)
        return  result

    def union(self, p, q):
        if p < q:
            element = p, q
        else:
            element = q, p

        if self.connected(p, q):
            if self.add_redundant:
                self.array.redundant_connections.add(element)
            return None
        else:
            self.array.connections.add(element)
            pId = self.find(p)
            qId = self.find(q)
            self.count -= 1
            return pId, qId

    def find(self, p):
        pass

    def connected(self, p, q):
        return self.find(p) == self.find(q)