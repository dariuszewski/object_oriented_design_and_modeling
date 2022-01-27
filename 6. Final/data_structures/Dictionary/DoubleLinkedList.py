class DoubleLinkedListNode(object):

    def __init__(self, value, nxt, prev):
        self.value = value
        self.next = nxt
        self.prev = prev

    def __repr__(self):
        nval = self.next and self.next.value or None
        pval = self.prev and self.prev.value or None
        return f"[{self.value}, {repr(nval)}, {repr(pval)}]"


class DoubleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""

        if self.end:
            node = DoubleLinkedListNode(obj, None, self.end)
            self.end.next = node
            self.end = node
        else:
            self.begin = self.end =  DoubleLinkedListNode(obj, None, None)


    def pop(self):
        """Removes the last item and returns it."""

        if self.end:
            node = self.end

            if self.end != self.begin:
                node.prev.next = None
                self.end = node.prev
                return node.value

            elif self.end == self.begin:
                self.end = self.begin = None
                return node.value
            
        else:
            return None

    def shift(self, obj):
        """Actually just another name for push."""
        self.push(obj)

    def unshift(self):
        """Removes the first item (from begin) and returns it."""
        
        if self.begin:
            node = self.begin

            if self.begin != self.end:
                self.begin = node.next
                self.begin.prev = None
            else:
                self.begin = self.end = None

            return node.value

        else: return None

    def count(self):
        """Counts the number of elements in the list."""

        node = self.begin
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def detach_node(self, node):
        """You'll need to use this operation sometimes, but mostly 
        inside remove().  It should take a node, and detach it from
        the list, whether the node is at the front, end, or in the middle."""

        if self.end == node:
            self.pop()
        elif self.begin == node:
            self.unshift()
        else:
            nxt = node.next
            prev = node.next

            prev.next = nxt
            next.prev = prev


    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

        node = self.begin
        counter = 0
        
        while node:
            if node.value == obj:
                self.detach_node(node)
                return counter
            else:
                node = node.next
                counter += 1

        return None

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin and self.begin.value or None

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end and self.end.value or None

    def _invariant(self):
        if self.begin == None:
            assert self.end == None, "End set while begin is not."

        if self.begin:
            assert self.begin.prev == None, "begin.prev not None"
            assert self.end.next == None, "end.next not None"

    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin and self.begin.value or None

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end and self.end.value or None

    def get(self, index):
        """Get the value at index."""
        # similar code to count, but stop at index and return value or None
        node = self.begin
        i = 0
        while node:
            if i == index:
                return node.value
            else:
                i += 1
                node = node.next
        return None

    def dump(self, mark):
        """Debugging function that dumps the contents of the list."""
        # set node to begin
        node = self.begin
        print(">>>> ", end="")
        # while there's a node, print it out
        while node:
            print(node, end="")
            node = node.next
        # print new line
        print()




