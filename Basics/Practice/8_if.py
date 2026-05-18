def solution():
    india = ["mumbai", "banglore", "chennai", "delhi"]
    pakistan = ["lahore","karachi","islamabad"]
    bangladesh = ["dhaka", "khulna", "rangpur"]

    city = input("Enter your city: ")
    try:
        if city in india:
            print("This city belongs to India")
        elif city in pakistan:
            print("This city belongs to Pakistan")
        elif city in bangladesh:
            print("This city belongs to Bangladesh")
    except:
        print("Please enter a valid city name")

def solution2():
    sugar_level = input("Enter your sugar level: ")
    if sugar_level < 80:
        print("Sugar is low")
    elif sugar_level > 100:
        print("Sugar is high")
    else:
        print("Sugar is normal")

solution()