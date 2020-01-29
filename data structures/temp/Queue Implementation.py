"""
Implementation of Queue Data Structure.
"""


class Item(object):

    """
    Reprsents an Item in Queue.
    """

    def __init__(self, value, back_end, front_end):
        """
        Inits an Item in Queue.
        Sequence of inputs specfied in that order to help visualize.
        (pushed/added to queue) back_end....front_end (popped/removed from queue)
        """

        self._value = value
        self._front_end = front_end
        self._back_end = back_end


class Queue(object):

    """
    A implementation of Queue data structure
    """

    def __init__(self):
        """
        Initiates a Queue class, holds vars like _size, capacity.
        """
        self._size = 0
        self._front_end = None
        self._back_end = None

    def __len__(self):
        """
        Returns the _size (elements count).
        """
        return self._size

    def enque(self, item):
        """
        enquees an element into the Queue at Back End.
        """

        if self._back_end is None:
            new_item = Item(item, None, None)
            self._front_end = new_item
            self._back_end = new_item
        else:
            new_item = Item(item, None, self._back_end)
            self._back_end._back_end = new_item
            self._back_end = new_item
        self._size += 1

        return new_item._value

    def deque(self):
        """
        deques (removes) an item from the front end of the Queue.
        If Queue is empty them Error is raised.
        """

        if self._front_end is None:
            raise IndexError("Queue is Empty")
        else:
            item = self._front_end
            self._front_end = item._back_end
            self._size -= 1
            return item._value

    def __str__(self):
        """
        Returns the representation of Queue.
        """
        str_form = ""
        seperator = " "
        # using seperate var to traverse so self._front_end won't get changed.
        current_front_end = self._front_end
        while current_front_end is not None:
            str_form += str(current_front_end._value) + seperator
            current_front_end = current_front_end._back_end

        return str_form.strip()


q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)
print("length of Queue is: ", len(q))
print("Str form of Queue is: ", str(q))
q.deque()
print(str(q))
q.deque()
print(str(q))
q.deque()
print(str(q))
print("length of Queue is: ", len(q))
print("Str form of Queue is: ", str(q))
