node_tab_size = 6

class Node:
    def __init__(self):
        self.tab = [None for i in range(node_tab_size)]
        self.count = 0
        self.next = None

    def insert(self, index, data):
        if index <= self.count:
            for i in range(self.count-1, index-1, -1):
                self.tab[i+1] = self.tab[i]
            self.tab[index] = data
            self.count += 1

    def delete(self, index):
        if index+1 <= self.count:
            for i in range(index, self.count-1):
                self.tab[i] = self.tab[i+1]
            self.tab[self.count-1] = None
            self.count -= 1
    
    def is_full(self):
        return self.count == node_tab_size
    
    def is_empty(self):
        return self.count == 0
    
    def is_half_empty(self):
        return self.count < node_tab_size/2
            
class UnrolledLinkedList:
    def __init__(self):
        self.first = Node()

    def get(self, index):
        pointer = self.first
        while True:
            if index > pointer.count-1:
                if pointer.next is None:
                    return None
                else:
                    index -= pointer.count
                    pointer = pointer.next
            else:
                return pointer.tab[index]
            
    def insert(self, index, data):
        pointer = self.first
        while True:
            if index > pointer.count-1:
                if pointer.next is None:
                    if pointer.is_full():
                        pointer.next = Node()
                        pointer.next.insert(0, data)
                        break
                    else:
                        pointer.insert(pointer.count, data)
                        break
                else:
                    index -= pointer.count
                    pointer = pointer.next
            else:
                if pointer.is_full():
                    if pointer.next is None:
                        pointer.next = Node()
                        for i in range(node_tab_size-1, (node_tab_size-1)//2, -1):
                            pointer.next.insert(0, pointer.tab[i])
                            pointer.delete(i)
                        break
                    else:
                        temp = pointer.next
                        pointer.next = Node()
                        for i in range(node_tab_size-1, (node_tab_size-1)//2, -1):
                            pointer.next.insert(0, pointer.tab[i])
                            pointer.delete(i)
                        pointer.next.next = temp
                        self.insert(index, data)
                        break
                else:
                    pointer.insert(index, data)
                    break

    def delete(self, index):
        pointer = self.first
        while True:
            if index > pointer.count-1:
                if pointer.next is None:
                    break
                else:
                    index -= pointer.count
                    pointer = pointer.next
            else:
                pointer.delete(index)
                while pointer.next is not None:
                    if pointer.is_half_empty() and pointer.next.tab[0] is not None:
                        temp = pointer.next.tab[0]
                        pointer.next.delete(0)
                        pointer.insert(pointer.count, temp)
                    if pointer.next.tab[0] is None:
                        pointer.next = None
                        break
                    pointer = pointer.next       
                break

    def __str__(self):
        string ="["
        pointer = self.first
        while True:
            for i in pointer.tab:
                if i is not None:
                    string += str(i)
                    string += ", "
            if pointer.next is None:
                break
            pointer = pointer.next
        string = string[:-2]
        return string+"]"
    
    def debug_print(self):
        string ="start: "
        pointer = self.first
        while True:
            string += str(pointer.tab)
            if pointer.next is None:
                break
            pointer = pointer.next
        print(string)

def main():
    ullist = UnrolledLinkedList()
    for i in range(1,10):
        ullist.insert(i-1,i)
    print(ullist.get(4))
    ullist.insert(1, 10)
    ullist.insert(8, 11)
    print(ullist)
    ullist.delete(1)
    ullist.delete(2)
    print(ullist)
    ullist.debug_print()

if __name__ == "__main__":
    main()