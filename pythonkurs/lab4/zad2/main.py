def find_word_with_most_letters(file_path, letters):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()

    max_count = 0
    max_word = ""
    for word in words:
        count = sum(1 for letter in word if letter in letters)
        if count > max_count:
            max_count = count
            max_word = word

    return max_word, max_count


def main():
    file_path = "text.txt"
    letters_to_find = "абвгди"

    result, count = find_word_with_most_letters(file_path, letters_to_find)
    print(f"Слово с наибольшим количеством букв из '{letters_to_find}': {result}")
    print(count)


if __name__ == "__main__":
    main()

