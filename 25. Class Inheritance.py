class employee:

    raise_ratio = 1.1

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name + surname + "@gmail.com"

    def info(self):
        return "Name: {}  Surname: {}  Salary:  {}  Email:  {}".format(self.name, self.surname, self.salary, self.email)


employee1 = employee("Jack","Ryan",5000)
employee2 = employee("Mike","Ruee", 7000)

class developers(employee):                         #inheritance, bir üst class' ın fonksiyonlarını kullanabilir

    raise_ratio = 1.7

    def __init__(self, name, surname, salary, languages):
        super().__init__(name, surname, salary)    #çatı class' ın __init__ kısmını kopyaladık
        self. languages = languages

    def info(self):
        return f"Name: {self.name}, Surname: {self.surname}, Salary: {self.salary}, Email: {self.email}, Languages: {self.languages}"

    def lang_know(self):
        return f"Languages I know: {self.languages}"

developer1 = developers("Mehmet", "Rüzgar", 9000, "C++")
developer2 = developers("Ahmet","Tuzlu", 8000, "Python")


print(developer2.raise_ratio)
print(employee2.info())
print(developer1.info())


