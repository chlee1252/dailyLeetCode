class Trie:
  def __init__(self):
    self.tree = {}
  
  def insert(self, word: str) -> None:
    t = self.tree
    for char in word:
      if char not in t:
        t[char] = {}
      t = t[char]
    
    t['-'] = '-'
  
  def search(self, word: str) -> bool:
    t = self.tree
    for char in word:
      if char not in t:
        return False
      t = t[char]
    return '-' in t
  
  def startsWith(self, prefix: str) -> bool:
    t = self.tree
    for char in prefix:
      if char not in t:
        return False
      t = t[char]
    
    return True