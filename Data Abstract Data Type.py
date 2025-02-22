class date:
    def __init__ (self,a,b,c):
        self.d = a
        self.m = b
        self.y = c
    def day(selfself):
        print("day = ",self.d)
    def month(selfself):
        print("month = ",self.m)
        def year(self):
            print("year = ",self.y)
    def monthName(selfself):
        months = ["unknown", "January", "Febuary", "March", "April", "May","June","July", "August", "September","October", "November", "December"]
        print("Month Name:",months[self.m])
    def isLeapYear(selfself):
        if (self.y % 400 == 0)and (self.y % 100 == 0):
            print("It is a leap Year")
        elif (self.y % 4 == 0) and (self.y % 100 != 0):
            print("It is a Leap year")
        else:
            print("It is not a leap year")
d1 = date(3,8,2000)
d1.day()
d1.month()
d1.year()
d1.monthName()
d1.isLeapYear()
