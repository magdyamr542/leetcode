def group_anagrams(strs):
    strs_sorted = list(map(lambda word : "".join(sorted(word)) , strs))
    words = {}
    for i in range(len(strs)):
        word = strs[i]
        word_sorted = strs_sorted[i]
        if words.get(word_sorted , None):
            words[word_sorted].append(i)
        else:
            words[word_sorted] = [i]
        
        
    result = []
    for key , indexes in words.items():
        curr_words = []
        for index in indexes:
            curr_words.append(strs[index])
        result.append(curr_words)
        
    return result
        

#https://leetcode.com/problems/group-anagrams/
if __name__ == "__main__":
    words=  ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(words))
