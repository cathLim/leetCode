#https://neetcode.io/problems/dynamicArray
class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.dynamicArr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.dynamicArr[i]

    def insert(self, i: int, n: int) -> None:
        self.dynamicArr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.dynamicArr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.dynamicArr[self.length]
 
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_dynamicArr = [0] * self.capacity

        for i in range(self.length):
            new_dynamicArr[i] = self.dynamicArr[i]
        self.dynamicArr = new_dynamicArr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity
