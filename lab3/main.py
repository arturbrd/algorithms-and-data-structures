def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]

class Queue:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.size = 5
        self.front = 0
        self.back = 0

    def is_empty(self):
        return self.front == self.back and self.tab[self.front] is None

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.front]

    def dequeue(self):
        if self.is_empty():
            return None       
        index = self.front
        val = self.tab[index]
        self.tab[index] = None
        if index + 1 == self.size:
            self.front = 0
        else:
            self.front += 1
        return val

    def enqueue(self, data):
        if not self.is_empty() and self.back == self.front:
            self.tab = realloc(self.tab, self.size*2)
            for i in range(self.back, self.size):
                self.tab[i], self.tab[i+self.size] = self.tab[i+self.size], self.tab[i]
            if self.front >= self.back:
                self.front += self.size
            self.size *= 2
        self.tab[self.back] = data
        if self.back + 1 == self.size:
            self.back = 0
        else:
            self.back += 1

    def __str__(self):
        string = ""
        for i in range(self.size):
            index = (i+self.front)%self.size
            val = self.tab[index]
            if val is not None:
                string += str(val)+", "
            if index == self.back:
                string = string[:-2]
                break
        return "["+string+"]"

    def print_tab(self):
        print(self.tab)

queue = Queue()
for i in range(1,5):
    queue.enqueue(i)
print(queue.dequeue())
print(queue.peek())
print(queue)
for i in range(5,9):
    queue.enqueue(i)
queue.print_tab()
while not queue.is_empty():
    queue.dequeue()
print(queue)