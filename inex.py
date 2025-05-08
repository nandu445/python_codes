class Animal:
    def hello(self):
        print("Some sound")

class Cat(Animal):
    def sound(self):
        print("Meow")

c1=Animal()
c1.hello()


c = Cat()
c.sound() 
c.hello()