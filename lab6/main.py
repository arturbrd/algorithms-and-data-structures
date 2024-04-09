class Element:
    def __init__(self, dane, priorytet) -> None:
        self.__dane = dane
        self.__priorytet = priorytet    
        
    def __lt__(self, obj):
        return self.__priorytet < obj.__priorytet

    def __gt__(self, obj):
        return self.__priorytet > obj.__priorytet

    def __repr__(self):
        return repr(repr(self.__priorytet) + ": " + repr(self.__dane))

class Queue:
    def __init__(self):
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

def main():
    queue = Queue()
    chars = [*"GRYMOTYLA"]
    priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    for char, priority in zip(chars, priorities):
        queue.enqueue(Element(char, priority))
    queue.print_tree(0, 0)
    queue.print_tab()
    first = queue.dequeue()
    print(queue.peek())
    queue.print_tab()
    print(first)
    while not queue.is_empty():
        print(queue.dequeue())
    queue.print_tab()

if __name__ == "__main__":
    main()
