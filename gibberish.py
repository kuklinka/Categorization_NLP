import random

def gen_gibberish(word, char_set, thresh=0.4):
    times = int(random.randrange(1,len(word)) * thresh)
    '''
    Types of replacement:
        1.Delete random character.
        2.Add random character.
        3.Replace a character.
        4.Combination?
    '''
    while times!=0:
        # try to gen noise length times...
        times-=1
        val = random.randrange(0,10)
        if val <= 5:
            #get random index
            val = random.randrange(0,10)
            index = random.randrange(0,len(word))
            if val <= 3 :
                # delete character
                word = word[:index]+word[index+1:]
            else:
                # add character
                insert_index = random.randrange(0,len(char_set))
                word = word[:index] + char_set[insert_index] + word[index:]
        else:
            index = random.randrange(0,len(char_set))
            replace_index = random.randrange(2,len(word))
            word = word[:replace_index] + char_set[index] + word[replace_index+1:]
    
    return word

