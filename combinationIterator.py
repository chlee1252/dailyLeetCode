class CombinationIterator:
    
    def gen_all(self, combinationLength, chars, i, accu, res):
        if len(accu) == combinationLength:
            res.append("".join(accu))
            return
        
        if i == len(chars):
            return
        else:
            self.gen_all(combinationLength, chars, i + 1, accu + [chars[i]], res)
            self.gen_all(combinationLength, chars, i + 1, accu, res)

    def __init__(self, characters: str, combinationLength: int):
        characters = list(characters)
        self.all_comb = []
        self.gen_all(combinationLength, characters, 0, [], self.all_comb)
        self.curr = -1

    def next(self) -> str:
        self.curr = self.curr + 1
        return self.all_comb[self.curr]

    def hasNext(self) -> bool:
        return self.curr != len(self.all_comb) - 1
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()