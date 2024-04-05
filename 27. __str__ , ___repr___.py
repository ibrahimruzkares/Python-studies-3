class player:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Age: {self.age} "

    def __repr__(self):
        return "If there is no __str__ function, then __repr__ will work."


player1 = player("Mikhael","Johnson", 25)
print(player1)
# print(player1.__repr__())
