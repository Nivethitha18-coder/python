s = input("Enter the string in the format letter no.of times to be repeated another letter: ")

result=""
i = 0

while i < len(s):
        char=s[i] #letter
        num = int(s[i+1]) # number after the letter
        result += char * num
        i += 2

print(result)