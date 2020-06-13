class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.data = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.data.append(val)
            self.dict[val] = len(self.data)-1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            idx,last = self.dict[val], self.data[-1]
            self.data[idx], self.dict[last] = last, idx
            self.data.pop()
            self.dict.pop(val, 0)
            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()