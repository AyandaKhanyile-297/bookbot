import sys
from stats import word_count, character_count, dictionary_format

def get_book_text(filepath):
    file_contents = ""
    
    with open(filepath) as file:
        file_contents = file.read()
        
    return file_contents

def display_info(bookname, total_words, story):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookname}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    display_story(story)

def display_story(data):
    for dictionary in data:
        chrctr = dictionary["char"]
        cnt = dictionary["num"]
        print(f"{chrctr}: {cnt}")
    
def main():
    book_path = sys.argv[1]
    story = get_book_text(book_path)
    num_words = word_count(story)
    num_characters = character_count(story)
    character_list = dictionary_format(num_characters) 
    display_info(book_path, num_words, character_list)
    
main()