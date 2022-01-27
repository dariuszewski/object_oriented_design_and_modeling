from enum import Enum

class Command(Enum):
    LEFT = 0
    RIGHT = 1
    DOWN = 2
    PROG1 = 11
    PROG2 = 12
    PROG3 = 13
    PROG4 = 14

class Flag(Enum):
    NONE = 0
    ANY = 1
    RED = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5

class InstructionSet(Enum):
    MPDEC = 0
    MPINC = 1
    CALL = 3
    RET = 4
    EQ = 5
    EMP = 6
    NEMP = 7
    FSKIP = 8
    SKIP = 9
    PUSH = 10
    POP = 11
    NOP = -1
    BRK = -2

class CommandCompiler:
    def translate(self, command):
        return [...]

class ProgramControl:
    def __init__(self, programs, default_instruction=InstructionSet.NOP):
        self.programs = [list(p) for p in programs]
        self.ip = (0, 0)
        self.default = default_instruction
        self.stack = []

    def retrive_instruction(self):
        try:
            prog_idx, instr_idx = self.ip
            current_program = self.programs[prog_idx]
            current_instruction = current_program[instr_idx]
            self.advance_ip()
            return current_program[instr_idx]
        except IndexError:
            return self.default

    def advance_ip(self):
        self.move_ip(1)

    def move_ip(self, offest):
        self.ip = self.offset_ip(offest)

    def offset_ip(self):
        try:
            prog_idx, cmd_idx = self.ip
            current_program = self.programs[prog_idx]
            self.ip = min(cmd_idx + 1, len(current_program))
        except IndexError:
            return self.ip

    def switch_program(self, prog_idx):
        self.stack.append(self.ip)
        self.ip = prog_idx, 0

    def switch_back(self):
        try:
            self.ip = self.stack.pop()
        except IndexError:
            pass