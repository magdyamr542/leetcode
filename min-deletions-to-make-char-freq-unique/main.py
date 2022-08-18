def minDeletions(s: str) -> int:
    # build maps
    char_to_freq_map = {}
    for char in s:
        if char_to_freq_map.get(char , None):
            char_to_freq_map[char] = char_to_freq_map[char] + 1
        else:
            char_to_freq_map[char] = 1
            
        
    freq_to_char_map = {}
    for char , freq in char_to_freq_map.items():
        if freq_to_char_map.get(freq , None):
            freq_to_char_map[freq].append(char)
        else:
            freq_to_char_map[freq] = [char]
    
    result = 0
    frequencies = list(freq_to_char_map.keys())
    frequencies.sort()
    currFreq = frequencies[len(frequencies) - 1]
    while currFreq > 0:
        theCurrFreq = currFreq
        currFreq -= 1
        chars = freq_to_char_map.get(theCurrFreq , None)
        if not chars:
            continue
            
        if len(chars) < 2:
            continue
            
        result += len(chars) - 1
        for char_to_move in chars[1:]:
            if freq_to_char_map.get(theCurrFreq - 1 , None):
                freq_to_char_map[theCurrFreq - 1].append(char_to_move)
            else:
                freq_to_char_map[theCurrFreq - 1] = [char_to_move]
            
    
    return result

# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
def main():
    s = "aaabb"
    res = minDeletions(s) 
    print(f"result for {s} is {res}")

if __name__ == "__main__":
    main()
