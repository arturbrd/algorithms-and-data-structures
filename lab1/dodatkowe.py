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


def swap_rows(mtrx, a):
    new_table = []
    new_table.append(mtrx[a])
    for i in range(1, mtrx.size()[0]):
        if i == a:
            new_table.append(mtrx[0])
        else:
            new_table.append(mtrx[i])

    new_table[1], new_table[2] = new_table[2], new_table[1]
    return Matrix(new_table)

def chio(mtrx):
    rows, cols = mtrx.size()
    if (rows, cols) == (2,2):
        return mtrx[0][0]*mtrx[1][1]-mtrx[1][0]*mtrx[0][1]

    if mtrx[0][0] == 0:
        for i in range(1, rows-1):
            if mtrx[i][0] != 0:
                mtrx = swap_rows(mtrx, i)
                break
        else:
            return None

    new_table = []
    for i in range(1, rows):
        new_row = []
        for j in range(1, cols):
            new_row.append(mtrx[0][0]*mtrx[i][j]-mtrx[i][0]*mtrx[0][j])
        new_table.append(new_row)
    return 1/((mtrx[0][0])**(rows-2))*chio(Matrix(new_table))

print(chio(Matrix([
    [5, 1, 1, 2, 3],
    [4, 2, 1, 7, 3],
    [2, 1, 2, 4, 7],
    [9, 1, 0, 7, 0],
    [1, 4, 7, 2, 2]
])))

print(chio(Matrix([
     [0, 1, 1, 2, 3],
     [4, 2, 1, 7, 3],
     [2, 1, 2, 4, 7],
     [9, 1, 0, 7, 0],
     [1, 4, 7, 2, 2]
])))