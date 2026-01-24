# Parent class
class Parent:
    def __init__(self, name):
        self.name = name


    def show_name(self):
        print("Parent name:", self.name)

# Child class extends Parent
class Child():
    def __init__(self,name,dob, age):
        # Call Parent's constructor using super()
        super().__init__(name)
        self.age = age

    def show_details(self):
        print("Child name:", self.name, "Age:", self.age)

# Usage
c = Child("Swapnil", 25)
c.show_name()      # inherited from Parent
c.show_details()   # defined in Child