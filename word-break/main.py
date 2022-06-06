def can_build_word(word , words , parts):
    for dict_word in words:
        if len(dict_word) > len(word):
            continue
        if word.startswith(dict_word):
            # we could use this dict_word as a part 
            rest = word[len(dict_word):]
            parts.append(dict_word)
            if len(rest) == 0:
                # we built the whole word
                return True
            if(can_build_word(rest , words, parts)):
               return True
            else:
              parts.remove(dict_word)
    return False

def main():
    words = ["leet" ,"co" ,"e" ,  "c" , "o" , "ode" , "tc"]
    word = "leetcode"
    parts = []
    if can_build_word(word , words , parts):
        print("can build with parts" , parts)
    else:
        print("cannot build")

if __name__ == "__main__":
    main()
