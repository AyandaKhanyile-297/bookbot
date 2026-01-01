from stats import word_count, character_count

def get_book_text(filepath):
    file_contents = ""
    
    with open(filepath) as file:
        file_contents = file.read()
        
    return file_contents

def display_info(story):
    print(story)

    
def main():
    book_path = "books/frankenstein.txt"
    story = get_book_text(book_path)
    num_words = word_count(story)
    print(f"Found {num_words} total words")
    num_characters = character_count(story)
    display_info(num_characters)
    
main()