class Matrix:

    # consumes a length (m) list of length (n) list of integers, and make it into a m*n matrix
    def __init__(self, list_of_list):
        self._data = list_of_list
        self._row = len(list_of_list)
        self._col = len(list_of_list[0])
    
    ## returns the value of the i,j th entry of the matrix
    def entry(self, row, col):
        return self._data[row - 1][col - 1]
    
    ## col_join consumes another matrix mat2, and concatenate it to self to obtain a new matrix
    ## req: the two matrices need to have the same number of rows (m)
    def col_join(self, mat2, dir):
        m_2 = len(mat2)
        new_mat = [0]*m_2
        if self._row != m_2:
            return "invalid matrices dimensions"
        if dir == "right":
            for i in range(m_2):
                new_mat[i] = self._data[i] + mat2[i]
        else:
            for i in range(m_2):
                new_mat[i] = mat2[i] + self._data[i]
        return Matrix(new_mat)

    ## product consumes a vector of length n, returns the matrix calculation Av correspondingly
    ## consumes a vector (list of n elements of numbers)
    def product(self, vector):
        result = [None] * self._row
        for i in range(self._row):
            sum = 0
            for j in range(self._col):
                sum = sum + self._data[i][j]*vector[j]
            result[i] = sum
        return result

    ## row_prod consumes a vector of length m element, returns sum of applying the vector scalar
    ## product with each row and sum them up.
    def row_prod(self, vector):
        result = [None]*self._col
        for i in range(self._row):
            for j in range(self._col):
                result[j] = result[j] + self._data[i][j]*vector[i]
        return result
            
