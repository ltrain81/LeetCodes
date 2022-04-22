class MyHashMap:

    def __init__(self):
        self.MyHash = [[] for i in range(10)]
        self.HashFunc = lambda x: x % 10
        
    def put(self, key: int, value: int) -> None:
        place = self.HashFunc(key)
        curVal = self.findTuple(key)
        if curVal == -1:
            self.MyHash[place].append((key, value))
        else:
            print(str(key) + " : " + str(curVal))
            self.MyHash[place].remove((key, curVal))
            self.MyHash[place].append((key, value))

    def get(self, key: int) -> int:
        place = self.HashFunc(key)
        withIn = self.findTuple(key)
        return withIn

    def remove(self, key: int) -> None:
        place = self.HashFunc(key)
        value = self.findTuple(key)
        if value != -1:
            self.MyHash[place].remove((key, value))
            
    def findTuple(self, key):
        place = self.HashFunc(key)
        for k, v in self.MyHash[place]:
            if k == key:
                return v
        return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)