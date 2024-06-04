import time

def search(S, W):
    m = 0
    indexes = []
    comp = 0
    while m <= len(S)-len(W):
        i = 0
        while i < len(W):
            comp += 1
            if S[m+i] != W[i]:
                break
            i += 1
        else:
            indexes.append(m)
        m += 1
    return indexes, comp

def RabinKarp(S, W):
    M = len(S)
    N = len(W)
    hW = hash(W)
    indexes = []
    comp = 0
    col = 0
    for m in range(M-N+1):
        hS = hash(S[m:m+N])
        comp += 1
        if hS == hW:
            for i in range(N):
                comp += 1
                if S[m+i] != W[i]:
                    col += 1
                    break
            else:
                indexes.append(m)
    return indexes, comp, col

def RabinKarpRolling(S, W):
    M = len(S)
    N = len(W)
    hW = hash(W)
    indexes = []
    comp = 0
    col = 0
    h = 1
    for i in range(N-1):  # N - jak wyżej - długość wzorca
        h = (h*256) % 101  

    hS = hash(S[:N])
    comp += 1
    if hS == hW:
        for i in range(N):
            comp += 1
            if S[m+i] != W[i]:
                col += 1
                break
        else:
            indexes.append(m)
    for m in range(1, M-N+1):
        hS = (256*(hS - ord(S[m-1])*h) + ord(S[m+N-1])) % 101
        comp += 1
        if hS == hW:
            for i in range(N):
                comp += 1
                if S[m+i] != W[i]:
                    col += 1
                    break
            else:
                indexes.append(m)
    return indexes, comp, col

def hash(word):
    hw = 0
    for i in range(len(word)):
        hw = (hw*256 + ord(word[i])) % 101
    return hw

def main():
    with open("lab12/lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ''.join(text).lower()

    W = "time."

    t_start = time.perf_counter()

    indexes, comp = search(S, W)

    t_stop = time.perf_counter()

    print(len(indexes), "; ", comp, sep="")

    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()

    indexes, comp, col = RabinKarp(S, W)

    t_stop = time.perf_counter()

    print(len(indexes), "; ", comp, "; ", col, sep="")

    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()

    indexes, comp, col = RabinKarpRolling(S, W)

    t_stop = time.perf_counter()

    print(len(indexes), "; ", comp, "; ", col, sep="")

    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


if __name__ == "__main__":
    main()