print("TO CHECK FOR ANAGRAM")
s1=input("enter first string")
s2=input("enter second string")

s1=s1.replace(" ","").lower()
s2=s2.replace(" ","").lower()

if sorted(s1)==sorted(s2):
    print("the string is anagram")
else:
    print("the string is not anagram")
