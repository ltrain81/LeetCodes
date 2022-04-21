class MyHashSet:

    def __init__(self):
        self.MyHash = [[] for i in range(10)]
        self.HashFunc = lambda x: x % 10

    def add(self, key: int) -> None:
        place = self.HashFunc(key)
        if key not in self.MyHash[place]:
            self.MyHash[place].append(key)

    def remove(self, key: int) -> None:
        place = self.HashFunc(key)
        if key in self.MyHash[place]:
            self.MyHash[place].remove(key)

    def contains(self, key: int) -> bool:
        place = self.HashFunc(key)
        if key in self.MyHash[place]:
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)