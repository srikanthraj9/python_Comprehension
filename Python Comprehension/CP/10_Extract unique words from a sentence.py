sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()

# Unique words
unique_words = {w for w in words}
print(unique_words)
# {'the', 'quick', 'brown', 'fox', 'jumps', 'over', 'lazy', 'dog'}
