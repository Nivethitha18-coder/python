class ExceptionDemo:

    def divide(self):
        try:
            a = int(input("Enter numerator: "))
            b = int(input("Enter denominator: "))
            result = a / b
            print("Result:", result)

        except ZeroDivisionError:
            print("Error: Divide by zero error occurred.")

        except ValueError:
            print("Error: Input not in specified data type (integer required).")

    def access_list(self):
        try:
            lst = [10, 20, 30, 40, 50]
            print("List:", lst)
            index = int(input("Enter index to access element: "))
            print("Element at index", index, "is", lst[index])

        except IndexError:
            print("Error: Index greater than length of list.")

        except ValueError:
            print("Error: Please enter a valid integer index.")

    def access_dict(self):
        try:
            d = {"a": 1, "b": 2, "c": 3}
            print("Dictionary:", d)
            key = input("Enter key to access value: ")
            print("Value for key", key, "is", d[key])

        except KeyError:
            print("Error: Key not found in dictionary.")


# Main program
if __name__ == "__main__":
    obj = ExceptionDemo()

    print("\n--- Division Operation ---")
    obj.divide()

    print("\n--- List Access Operation ---")
    obj.access_list()

    print("\n--- Dictionary Access Operation ---")
    obj.access_dict()
