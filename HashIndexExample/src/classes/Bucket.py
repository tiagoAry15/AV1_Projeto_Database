class Bucket:
    def __init__(self, id, size, isOverflow=False):

        self.id = id
        self.tuplas = []
        self.size = size
        self.nextBucket = None
        self.isOverflow = isOverflow
        self.collisions = 0
        self.overflows = 0

    def add(self, tuple):
        if len(self.tuplas) == self.size:
            if self.nextBucket == None:
                self.nextBucket = Bucket(self.id, self.size, True)
                self.overflows += 1
            self.nextBucket.add(tuple)

        else:
            self.tuplas.append(tuple)
            if self.isOverflow == True and len(self.tuplas) > 0:
                self.collisions += 1

    def getCollisions(self):
        soma = 0
        soma += self.collisions
        return soma + self.nextBucket.getCollisions() if self.nextBucket != None else soma

    def getOverflows(self):
        soma = 0
        soma += self.overflows
        return soma + self.nextBucket.getOverflows() if self.nextBucket != None else soma
