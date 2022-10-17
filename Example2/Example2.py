def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("The number must be integer")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Enter the number: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Product of numbers from 1 to {num}:  {list}")    