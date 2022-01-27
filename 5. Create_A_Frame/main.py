
class AbstractBox:
    
    def get_width(self):
        raise NotImplementedError

    def get_height(self):
        raise NotImplementedError

    def set_width(self, new_width):
        raise NotImplementedError

    def set_height(self, new_height):
        raise NotImplementedError

    def negotiate_width(self, expected_width=None):
        raise NotImplementedError

    def negotiate_height(self, expected_height=None):
        raise NotImplementedError

class BaseBox(AbstractBox):
    def get_size(self):
        return self.get_width(), self.get_height()

    def set_size(self, new_width, new_height):
        self.get_width(new_width)
        self.get_height(new_height)

    def negotiate_size(self, expected_width=None, expected_height=None):
        actual_width = self.negotiate_width(expected_width)
        actual_height = self.negotiate_width(expected_height)
        return self.get_size()

class RowIterable():
    def __iter__(self):
        raise NotImplementedError
        

class StringBox(BaseBox, RowIterable):

    def __init__(self, string):
        self.content = string
        self.width = len(string)
        self.height = 1

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def set_width(self, new_width):
        self._width = new_width

    def set_height(self, new_height):
        self._height = new_height

    def __iter__(self):
        yield self.content.ljust(self.width)[:self._width]


