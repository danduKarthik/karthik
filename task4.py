def word_frequency():
    text = input("Enter a string: ")
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

if __name__ == "__main__":
    frequencies = word_frequency()
    print("word frequencies:",frequencies)