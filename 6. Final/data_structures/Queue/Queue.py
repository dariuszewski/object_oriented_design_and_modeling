from DoubleLinkedList import *


"""building on top of double linked list makes it have
all possibillities of it. Only difference is unshift function."""

class Queue(DoubleLinkedList):

    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        """Overwriten becouse in DLS it was push"""

        if self.end:
            node = self.end

            if self.begin != self.end:
                self.end= node.prev
                self.end.next = None
            else:
                self.begin = self.end = None

            return node.value

        else: return None

        