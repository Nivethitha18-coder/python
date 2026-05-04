def replace(sentence, lookup):
        words = sentence.split()
        new_words = [lookup.get(word, word) for word in words]
        return " ".join(new_words)
a=input("Enter a sentence")
lookup={}
n=int(input("Enter a number of words to be replaced"))
for i in range(n):
    b=input("enter a word in a sentence to be replaced")
    d=input("enter word to be replaced in the sentence")
    lookup[b]=d
c=lookup
print(c)
r= replace(a,c)
print(r)