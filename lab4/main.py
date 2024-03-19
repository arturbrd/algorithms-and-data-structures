class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.__tab = [None for i in range(size)]
        self.__size = size
        self.__c1 = c1
        self.__c2 = c2
        
    def hash(self, key):
        if isinstance(key, str):
            key = ord(key)
        return key%self.__size
    
    def resolve_collision(self, key):
        for i in range(1, self.__size):
            return self.hash(key) + self.__c1*i + self.__c2*i*i      
        
    def search(self, key):
        hash = self.hash(key)
        element = self.__tab[hash]
        if element is not None and element.key == key:
            return element.value
        else:
            pass
            
        
    def insert(self, key, data):
        hash = self.hash(key)
        if self.__tab[hash] is None:
            self.__tab[hash] = Element(key, data)
    
    def remove(self, key):
        pass
        
    def __str__(self):
        tabstr = ""
        for i in self.__tab:
            tabstr += f"{i}, "
        tabstr = tabstr[:-2]
        return "["+tabstr+"]"

    
class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

def test1(size=13, c1=1, c2=0):
    tab = HashTable(size, c1, c2)
    keys = [i for i in range(1, 16)]
    keys[5] = 18
    keys[6] = 31
    
    for key, val in zip(keys, letters):
        tab.insert(key, val)
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(5, 'Z')
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))
    tab.insert('test', 'W')
    print(tab)

def test2(size=13, c1=1, c2=0):
    tab = HashTable(size, c1, c2)
    keys = [i*13 for i in range(1, 16)]

    for key, val in zip(keys, letters):
        tab.insert(key, val)
    print(tab)


# tab = HashTable(7)
# tab.insert(8, "8 -> 1")
# print(tab.search(7))
# tab.insert(0, "0 -> 1")
# print(tab)

test1()
test2()
test2(c1=0, c2=1)
test1(c1=0, c2=1)