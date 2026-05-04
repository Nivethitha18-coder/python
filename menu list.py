list1 = []
list2 = []
b=int(input("Enter no of elements in list1: "))
print("enter the elements")
for i in range(b):
    list1.append(input())
c=int(input("Enter no of elements in list2: "))
print("enter the elements")
for i in range(c):
    list2.append(input())
while True:
    print("\nMENU")
    print("1. Add element at specified position")
    print("2. Add element at last")
    print("3. Compare two lists")
    print("4. Print id of all elements")
    print("5. Find first occurrence of an item")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        pos = int(input("Enter position: "))
        element = input("Enter element: ")
        list1.insert(pos, element)
        print("Updated list:", list1)

    elif choice == 2:
        element = input("Enter element to add: ")
        list1.append(element)
        print("Updated list:", list1)

    elif choice == 3:
        print("Is list1 = list2 ", list1 == list2)
        print("Is list1 = list2 ", list1 != list2)
        print("Is list1>list2 ",list1>list2)
        print("Is List1<list2 ",list1<list2)

    elif choice == 4:
        print("ID of elements:")
        for i in list1:
            print(i, ":", id(i))

    elif choice == 5:
        item = input("Enter item to search: ")
        if item in list1:
            print("First occurrence at index:", list1.index(item))
        else:
            print("Item not found")

    elif choice == 6:
        print("Program ended")
        break

    else:
        print("Invalid choice")
