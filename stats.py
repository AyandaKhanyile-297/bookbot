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
    
def dictionary_format(dictionary):
    formatted = []
    
    for character in dictionary:
        singular = {"char":character, "num":dictionary[character]}
        formatted.append(singular)
    
    formatted.sort(reverse=True, key=sort_on)
    return formatted
    
def sort_on(items):
    return items["num"]    