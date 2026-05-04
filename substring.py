s = input("Enter a string: ")

print("All substrings are:")
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])