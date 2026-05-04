sentence = input("Enter the sentence: ")
n = int(input("Enter number of dictionary entries: "))
lookup = {}
for i in range(n):
    key = input("Enter word to replace: ")
    value = input("Enter replacement word: ")
    lookup[key] = value
words = sentence.split()
new_words = []
for w in words:
    word = w.strip(".,!?")

    if word in lookup:
        replaced = lookup[word]

        # keep punctuation if present
        if w.endswith('.'):
            replaced += '.'
        new_words.append(replaced)
    else:
        new_words.append(w)
result = " ".join(new_words)

print("Output:", result)