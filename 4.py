s=input("Enter a string: ")
v=""
for ch in s:
    if ch not in v:
        co=0
        for c in s:
            if ch == c:
                co+=1
        print(ch,":",co)
        v+=ch
