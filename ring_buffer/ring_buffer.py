class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.capacity > self.current:
            if self.storage[0] is not None:
                self.current += 1

            if self.current >= self.capacity:
                self.current = 0\

            self.storage[self.current] = item

        else:
            if self.current < len(self.storage):
                self.current += 1
            else:
                self.current = 0
            self.storage[self.current] = item
        return

    def get(self):
        return [x for x in self.storage if x is not None]