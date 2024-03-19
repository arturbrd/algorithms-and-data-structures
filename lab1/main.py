class Matrix:
    def __init__(self, mtrx, val=0):
        if isinstance(mtrx, tuple):
            self.__mtrx = []
            for i in range(mtrx[0]):
                self.__mtrx.append([val for x in range(mtrx[1])])
        else:
            self.__mtrx = mtrx

    def __add__(self, other):
        if self.size() != other.size():
            return None
        
        new = []
        for si, oi in zip(self.__mtrx, other):
            inner = []
            for sj, oj in zip(si, oi):
                inner.append(sj+oj)
            new.append(inner)

        return Matrix(new)

    def __mul__(self, other):
        nrows, s_cols = self.size()
        o_rows, ncols = other.size()
        if s_cols != o_rows:
            return None

        new_table = []
        for i in range(nrows):
            new_row = []
            for j in range(ncols):
                sum = 0
                for k in range(s_cols):
                    sum += self[i][k]*other[k][j]
                new_row.append(sum)
            new_table.append(new_row)

        return Matrix(new_table)

    def __getitem__(self, i):
        return self.__mtrx[i]
    
    def __str__(self):
        mtrx_str = ""
        for i in self.__mtrx:
            line = "|"
            for j in i:
                if j >= 0:
                    line += " "
                line = line+str(j)+"  "
            line = line[:-1]
            line += "|\n"
            mtrx_str += line
        mtrx_str = mtrx_str[:-1]
        return mtrx_str

    def size(self):
        return len(self.__mtrx), len(self.__mtrx[0])

def transpose(mtrx):
    rows, cols = mtrx.size()
    new_table = []
    for i in range(cols):
        new_line = []
        for j in range(rows):
            new_line.append(mtrx[j][i])
        new_table.append(new_line)
    return Matrix(new_table)

m1 = Matrix(
[ [1, 0, 2],
  [-1, 3, 1] ]
)

print(transpose(m1), end="\n\n")

m2 = Matrix((2,3), 1)

print(m1+m2, end="\n\n")

m3 = Matrix([
    [3,1],
    [2,1],
    [1,0]
])

print(m1*m3)