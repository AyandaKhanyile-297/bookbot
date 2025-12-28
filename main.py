def word_count(paragraph):
    words = paragraph.split()
    return len(words)

def get_book_text(filepath):
    file_contents = ""
    
    with open(filepath) as file:
        file_contents = file.read()
        
    return file_contents
    
def main():
    book_path = "books/frankenstein.txt"
    story = get_book_text(book_path)
    num_words = word_count(story)
    print(f"Found {num_words} total words")
    
main()