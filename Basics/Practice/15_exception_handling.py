def solution(grade: int):
    try:
        if 90 <= grade and grade < 100:
            print("A")
        elif 80 <= grade and grade < 90:
            print("B")
        elif 70 <= grade and grade < 80:
            print("C")
        elif 60 <= grade and grade < 70:
            print("D")
        elif 0 <= grade and grade < 60:
            print("F")
        else:
            raise ValueError("Grade must be between 0 and 100")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print("Thank you for using the Grade Calculator. Goodbye!")

def solution2():
    try:
        grade = int(input("Enter your grade: "))
        if grade < 0 or grade > 100:
            raise ValueError
    except ValueError:
        print("Please enter a valid number(0 ~ 100)")
    else:
        print(grade)
    finally:
        print("Thank you for using the Grade Calculator. Goodbye!")

if __name__ == "__main__":
    solution2()