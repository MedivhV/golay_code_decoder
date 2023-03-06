class Binary:

    ## consumes a vector of normal digits, convert them into binary form
    def __init__(self, vector):
        self._length = len(vector)
        self._data = []
        for i in range (self._length):
            self._data = self._data + [vector[i] % 2]
    
    ##returns the value of the binary number
    def value(self):
        return self._data

    ## returns the weight of the binary vector
    def weight(self):
        w = 0
        for i in range(self._length):
            if self._data[i] == 1:
                w += 1
        return w

    ## sub consumes another vector of the same dimension and subtracts it to _data according 
    ## to binary rules
    def sub(self, v1, v2):
        n = len(v1)
        new = Binary([0]*n)
        if n != len(v2):
            return "invalid dimension"
        for i in range(n):
            n1 = v1[i]
            n2 = v2[i]
            if n1 - n2 == -1:
                new._data[i] = 1
            else:
                new._data[i] = n1 - n2
        return new
    
    ## diff consumes a vector, records the position of the vector of difference
    def diff(self, vector):
        count = 0
        pos = []
        for i in range(self._length):
            if self._data[i] != vector[i]:
                count += 1
                pos = pos + [i]
        return [count, pos]