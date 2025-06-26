from stats import words_counter, char_counter, sort_list
import sys
def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print(f"Found {words_counter(text.split())} total words")
    num_char = char_counter(get_book_text(sys.argv[1]))
     
    sort_ = sort_list(num_char)
    for i in sort_:
        print(f"{i['char']}: {i['num']}")

main()
