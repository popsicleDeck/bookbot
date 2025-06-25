from stats import words_counter
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
def main():
    text = get_book_text('books/frankenstein.txt').split()
    print(f"{words_counter(text)} words found in the document")
main()



