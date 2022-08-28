class WordDictionary:

    def __init__(self):
        self.children = {} # maps a letter between 'a-z' to a Trie node
        self.isWord = False
        


    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.isWord = True
            return
        
        if self.children.get(word[0] , None):
            return self.children.get(word[0]).addWord(word[1:])
        else:
            self.children[word[0]] = WordDictionary()
            self.children[word[0]].addWord(word[1:])
            
            
    def search(self, word: str) -> bool:
        return self.doSearch(word)
        
        
    def doSearch(self, word: str) -> bool:
        if len(word) == 0:
            return self.isWord
        
        if word[0] == ".":
            for node in self.children.values():
                found = node.doSearch(word[1:])
                if found:
                    return True
        else:
            if self.children.get(word[0] , None):
                return self.children.get(word[0]).doSearch(word[1:]) 
            else:
                return False
        
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
            
        
        
                
                
# https://leetcode.com/problems/design-add-and-search-words-data-structure/submissions/
if __name__ == "__main__":
    pass


    
