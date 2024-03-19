class LinkedList:

    def __init__(self):
        self.head = None
        self.cursor = None

    def destroy(self):
        self.head = None
        self.cursor = None
        return None
    
    def add(self, data):
        self.head = Element(data, self.head)
    
    def append(self, data):
        if self.is_empty():
            self.head = Element(data)
        else:
            for el in self:
                if el.next is None:
                    el.next = Element(data)
                    break

    def remove(self):
        if self.is_empty():
            return None
        self.head = self.head.next

    def remove_end(self):
        if self.is_empty():
            return None
        elif self.head.next is None:
            self.head = None
        else:
            for el in self:
                if el.next.next is None:
                    el.next = None
                    break
    
    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        if self.is_empty():
            return 0
        else:
            length = 0
            for _ in self:
                length = length + 1
            return length
        
    def get(self, index):
        if len(self) <= index:
            return None
        else:
            for i, el in enumerate(self):
                if i == index:
                    return el.data

    def __iter__(self):
        self.cursor = self.head
        return self
    
    def __next__(self):
        if self.cursor is None:
            self.cursor = None
            raise StopIteration
        data = self.cursor
        self.cursor = self.cursor.next
        return data
    
    def __str__(self):
        list_str = ""
        for el in self:
            list_str += "-> "+str(el.data)+"\n"
        return list_str[:-1]


class Element:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def main():
    tab = [('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]
    uczelnie = LinkedList()
    uczelnie.append(tab[0])
    uczelnie.append(tab[1])
    uczelnie.append(tab[2])
    uczelnie.add(tab[3])
    uczelnie.add(tab[4])
    uczelnie.add(tab[5])
    print(uczelnie)
    print(len(uczelnie))
    uczelnie.remove()
    print(uczelnie.get(0))
    uczelnie.remove_end()
    print(uczelnie)
    uczelnie.destroy()
    print(uczelnie.is_empty())
    uczelnie.remove()
    uczelnie.append(tab[0])
    uczelnie.remove_end()
    print(uczelnie.is_empty())

if __name__ == "__main__":
    main()