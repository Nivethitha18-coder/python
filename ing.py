s = input("Enter a string: ")

if len(s) < 3:
    result = s
elif s.endswith("ing"):
    result = s + "ly"
else:
    result = s + "ing"

print("Result:", result)