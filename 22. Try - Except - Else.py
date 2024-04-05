try:
    a = 5
    b = 2
    if b == 0:
        raise ZeroDivisionError
    c = a / b
    x = 6
    d = x
    name = "Jack"
    char = name[0]
except ZeroDivisionError:
    print("denominator cannot be 0.")
except NameError:
    print("name is not defined.")
except IndexError:
    print("string is out of range.")
except Exception:
    print("An unknown error occured.")

else:
    print("Else block is working.")
    print(c)
    print(char)

finally:
    print("Finally block is working.")