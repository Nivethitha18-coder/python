directory = {}
n = int(input("Enter number of contacts: "))

for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    directory[name] = phone

print(directory)

print("\nTelephone Directory:")
for name, phone in directory.items():
    print(name, ":", phone)