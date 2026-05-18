def calculate_area(shape: str = "triangle"):
    base = float(input("Enter triangle base: "))
    height = float(input("Enter triangle height: "))
    area = base * height if shape == "rectangle" else 0.5*base*height

    print(f"Area of the triangle is: {area}")
    return area

def print_shape():
    num = int(input("Enter a number"))
    for cur in range(1, num+1):
        for iteration in range(cur):
            print("*", end="")
        print("\n")
        

if __name__ == "__main__":
    calculate_area()
    print_shape()