def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    counts = count_letters(text)
    sortedCounts = sort_counts(counts)
    for key, value in sortedCounts:
        print(f"The \'{key}\' character was found {value} times")
    print("--- End report ---")
    return

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    textL = text.lower()
    textList = list(set(textL))
    counts = {}
    for char in textList:
        if char.isalpha():
            counts.update({char: textL.count(char)})
        else:
            continue
    return counts
    
def sort_counts(counts):
    listCounts = list(counts.items())
    listCounts.sort(key = lambda x: x[1], reverse = True)
    return listCounts
main()
