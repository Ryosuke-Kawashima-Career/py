class Employee:
    def __new__(cls, id, name):
        print("Creating a new employee instance")
        # super().__new__(cls) does not take additional arguments
        return super().__new__(cls)

    def __init__(self, id, name):
        print("Initializing the employee instance")
        self.id = id
        self.name = name
    
    def __del__(self):
        # We don't need to manually delete attributes, Python's garbage collector handles it.
        print(f"Deleting the employee: {self.name}")


def solution():
    emp = Employee(1, "Alice")
    print(f"Employee Details - ID: {emp.id}, Name: {emp.name}")


if __name__ == "__main__":
    solution()
