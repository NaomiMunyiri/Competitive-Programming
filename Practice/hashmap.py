class Hashtable:
    def __init__(self):
        self.MAX=100
        self.arr=[[] for i in range(self.MAX)]

    def get_hash(self,key):
        h=0
        for char in key:  #loops thru characters
            h+=ord(char)  #gets sum of ascii
        return h % self.MAX  #finds mod

    def __setitem__(self,key,val):
        h=self.get_hash(key) #gets hash index
        #self.arr[h]=val #puts index in array

        found=False
        for index, element in enumerate(self.arr[h]):
            if len(element==2) and element[0] == key:
                self.arr[h][index]=(key,val) #changes value if exists ie inserts new tuple
                found=True
                break
        if not found:
            self.arr[h].append(key,val) #if element doest exits in linked list,

    def __getitem__(self,key):
        h=self.get_hash(key)
        #return self.arr[h]
        for element in self.arr[h]:
            if element [0] == key:
                return element[1]
    
    def __delitem(self,key):
        h=self.get_hash(key)
        #self.arr[h]=None #sets array to be none
        for index, element in enumerate(self.arr[h]): #loops through list
            if element [0] == key:
                del self.arr[h][index]

if __name__=='__main__':

    t=Hashtable()
    t['march 7'] = 130
    t['march 7']
            

            
