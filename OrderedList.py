from Node import Node
from LinkedListIterator import LinkedListIterator

class OrderedList:

    def __init__(self):
        self.__head = None
        self.__count = 0
    
    def is_empty(self):
        return self.__count == 0

    def size(self):
        return self.__count

    def add(self,item):
        new_node = Node(item)
        curr = self.__head
        prev = None
        stop = False
        while curr != None and not stop:
            if item < curr.get_data():
                stop = True
            else:
                prev = curr
                curr = curr.get_next()
        new_node.set_next(curr)
        if prev == None:
            self.__head = new_node
        else:
            prev.set_next(new_node)
        self.__count += 1
        
    def search(self,item):
        curr = self.__head
        while curr != None:
            if curr.get_data() == item:
                return True
            elif curr.get_data() > item:
                return False
            else:
                curr = curr.get_next()
        return False

    def remove(self,item):
        curr = self.__head
        prev = None
        while curr != None and curr.get_data() != item:
            prev = curr
            curr = curr.get_next()
        if prev == None:
            self.__head = curr.get_next()
        else:
            prev.set_next(curr.get_next())
        self.__count -= 1

    def __iter__(self):
        return LinkedListIterator(self.__head)

