

class HashUtil:
    def hash(value):
        soma = 0
        for letter in value:
            soma += ord(letter)

        return soma % 100
