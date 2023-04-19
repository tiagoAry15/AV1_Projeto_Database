class Bucket:
    def __init__(self, id, initialSize, isOverflow=False):

        self.id = id
        self.tuplas = []
        self.initialSize = initialSize
        self.size = initialSize
        self.nextBucket = None
        self.isOverflow = isOverflow
        self.collisions = 0
        self.overflows = 0

    def add(self, tuple):
        if len(self.tuplas) == self.size:
            self.size += self.initialSize
            self.overflows += 1       
        self.tuplas.append(tuple)
            
        if len(self.tuplas) > self.initialSize:
            self.collisions += 1

    def getCollisions(self):
    
        return self.collisions 

    def getOverflows(self):

        return  self.overflows
