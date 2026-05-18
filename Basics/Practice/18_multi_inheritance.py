class Teacher:
    def __init__(self, name):
        self.name = name
    def teach(self):
        print(f"{self.name} is teaching")

class YouTuber:
    def __init__(self, account):
        self.account = account
    def make_videos(self):
        print(f"{self.account} is making videos")

class Student(Teacher, YouTuber):
    def __init__(self, name, channel):
        Teacher.__init__(self, name)
        YouTuber.__init__(self, channel)


def main():
    student = Student("John Doe", "JohnTube")
    student.teach()
    student.make_videos()

if __name__ == "__main__":
    main()

