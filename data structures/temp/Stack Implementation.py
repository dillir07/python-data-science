"""
Implementation of Stack Data Structure.
"""


class Item:

    """
    Reprsents an Item in Stack.
    """

    def __init__(self, _value, _top, _bottom):
        self._value = _value
        self._top = _top
        self._bottom = _bottom


class Stack:

    """
    A implementation of Stack data structure
    """

    def __init__(self):
        """
        Initiates a stack class, holds vars like _size, capacity.
        """
        self._size = 0
        self._top = None

    def __len__(self):
        """
        Returns the _size (elements count).
        """
        return self._size

    def push(self, item):
        """
        Pushes an element on to the Stack.
        """

        if self._top is None:
            new_item = Item(item, None, None)
        else:
            new_item = Item(item, None, self._top)
        self._top = new_item
        self._size += 1

        return new_item

    def pop(self):
        """
        Pops (removes) an item from the Stack.
        If Stack is empty them Error is raised.
        """

        if self._top is None:
            raise IndexError("Stack is Empty")
        else:
            item = self._top
            self._top = item._bottom
            self._size -= 1
            return item

    def __str__(self):
        """
        Returns the representation of Stack.
        """
        str_form = ""
        seperator = " "
        # using seperate var to traverse so self._top won't get changed.
        current_top = self._top
        while current_top is not None:
            str_form += str(current_top._value) + seperator
            current_top = current_top._bottom

        return str_form.strip()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print("length of Stack is: ", len(s))
print("Str form of Stack is: ", str(s))
s.pop()
s.pop()
s.pop()
s.pop()
print("length of Stack is: ", len(s))
print("Str form of Stack is: ", str(s))
# s.pop() -> throws Index error
