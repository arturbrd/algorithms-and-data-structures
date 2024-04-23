import random
import time

class Element:
    def __init__(self, priorytet, dane) -> None:
        self.__dane = dane
        self.__priorytet = priorytet    
        
    def __lt__(self, obj):
        return self.__priorytet < obj.__priorytet

    def __gt__(self, obj):
        return self.__priorytet > obj.__priorytet

    def __repr__(self):
        return repr(repr(self.__priorytet) + ": " + repr(self.__dane))

def insert_sort(tab):
    for i in range(1, len(tab)):
        for j in range(i-1, -1, -1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
            else:
                break

def shell_sort(tab):
    h = len(tab)//2
    while h >= 1:
        for offset in range(0, h):
            for i in range(1+offset, len(tab), h):
                for j in range(i-h, -1, -h):
                    if tab[j] > tab[j+h]:
                        tab[j], tab[j+h] = tab[j+h], tab[j]
                    else:
                        break
        h = h//2

def shell_sort2(tab):
    h = None
    k = 1
    while True:
        val = (3**k-1)//2
        if val < len(tab)/3:
            h = val
        else:
            break
        k += 1
    while h >= 1:
        for offset in range(0, h):
            for i in range(1+offset, len(tab), h):
                for j in range(i-h, -1, -h):
                    if tab[j] > tab[j+h]:
                        tab[j], tab[j+h] = tab[j+h], tab[j]
                    else:
                        break
        h = h//3


def main():
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    elem_list = [Element(key, value) for key, value in data]
    elem_list_shell = elem_list.copy()
    random_num = [int(random.random() * 100) for _ in range(10000)]
    random_num_shell = random_num.copy()
    random_num_shell2 = random_num.copy()
    insert_sort(elem_list)

    print(elem_list)

    # klasyczny insertion sort jest stabilny

    shell_sort(elem_list_shell)

    print(elem_list_shell)

    # sortowanie shella nie jest stabilne

    t_start = time.perf_counter()
    insert_sort(random_num)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    shell_sort(random_num_shell)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    t_start = time.perf_counter()
    shell_sort2(random_num_shell2)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

if __name__ == "__main__":
    main()