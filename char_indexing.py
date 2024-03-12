# char indexing
def get_char_indexing(char_set):
    char2int = { char_set[x]:x for x in range(len(char_set)) }
    int2char = { char2int[x]:x for x in char_set }
    return char2int, int2char

# convert a word into integers
def convert_word_to_int(word, char_set, char2int):
    converted_word = []
    for char in word:
        if char.lower() in char_set:
            converted_word.append(char2int[char.lower()])
    return converted_word
    
# deconvert integers into a word
def deconvert_integers_to_word(integers, int2char):
    deconverted_word = []
    for integer in integers:
        if integer != 0:
            deconverted_word.append(int2char[integer])
    return deconverted_word