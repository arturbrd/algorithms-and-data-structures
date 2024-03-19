class ResolvingCollisionException(Exception):
    pass

class NoSuchKeyException(Exception):
    pass

class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.__tab = [None for i in range(size)]
        self.__size = size
        self.__c1 = c1
        self.__c2 = c2
        
    def hash(self, key):
        if isinstance(key, str):
            counter = 0
            for i in [*key]:
                counter += ord(i)
            key = counter
        return key%self.__size
    
    def resolve_collision(self, key):
        for i in range(1, self.__size):
            new_hash = self.hash(self.hash(key) + self.__c1*i + self.__c2*i*i)
            new_el = self.__tab[new_hash]
            if new_el is None or new_el.key == key:
                return new_hash
        raise ResolvingCollisionException
        
    def search(self, key):
        hash = self.hash(key)
        element = self.__tab[hash]
        if element is not None and element.key == key:
            return element.value
        else:
            try:
                new_hash = self.resolve_collision(key)
            except ResolvingCollisionException:
                return None
            return self.__tab[new_hash].value
            
        
    def insert(self, key, data):
        hash = self.hash(key)
        element = self.__tab[hash]
        if element is not None and element.key != key:
            hash = self.resolve_collision(key)
        self.__tab[hash] = Element(key, data)

    
    def remove(self, key):
        hash = self.hash(key)
        element = self.__tab[hash]
        if element is not None and element.key != key:
            hash = self.resolve_collision(key)
        self.__tab[hash] = None
        
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
    keys = [*range(1, 16)]
    keys[5] = 18
    keys[6] = 31
    
    for key, val in zip(keys, letters):
        try:
            tab.insert(key, val)
        except ResolvingCollisionException:
            print("Brak miejsca")
    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    try:
        tab.insert(5, 'Z')
    except ResolvingCollisionException:
        print("Brak miejsca")
    print(tab.search(5))
    try:
        tab.remove(5)
    except ResolvingCollisionException:
        print("Brak miejsca")
    except NoSuchKeyException:
        print("Brak danej")
    print(tab)
    print(tab.search(31))
    try:
        tab.insert('test', 'W')
    except ResolvingCollisionException:
        print("Brak miejsca")
    print(tab)
    
    

def test2(size=13, c1=1, c2=0):    
    tab = HashTable(size, c1, c2)
    keys = [i*13 for i in range(1, 16)]

    for key, val in zip(keys, letters):
        try:
            tab.insert(key, val)
        except ResolvingCollisionException:
            print("Brak miejsca")
    print(tab)

test1()
test2()
test2(c1=0, c2=1)
test1(c1=0, c2=1)