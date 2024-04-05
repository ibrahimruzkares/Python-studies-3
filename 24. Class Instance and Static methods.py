from datetime import date
class person:
    person_count = 0
    raise_ratio = 1.1

    def __init__(self,name,age):
        self.name = name
        self.age = age
        person.person_count += 1

    def show_info(self):                               #instance method
        return f"Name: {self.name} Age: {self.age}"

    @classmethod
    def show_person_count(cls):
        return cls.person_count

    @classmethod
    def create_with_string(cls, str_):
        name, age = str_.split("-")
        return cls(name, age)

    @classmethod
    def create_with_birthday(cls, name, birth_date):
        return cls(name, date.today().year - birth_date)

    @staticmethod
    def calculate_birthdate(person):
        return date.today().year - person.age

    @staticmethod
    def say_hi():                                      #static method bir parametre almak zorunda değil
        return "Merhaba"                               #class ve içerisindeki değişkenlerden bağımsız çalışır





person1 = person("John", 30)
person2 = person("Jack", 21)

person3 = person.create_with_string("Ayşe-25")
print(person3.show_info())

person4 = person.create_with_birthday("Mehmet",1994)
print(person.show_person_count())
print(person4.age)

print(person.calculate_birthdate(person1))
print(person.say_hi())