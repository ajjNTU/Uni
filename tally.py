class Tally:
    def __init__(self, upper_limit: int = 100):
        self.count = 0
        self.upper_limit = upper_limit
        print(f"Tally created starting at {self.count}, upper limit is {self.upper_limit}")

    def incBy(self, inc: int = 1):
        if self.count + inc <= self.upper_limit:
            self.count += inc
            print(f"Tally increased, it's now {self.count}")
        else:
            print(f"{self.count} + {inc} is greater than the {self.upper_limit}")

    def decBy(self, dec: int = 1):
        self.count -= dec
        print(f"Tally decreased, it's now {self.count}")

    def tally(self):
        print(f"Tally is {self.count}")
        return self.count


t = Tally()
t.incBy(10)
t.tally()
t.incBy()
t.tally()
t.decBy(20)
t.tally()
t.incBy(500)
t.tally()