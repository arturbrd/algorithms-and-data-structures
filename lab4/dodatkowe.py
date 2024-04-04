import random

class SkipList:
    def __init__(self, max_level):
        self.__head = [None for _ in range(max_level)]
        self.__max_level = max_level

    def search(self, key):
        pass

    def insert(self, key, data):
        next_list = self.__head
        prev = next_list.copy()
        for i in range(self.__max_level - 1, -1, -1):
            while next_list[i] is not None:
                if (next_list[i] is not None and key < next_list[i].key) or (i == 0 and next_list[i] is None):
                    lvl = self.randomLevel()
                    new_el = Element(key, data, lvl)
                    next_list[:lvl] = [new_el for _ in range(lvl)]
                    new_el.next_list = prev[:lvl]
                    break
                else:
                    prev[:i+1] = next_list[:i+1].copy()
                next_list[:i+1] = next_list[i]
        lvl = self.randomLevel()
        new_el = Element(key, data, lvl)
        next_list[:lvl] = [new_el for _ in range(lvl)]
        new_el.next_list = prev[:lvl]

    def remove(self, key):
        pass

    def __str__(self):
        pass

    def randomLevel(self, p=0.5):
        lvl = 1
        while random.random() < p and lvl < self.__max_level:
            lvl += 1
        return lvl
    
    def displayList(self):
        node = self.__head[0]  # pierwszy element na poziomie 0
        keys = [ ]                        # lista kluczy na tym poziomie
        while node is not None:
            keys.append(node.key)
            node = node.next_list[0]

        for lvl in range(self.__max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.__head[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.value:2s}", end="")
                node = node.next_list[lvl]
            print()

class Element:
    def __init__(self, key, value, levels):
        self.key = key
        self.value = value
        self.levels = levels
        self.next_list = [None for _ in range(levels)]

letters = 'abcdefghijklmno'
random.seed(42)   
sl = SkipList(5)
for i, letter in zip(range(1, 16), letters):
    sl.insert(i, letter)
    if i > 2:
        break
sl.displayList()
