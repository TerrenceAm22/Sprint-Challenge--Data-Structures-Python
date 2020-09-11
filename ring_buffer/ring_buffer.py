from double_linked import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None # a, b, c, d
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check size of the storage is less than the capacity
        if len(self.storage) < self.capacity:
            #add item to the tail
            self.storage.add_to_tail(item)
            return
        #if current has no value
        if self.current is None:
            self.current = self.storage.head
        #sets the current value to the item
        self.current.value = item
        #set current to the next  value
        self.current = self.current.next
       

    def get(self):
        # create a blank array 
        buffer = []
        # declare a current variable & set it to the head of the
        current = self.storage.head
        # while there still a current value
        while current:
            # append the value to the buffer
            buffer.append(current.value)
            # move the current reference to the next node in the
            current = current.next
        return buffer