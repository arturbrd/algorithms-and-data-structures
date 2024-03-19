import random

class SkipList:
    def __init__(self, maxHeight):
        self.__head = Element
        self.__maxHeight = maxHeight

    def search(self, key):
        pass

    def insert(self, key, data):
        pass

    def remove(self, key):
        pass

    def __str__(self):
        pass

    def randomLevel(self, p):
        lvl = 1
        while random.random() < p and lvl < self.__maxHeight:
            lvl += 1
        return lvl

class Element:
    def __init__(self):
        self.key = key
        self.value = value
        self.height = height
        self.nextList = None

    
