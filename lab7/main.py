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

class Queue:
    def __init__(self, list=None):
        if list is not None:
            self.tab = list
            self.heap_size = len(list)
            index = self.parent(self.heap_size-1)
            while index >= 0:
                self.repair(index)
                index -= 1
        else:
            self.tab = []
            self.heap_size = 0

    def is_empty(self) -> bool:
        return self.heap_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[0]

    def dequeue(self):
        el = self.tab[0]
        self.tab[0] = self.tab[self.heap_size-1]
        self.tab[self.heap_size-1] = el
        self.heap_size -= 1
        self.repair(0)
        return el

    def repair(self, index):
        while True:
            child_to_swap = None
            left = self.left(index)
            right = self.right(index)
            if left is not None and self.tab[index] < self.tab[left]:
                child_to_swap = left
                if right is not None and self.tab[left] < self.tab[right]:
                    child_to_swap = right
            elif right is not None and self.tab[index] < self.tab[right]:
                child_to_swap = right
            else:
                break
            self.tab[index], self.tab[child_to_swap] = self.tab[child_to_swap], self.tab[index]
            index = child_to_swap
            
    def enqueue(self, el: Element):
        if self.heap_size == len(self.tab):
            self.tab.append(el)
        elif self.heap_size < len(self.tab):
            self.tab[self.heap_size] = el
        else:
            raise(Exception)
        index = self.heap_size
        self.heap_size += 1
        while True:
            parent = self.parent(index)
            if parent is None:
                break
            if self.tab[parent] < self.tab[index]:
                self.tab[parent], self.tab[index] = self.tab[index], self.tab[parent]
                index = parent
            else:
                break

    def left(self, index):
        new_index = 2*index+1
        if new_index >= self.heap_size:
            return None
        else:
            return new_index

    def right(self, index):
        new_index = 2*index+2
        if new_index >= self.heap_size:
            return None
        else:
            return new_index

    def parent(self, index):
        if index == 0:
            return None
        else:
            return int((index-1)//2)

    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.heap_size], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx < self.heap_size:
            right = self.right(idx)
            left = self.left(idx)
            if right is not None:           
                self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)    
            if left is not None:       
                self.print_tree(self.left(idx), lvl+1)

    def sort(self):
        while not self.is_empty():
            self.dequeue()
        return self.tab

def swap(tab):
    for i in range(len(tab)):
        min_v = tab[i]
        m = i
        for j in range(i, len(tab)):
            if tab[j] < min_v:
                min_v = tab[j]
                m = j
        # m = tab.index(min(tab[i:]))
        tab[i], tab[m] = tab[m], tab[i]

def shift(tab):
    for i in range(len(tab)):
        min_v = tab[i]
        m = i
        for j in range(i, len(tab)):
            if tab[j] < min_v:
                min_v = tab[j]
                m = j
        # m = tab.index(min(tab[i:]))
        tab.insert(i, tab.pop(m))

def main():
    # kopcowe na elementach
    data = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    elem_list = [Element(key, value) for key, value in data]
    heap = Queue(elem_list)
    heap.print_tab()
    heap.print_tree(0, 0)
    heap.sort()
    print(elem_list)

    # algorytm kopcowy nie jest stabilny

    # kopcowe na losowych liczbach
    random_num = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()
    heap2 = Queue(random_num)
    heap2.sort()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # swap na elementach
    to_swap = [Element(key, value) for key, value in data]
    swap(to_swap)
    print(to_swap)

    # algorytm pzez wybieranie (swap) nie jest stabilny

    # shift na elementach
    to_shift = [Element(key, value) for key, value in data]
    shift(to_shift)
    print(to_shift)

    # algorytm pzez wybieranie (shift) jest stabilny

    # swap na losowych liczbach
    random_num2 = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()
    swap(random_num2)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

    # shift na losowych liczbach
    random_num3 = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()
    shift(random_num3)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))

if __name__ == "__main__":
    main()