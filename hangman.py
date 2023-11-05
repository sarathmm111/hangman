import random

def get_random_word(wordlist="/usr/share/dict/words"):
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.isalpha(): # if there is punctuation
                continue
            if not word.islower(): # if it is a proper noun
                continue
            if len(word) < 5: # Too short
                continue
            good_words.append(word)

        return random.choice(good_words)
        
def get_mask_word(word, guesses):
    """Returns the provided word with all
    letters except the ones in guesses replaced by -"""
    ret = []
    for i in word:
        if i in guesses:
            ret.append(i)
        else:
            ret.append("-")
    return "".join(ret)
