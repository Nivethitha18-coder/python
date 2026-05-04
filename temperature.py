print("-------------MENU-------------")
print("TEMPERATURE->WARM OR COLD")
print("HUMIDITY->DRY OR HUMID")
print("-------------------------------")
a=input("enter temperature")
b=input("enter humidity")
if a=="warm":
    if b=="dry":
        print("PLAY BASKET BALL")
    elif b=="humid":
        print("PLAY TENNIS")
    else:
        print("invalid input")
elif a=="cold":
    if b=="dry":
        print("PLAY CRICKET")
    elif b=="humid":
        print("PLAY SWIM")
    else:
        print("invalid input")
else:
    print("invalid input")