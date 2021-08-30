some_string = input().split()
even_words = [words for words in some_string if len(words) % 2 == 0]

print('\n'.join(even_words))