# CHAR INDEXING
def get_char_indexing(char_set):
    char2int = { char_set[x]:x for x in range(len(char_set)) }
    int2char = { char2int[x]:x for x in char_set }
    return char2int, int2char

