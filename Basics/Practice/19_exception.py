class AdultException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_minor_age(self):
        if int(self.age) >= 18:
            print("You are a major.")
        else:
            raise AdultException("You are a minor.")

def main():
    age = input("Please enter your age:")
    user = Person("John", age)
    try:
        user.get_minor_age()
    except AdultException as e:
        print(e.message)
    finally:
        print("Execution finished")

if __name__ == '__main__':
    main()
