sentence = 'Hello my name is Varun Khanna. Hello my name is Aryan Dhingra. Hello my name is Anya Dhingra. '
import re
def word_extraction(sentences ):
    words = re.sub('[^\w]', " ", sentence).split()
    ignore_words = ["a", "an", "the", "and","to","am" , "I", "but", "is"]
    cleaned_text = [w.lower() for w in words if w not in ignore_words]
    return cleaned_text

def tokenize(sentences):    
    words = []    
    for sentence in sentences:        
        w = word_extraction(sentences = sentence )        
        words.extend(w)            
    words = sorted(list(set(words)))    
    return words

def bag_of_words(sentences):
    words_my_hash= {}
    ignore_words = ["a", "an", "the", "and","to","am" , "I", "but", "is"]
    for c in sentences.lower().split():
        if c not in ignore_words:
            words_my_hash[c] = 1 + words_my_hash.get(c, 0)
    return words_my_hash

print(bag_of_words(sentences=sentence))

# print(sentence.lower().split())
