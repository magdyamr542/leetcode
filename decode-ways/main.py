def numDecodings(s: str) -> int:
    if len(s) == 0:
        return 0
    
    if len(s) == 1:
        return 0 if s[0] == '0' else 1

    cache = {}
        
    def get_num_decoding(curr_word):
        if cache.get(curr_word , None):
            return cache.get(curr_word)

        length = len(curr_word)
        if length == 0:
            return 1 # we have built a combination
        elif len(curr_word) == 1:
            return 0 if curr_word[0] == '0' else 1
        
        using_first_char =  get_num_decoding(curr_word[1:]) if curr_word[0] != '0' else 0
        using_first_two_chars =   get_num_decoding(curr_word[2:]) if curr_word[0] != '0' and int(curr_word[0:2]) <= 26 else 0

        cache[curr_word] =  using_first_char + using_first_two_chars
        
        return using_first_char + using_first_two_chars
        
    return get_num_decoding(s)
        
    

if __name__ == "__main__":
    print(numDecodings("122"))


    
