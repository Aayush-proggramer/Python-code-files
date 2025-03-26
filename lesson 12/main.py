#cat
class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("My name is", self.name, "and my age is", self.age)

    def make_sound(self):
        print("the cat meows")

#dog
class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age  
    def info(self):
        print("My name is", self.name, "and my age is", self.age)

    def make_sound(self):
        print("the dog barks")

#object creation
c1 = cat("tom", 2)
c1.info()
c1.make_sound()
d1 = dog("sky", 2)
d1.info()
d1.make_sound()