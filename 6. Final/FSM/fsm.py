class Automaton(object):

    def __init__(self):
        self.state = self._q1
        
    def _q1(self, command):
        if command == "1":
            return self._q2
        return self._q3
    
    def _q2(self, command):
        if command == "1":
            return self._q2
        return self._q3
    
    def _q3(self, command):
        return self._q2

    def read_commands(self, commands):
        for command in commands:
            self.state = self.state(command)
        
        return self.state == self._q2

my_automaton = Automaton()