class employee:
   def __init__(self, name, surname, age):
      self.name = name
      self.surname = surname
      self.age = age

   def show_info(self):
      print(f"Name: {self.name}, Surname: {self.surname}, Age: {self.age}")


employee1 = employee("Jack", "Russell", 30)
employee2 = employee("Jones", "Mursk", age = 23)


employee1.show_info()
