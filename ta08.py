class Time:
    def __init__(self) -> None:
        self._seconds_since_midnight:int = 0

    @property
    def hours(self) -> int:
        return self._seconds_since_midnight / (60 * 60)

    @hours.setter
    def hours(self, hours:int):
        if(hours > 23): self._seconds_since_midnight += 23 * 60 * 60
        elif(hours < 0): self._seconds_since_midnight += 0
        else: self._seconds_since_midnight += hours * 60 * 60

    @property
    def minutes(self) -> int:
        return (self._seconds_since_midnight / 60) % 60

    @minutes.setter
    def minutes(self, minutes:int):
        if minutes > 59: self._seconds_since_midnight += 59 * 60
        elif minutes < 0: self._seconds_since_midnight += 0
        else: self._seconds_since_midnight += minutes * 60

    @property
    def seconds(self) -> int:
        return ((self._seconds_since_midnight % 60 ) % 60)

    @seconds.setter
    def seconds(self, seconds:int):
        if seconds > 59: self._seconds_since_midnight += 59
        elif seconds < 0: self._seconds_since_midnight += 0
        else: self._seconds_since_midnight += seconds

    @property
    def hours_simple(self) -> int:
        if self._seconds_since_midnight / (60 * 60) < 1: return 12
        if (self._seconds_since_midnight / (60 * 60)) >= 13: return self._seconds_since_midnight / (60 * 60) - 12
        return self._seconds_since_midnight / (60 * 60)

    @property
    def period(self) -> str:
        if self._seconds_since_midnight >= (12 * 60 * 60): return "PM"
        return "AM"

def main():
    time = Time()

    time.hours = int(input("Hours: "))
    time.minutes = int(input("Minutes: "))
    time.seconds = int(input("Seconds: "))

    # print(("Hours: %i | Minutes: %i | Seconds: %i") % (time.hours_simple, time.minutes, time.seconds))

    print(("%i:%02i:%02i %s") % (time.hours_simple, time.minutes, time.seconds, time.period))

if __name__ == "__main__":
    main()
