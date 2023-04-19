

class HashUtil:
    def __init__(self):
        self.mod = 1
        pass
    def hash(self,value):
        soma = 1
        for letter in value:
            soma *= ord(letter)

        return soma % self.mod
