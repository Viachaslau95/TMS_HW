class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        if isinstance(args[0], str):
            self.hours, self.minutes, self.seconds = args[0].split(':')

    def __eq__(self, other):
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.hours != other.hours or self.minutes != other.minutes or self.seconds != other.seconds:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        if self.hours <= other.hours and self.minutes < other.minutes:
            return True
        if self.hours <= other.hours and self.minutes <= other.minutes and self.seconds < other.seconds:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        if self.hours >= other.hours and self.minutes > other.minutes:
            return True
        if self.hours >= other.hours and self.minutes >= other.minutes and self.seconds > other.seconds:
            return True
        else:
            return False

    def __le__(self, other):
        if self.hours < other.hours:
            return True
        if self.hours <= other.hours and self.minutes < other.minutes:
            return True
        if self.hours <= other.hours and self.minutes <= other.minutes and self.seconds < other.seconds:
            return True
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.hours > other.hours:
            return True
        if self.hours >= other.hours and self.minutes > other.minutes:
            return True
        if self.hours >= other.hours and self.minutes >= other.minutes and self.seconds > other.seconds:
            return True
        if self.hours == other.hours and self.minutes == other.minutes and self.seconds == other.seconds:
            return True
        else:
            return False


if __name__ == '__main__':
    mytime = MyTime('10:12:30')
    mytime2 = MyTime('10:12:30')
    print(mytime == mytime2)
    print(mytime != mytime2)
    print(mytime < mytime2)
    print(mytime > mytime2)
    print(mytime <= mytime2)
    print(mytime >= mytime2)
# test str