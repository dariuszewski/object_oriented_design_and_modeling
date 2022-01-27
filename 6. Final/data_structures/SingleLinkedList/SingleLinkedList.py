class SingleLinkedListNode(object):

    def __init__(self, value, nxt):
        self.value = value
        self.next = nxt

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"[{self.value}:{repr.next}]"


class SingleLinkedList(object):

    def __init__(self):
        self.begin = None
        self.end = None

    def push(self, obj):
        """Appends a new value on the end of the list."""

        node = SingleLinkedListNode(obj, None)
        if self.begin == None:
            self.begin = node
            self.end = self.begin
        else:
            self.end.next = node
            self.end = node

    def pop(self):
        """Removes the last item and returns it."""

        if self.end == None:
            return None 
        elif self.end == self.begin:
            node = self.begin
            self.end = self.begin = None
            return node.value
        else:
            node = self.begin
            popped = self.end
            while node.next != self.end:
                node = node.next
            self.end = node
            node.next = None
            
            return popped.value
            

    def shift(self, obj):
        """Another name for push."""
        self.push(obj)

    def unshift(self):
        """Removes the first item and returns it."""

        if self.begin:
            node = self.begin
            if self.begin == self.end:
                self.begin = self.end = None
                return node.value
            else:
                self.begin = node.next
                return node.value
        return None

    def remove(self, obj):
        """Finds a matching item and removes it from the list."""

        if self.end == None:
            return None

        if self.end == self.begin:
            if self.end.value == obj:
                self.end = self.begin = None
                return 0
            else:
                return None

        counter = 0
        node = self.begin
        while node:
            if node.value == obj:
                if node == self.begin:
                    self.begin = node.next
                else:
                    node = node.next
                return counter
            else:
                node = node.next
                counter += 1 


    def first(self):
        """Returns a *reference* to the first item, does not remove."""
        return self.begin.value

    def last(self):
        """Returns a reference to the last item, does not remove."""
        return self.end.value

    def count(self):
        """Counts the number of elements in the list."""
        node = self.begin
        counter = 0

        while node:
            counter += 1
            node = node.next

        return counter


    def get(self, index):
        """Get the value at index."""
        
        node = self.begin
        counter = 0

        if index >= self.count() or self.count() == 0:
            return None

        while True:
            if counter == index:
                return node.value
            else:                
                counter += 1
                node = node.next


