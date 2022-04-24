class UndergroundSystem:

    def __init__(self):
        self.UndSystemMean = [{} for i in range(26)]
        self.ridingPassengers = [{} for i in range(10)]
        #hash by first letter of alphabet
        self.StationHashFunc = lambda x: ord(x[0]) % 26
        self.PassengerHashFunc = lambda x: x % 10

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        #add to passenger list
        index = self.PassengerHashFunc(id)
        self.ridingPassengers[index][str(id)] = (stationName, t)
        
        #print(self.ridingPassengers[index])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        #print(str(id) + " : " + stationName + " : " + str(t))
    
        #erasing current passengers
        pIndex = self.PassengerHashFunc(id)
        startingStation, startingTime = self.ridingPassengers[pIndex].pop(str(id))
        consumedTime = t - startingTime
        
        #keeps on updating the mean
        index = self.StationHashFunc(startingStation)
        
        if startingStation not in self.UndSystemMean[index]:
            self.UndSystemMean[index][startingStation] = {stationName : (consumedTime, 1)}
        else:
            #case 1 - goal station not yet initialized
            if stationName not in self.UndSystemMean[index][startingStation]:
                self.UndSystemMean[index][startingStation][stationName] = (consumedTime, 1)
            
            #case 2 - goal station is inside
            else:
                currentMean, cnt = self.UndSystemMean[index][startingStation][stationName]
                newMean = ((currentMean * cnt) + consumedTime) / (cnt + 1)
                self.UndSystemMean[index][startingStation][stationName] = (newMean, cnt + 1)
        
        #print(self.UndSystemMean[index])
                
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #match with dict name
        index = self.StationHashFunc(startStation)
        averageTime, cnt = self.UndSystemMean[index][startStation][endStation]
        return averageTime


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)