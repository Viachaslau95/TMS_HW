class MyTime:
    def __init__(self, *args):
        if isinstance(args[0], str):
            self.hours, self.minutes, self.seconds = args[0].split(':')
        elif len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False

    def __add__(self, other):
        sum_hours = self.hours + other.hours
        sum_minutes = self.minutes + other.minutes
        sum_seconds = self.seconds + other.seconds
        return MyTime(sum_hours, sum_minutes, sum_seconds)

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def __sub__(self, other):
        sub_hours = self.hours - other.hours
        sub_minutes = self.minutes - other.minutes
        sub_seconds = self.seconds - other.seconds
        return MyTime(sub_hours, sub_minutes, sub_seconds)

if __name__ == "__main__":
    mytime = MyTime(11, 30, 32)
    mytime2 = MyTime(11, 32, 21)
    print(mytime == mytime2)
    print(mytime + mytime2)
    print(mytime - mytime2)
    print(mytime)
