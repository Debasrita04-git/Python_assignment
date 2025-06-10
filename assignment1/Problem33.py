#Count words in a sentence.
def count_words(sentence):
    words = sentence.split()
    return len(words)

#Example Usage
print(count_words("This is a sample sentence."))  # Output: 5
