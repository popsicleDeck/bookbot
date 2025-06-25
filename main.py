from stats import words_counter, char_counter, sort_list
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
def main():
     text = get_book_text('books/frankenstein.txt')
     print(f"Found {words_counter(text.split())} total words")
     num_char = char_counter(get_book_text('books/frankenstein.txt'))
     
     sort_ = sort_list(num_char)
     for i in sort_:
        print(f"{i['char']}: {i['num']}")

main()
