class ResponsivePicture:
    
    def __init__(self, text, char):
        self.text = text
        self.char = char
        self.width = max([len(string) for string in text]) + 4

        
    def draw(self):
        picture =  (self.char*self.width) + '\n'
        for i in range(len(self.text)):
            chars_to_fill = self.width - len(self.text[i]) - 3
            line =  self.char + ' ' + self.text[i] + ' ' * chars_to_fill + self.char + '\n'
            picture += line

        picture += (self.char*self.width)
        return picture

def frame(text, char):
    return ResponsivePicture(text, char).draw()