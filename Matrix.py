

def dot( vec1, vec2 ):
    '''This method returns the dot product of two vectors'''
    if len(vec1)== len(vec2):
        return [[sum(a * b for a, b in zip(vec1_row, vec2_col)) for vec2_col in zip(*vec2)] for vec1_row in vec1]
    else:
        return

class Matrix():
    ## Initialize a Matrix object with an input matrix, stored as a list-of-lists.
    def __init__( self, matrix ):
        self.matrix= [[matrix[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]


    def get_row( self):
        '''this methds return  list of the rows of the self'''
        result=[]
        for i in range(len(self.matrix)):
            result.append(i)
        return result

    def get_col( self):
        '''this method return the list of the columns of the matrices'''
        result=[]
        for j in range(len(self.matrix[0])):
            result.append(j)
        return result


    def add( self, other ):
        '''this method adds two matrices together'''
        result = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
        for i in range(len(self.get_row())):
            for j in range(len(self.get_col())):
                if type(other)==list:
                    result[i][j]= self.matrix[i][j]+ other[i][j]
                else:
                    result= [[self.matrix[i][j]+other for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]

        return result


    def sub( self, other ):
        '''this method returns the self - other '''
        result = [[0,0,0],
                [0,0,0],   #---initial the dimensions of the result matrix
                [0,0,0]]
        for i in range(len(self.get_row())):
            for j in range(len(self.get_col())):
                if type(other)==list:
                    result[i][j]= self.matrix[i][j]-other[i][j]
                else:
                    result= [[self.matrix[i][j]-other for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
        return result

    def mult( self, other ):
        '''this method return the product of self times other'''
        if type(other)!=list: # this checks whether other is scalar or list
            matrix= [[self.matrix[i][j]*other for j in range(len(self.matrix[i]))] for i in range(len(self.matrix))]
            return matrix
        else:
            return dot(self.matrix, other)

    def transpose( self ):
        '''this methods transpose the matrix, rows become cols and cols become rows'''
        result = [[self.matrix[j][i] for j in range(len(self.get_row()))] for i in range(len(self.get_col()))]
        return result




self = [[1,2,3],
        [4 ,5,6],
        [7 ,8,9]]
# transpost-->[[1,4,7],
#              [2,5,8],
#              [3,6,9]]
# other=4
other=[[9,8,7],
        [6,5,4],
        [3,2,1]]

mat= Matrix(self)
# print('\n')
print("multiplications:\n ", mat.mult(other))
print("\n")
print("addition: \n ", mat.add(other))
print("\n")
print("substractions: \n ", mat.sub(other))
print("\n")
print("col index: \n", mat.get_row())
print("\n")
print("row indx: \n", mat.get_row())
print("\n")
print("transpose: \n", mat.transpose())
