class RandomizedSet:

    def __init__(self):
        self.items={} #dictionary
        

    def insert(self, val: int) -> bool:
        if self.items.get(val): #if it exists
            return False
        else:
            self.items[val]=True #insert if it doesnt exist
            return True        

    def remove(self, val: int) -> bool:
        if self.items.get(val): #if exists
            self.items.pop(val) #remove
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.items.keys()))