class UndergroundSystem:

    def __init__(self):
        #use 2 hashes-save check in time&upd tot time
        #key=customer id: timestart,startStation
        self.i=defaultdict(tuple) #hash-tuple

        #(startStation,endStation):timeEnd-timeStart
        self.o=defaultdict(list) #hash-list
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id]=(t,stationName)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime,startStation=self.i[id] #tuple
        Total=t-starttime #how long it took
        self.o[(startStation,stationName)].append(Total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.o[(startStation,endStation)])/len(self.o[(startStation,endStation)])