import numpy as np

def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    swaps_n = string_compare(P, T, i-1, j-1) + int(P[i]!=T[j])
    inserts_n = string_compare(P, T, i, j-1) + 1
    deletes_n = string_compare(P, T, i-1, j) + 1

    lowest_cost = min(swaps_n, inserts_n, deletes_n)

    return lowest_cost

def string_compare_PD(P, T):
    D = np.zeros((len(P), len(T)), dtype=np.uint8)
    for i in range(len(P)):
        D[i][0] = i
    for i in range(len(T)):
        D[0][i] = i
    parent = np.full((len(P), len(T)), 'X', dtype=np.dtype('U1'))
    for i in range(1, len(P)):
        parent[i][0] = 'D'
    for i in range(1, len(T)):
        parent[0][i] = 'I'
    for i in range(1, len(P)):
        for j in range(1, len(T)):
            swaps_n = D[i-1][j-1] + int(P[i]!=T[j])
            inserts_n = D[i][j-1] + 1
            deletes_n = D[i-1][j] + 1

            lowest_cost = np.inf
            op = 'X'
            
            
            if swaps_n < lowest_cost:
                lowest_cost = swaps_n
                if (P[i]!=T[j]):
                    op = 'S'
                else:
                    op = 'M'
            if inserts_n < lowest_cost:
                lowest_cost = inserts_n
                op = 'I'
            if deletes_n < lowest_cost:
                lowest_cost = deletes_n
                op = 'D'

            parent[i][j] = op
            D[i][j] = lowest_cost

    return D[len(P)-1][len(T)-1], parent

def path(parent):
    path_string = ""
    (i, j) = parent.shape
    i -= 1
    j -= 1
    op = parent[i][j]
    while op != 'X':
        
        if op == 'M':
            i -= 1
            j -= 1
        elif op == 'S':
            i -= 1
            j -= 1
        elif op == 'D':
            i -= 1
        elif op == 'I':
            j -= 1
        path_string += op
        op = parent[i][j]

    return path_string[::-1]

def main():
    P = ' kot'

    T = ' koń'
    print(string_compare(P, T, len(P)-1, len(T)-1))
    print(string_compare_PD(P, T)[0])

    T = ' pies'
    print(string_compare(P, T, len(P)-1, len(T)-1))
    print(string_compare_PD(P, T)[0])

    P = ' biały autobus'
    T = ' czarny autokar'
    # print(string_compare(P, T, len(P)-1, len(T)-1))
    print(string_compare_PD(P, T)[0])

    P = ' thou shalt not'
    T = ' you should not'
    parent = string_compare_PD(P, T)[1]
    print(path(parent))

if __name__ == "__main__":
    main()
