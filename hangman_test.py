import os

import hangman

def test_random_word_lowercase():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["Grape\n", "apple\n", "Mango\n"])
        
    for _ in range(100):
        assert hangman.get_random_word(fname) == "apple"

    os.unlink(fname)

def test_random_word_no_punctuation():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "mango's\n", '"beryl"'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"

    os.unlink(fname)

def test_random_word_min_length_5():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "ape\n", 'dog\n', 'bear\n'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"
        
    os.unlink(fname)

def test_random_word_no_repeated_words():
    words = {hangman.get_random_word() for _ in range(10)}
    assert len(words) == 10
    
def test_mask_word_no_guesses():
    guesses = []
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "--------"
    
def test_mask_word_single_wrong_guess():
    guesses = ['x']
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "--------"

def test_mask_word_single_correct_guess():
    guesses = ['t']
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "-------t"

def test_mask_word_two_correct_guesses():
    guesses = ['p','t']
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "---p---t"

def test_mask_word_single_guess_multiple_occurrence():
    guesses = ['e', 'p','t']
    word = "elephant"
    masked_word = hangman.get_mask_word(word, guesses)
    assert masked_word == "e-ep---t"

