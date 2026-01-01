def word_count(paragraph):
    words = paragraph.split()
    return len(words)

def character_count(paragraph):
    dictionary = {}
    book = paragraph.split()
    
    for word in book:
        word = word.lower()
        
        for character in word:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1

    return dictionary
    
