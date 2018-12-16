# to make a method of a class, you just move the function into
# the class! now you can invoke the function using dot notation

class Time:
    def printTime(time):
        print(str(time.hours) + ":" + \
        str(time.minutes) + ":" + \
        str(time.seconds))

currentTime = Time()
currentTime.hours = 9
currentTime.minutes = 14
currentTime.seconds = 30
currentTime.printTime()