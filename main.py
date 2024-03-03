def count_letters(in_file):
    word_count = 0
    letter_count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    for word in in_file.split(" "):
        for rune in list(word):
            if rune in letter_count:
                letter_count[rune.lower()] += 1
        if word.isalpha():
            word_count += 1
    return letter_count


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        book_letter_count = count_letters(file_contents)
        book_lc_sorted = {k: v for k, v in sorted(
            book_letter_count.items(), key=lambda item: item[1], reverse=True)}
        for key in book_lc_sorted:
            print(f"The '{key}' was found {book_lc_sorted[key]} times")


main()
