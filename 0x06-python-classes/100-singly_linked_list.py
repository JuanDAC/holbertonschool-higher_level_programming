#!/usr/bin/python3
"""Node is the class that defined a Node """


class Node:
    """Node is the class that defined a Node """
    def __init__(self, data, next_node=None):
        """__init__ is the class that defined a Node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """__init__ is the class that defined a Node """
        return self.__data

    @data.setter
    def data(self, value):
        """__init__ is the class that defined a Node """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def data(self):
        """__init__ is the class that defined a Node """
        return self.__data

    @data.setter
    def data(self, value):
        """__init__ is the class that defined a Node """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """__init__ is the class that defined a Node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """__init__ is the class that defined a Node """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Node is the class that defined a Node """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            current_node = self.__head
            while current_node is not None:
                if self.__head.data >= value:
                    self.__head = Node(value, self.__head)
                    break
                if current_node.next_node is None:
                    current_node.next_node = Node(value)
                    break
                elif current_node.next_node.data >= value:
                    current_node.next_node = \
                            Node(value, current_node.next_node)
                    break
                current_node = current_node.next_node

    def __str__(self):
        string = ""
        current_node = self.__head
        while current_node is None:
            new_line = "\n" if current_node.next_node is None else ""
            string += "%d%s" % (current_node.data, new_line)
            current_node = current_node.next_node
        return string


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
