class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

class Dog(Animal):
    def __init__(self, habitat, name):
        super().__init__(habitat)
        self.name = name
    
    def __new__(cls, habitat, name):
        instance = super(Dog, cls).__new__(cls)
        print("dog created")
        return instance
    
def solution():
    d = Dog("indoors", "buddy")

if __name__ == "__main__":
    solution()

