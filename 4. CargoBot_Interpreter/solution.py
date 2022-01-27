
    
class Interpreter:
    
    def __init__(self, initial_state, programs, max_steps):
        self.stacks = [stack for stack in initial_state]
        self.programs = [{'commands' : i, 'command_pointer': 0, 'caller' : 0} for i in programs]
        self.max_steps = max_steps
        self.steps = 0
        self.stack_pointer = 0
        self.program_pointer = 0
        self.claw = None
        
    def move(self, direction):
        if direction == "RIGHT" and self.stack_pointer < len(self.stacks)-1:
            self.stack_pointer += 1
            #print(f"claw moved from position {self.stack_pointer-1} to {self.stack_pointer}")
        elif direction == "LEFT" and self.stack_pointer > 0:
            self.stack_pointer -= 1
            #print(f"claw moved from position {self.stack_pointer+1} to {self.stack_pointer}")
        
    def action(self):
        if self.claw == None:
            try:
                self.claw = self.stacks[self.stack_pointer][-1]
                self.stacks[self.stack_pointer].pop()
                #print(f"picked up {self.claw} from {self.stack_pointer}")
            except IndexError:
                self.claw = None
                #print(f"picked up {self.claw} from {self.stack_pointer}")
        else:
            #print(f"putting down {self.claw} to {self.stack_pointer}")
            self.stacks[self.stack_pointer].append(self.claw)
            self.claw = None
            #print(f"picked up {self.claw} from {self.stack_pointer}")
            
    def change_program(self, program_number):        
        self.programs[int(program_number[4])-1]['caller'] = self.program_pointer
        self.program_pointer = int(program_number[4])-1
        self.programs[self.program_pointer]['command_pointer'] = 0
        #print(f"program changed from {self.programs[self.program_pointer]['caller'] } to {self.program_pointer}")

        
    def execute(self, command):
        
        self.programs[self.program_pointer]['command_pointer'] += 1
        
        if command.flag is not None:
            
        
            if command.flag  == "NONE" and self.claw is not None:
            #if command.flag != self.claw and self.claw is None:
                #print(f'flag: {command.flag} claw {self.claw}, no operation performed')
                return None

            elif command.flag == "ANY" and self.claw is None:
                #print(f'flag: {command.flag} claw {self.claw}, no operation performed')
                return None

            elif command.flag not in (None, "ANY", "NONE"):
                if not hasattr(self.claw, 'color') or self.claw.color != command.flag:
                    #print(f'flag: {command.flag} claw {self.claw}, no operation performed')
                    return None        

        

        if command.command in ("LEFT", 'RIGHT'):
            return self.move(command.command)
        elif command.command == "DOWN":
            return self.action()
        elif command.command[0] == "P":
            return self.change_program(command.command)
        
    def debug(self):
        print(f"current program: {self.program_pointer}")
        print(f"caller: {self.programs[self.program_pointer]['caller']}")
        print(f"current state: {self.programs[self.program_pointer]['command_pointer']}")
        print(f"current command set: {self.programs[self.program_pointer]['commands']}")
        print(f"current stack: {self.stack_pointer}")
        print(f"stack: {self.stacks[self.stack_pointer]}")
        for i in range(len(self.stacks)):
            print(f'stack {i}: {self.stacks[i]}')
        print(f"steps: {self.steps}/{self.max_steps}")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++")
        
        
    def run(self):
        #print(self.programs)
        

        
        
        for i in range(self.max_steps):
            #self.debug()
            #print(self.programs)
            #print(len(self.programs))
            
            done = 0
            for program in self.programs:
                if len(program['commands']) <= program['command_pointer']:
                    done += 1
                if done == len(self.programs):
                    return self.stacks
            
            if self.programs[self.program_pointer]['command_pointer'] > len(
                self.programs[self.program_pointer]['commands'])-1:            

                #print(f"moving back to program {self.programs[self.program_pointer]['caller']}")
                #self.program_pointer = self.previous_command
                if self.programs[self.program_pointer]['caller'] == self.program_pointer:
                    return self.stacks
                self.program_pointer = self.programs[self.program_pointer]['caller'] 
                #print(f"state of program: {self.programs[self.program_pointer]['command_pointer']}")
                continue
            
            
            else:
                self.max_steps -= 1
                self.execute(self.programs[self.program_pointer]['commands']
                         [self.programs[self.program_pointer]['command_pointer']])
            
            #self.programs[self.program_pointer]['command_pointer'] += 1
                                   
            
        #self.debug()
        if self.max_steps > 0: self.run()
        return self.stacks
        
        


def cargobot(initial_state, programs, max_steps):
    return Interpreter(initial_state, programs, max_steps).run()