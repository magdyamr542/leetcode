from typing import Dict, List, Optional

chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]

def buildTrie(words : List[str]) -> 'Trie':
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie

class Trie:

    def __init__(self):
        self.children : Dict[str , Trie] = {} # maps a letter between 'a-z' to a Trie node
        self.isWord = False


    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.isWord = True
            return
        
        if self.children.get(word[0] , None):
            return self.children[word[0]].insert(word[1:])
        else:
            self.children[word[0]] = Trie()
            self.children[word[0]].insert(word[1:])
            
            

    def getTrieNodeByPrefix(self, prefix: str) -> Optional['Trie']:
        if len(prefix) == 0:
            return self

        if self.children.get(prefix[0] , None):
            return self.children[prefix[0]].getTrieNodeByPrefix(prefix[1:])
        else:
            return None


    # get all words accessible by this node
    def getWords(self , currWord : str ,  result : List[str] , maxResults : int):
        if len(result) == maxResults:
            return # done

        if self.isWord:
            result.append(currWord)

        for char in chars:
            if self.children.get(char , None):
                self.children[char].getWords(currWord + char , result , maxResults)




        
        
    def search(self, prefix: str , maxResults : int) -> List[str]:
        node = self.getTrieNodeByPrefix(prefix)
        if not node:
            return []

        result : List[str] = []
        node.getWords(prefix , result , maxResults)
        return result
        


        

# https://leetcode.com/problems/search-suggestions-system/submissions/
def main():
    words = ["bags","baggage","banner","box","cloths"]
    searchWord = "bags"
    result : List[List[str]] = []
    trie = buildTrie(words)
    for i in range(len(searchWord)):
        currPrefix = searchWord[:i + 1]
        result.append(trie.search(currPrefix , 3))
    print(result)

if __name__ == "__main__":
    main()

