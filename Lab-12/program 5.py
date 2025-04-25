class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def add(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) + \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def subtract(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) - \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        if total_seconds < 0:
            total_seconds += 24 * 3600
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def multiply(self, factor):
        total_seconds = (self.hours * 3600 + self.minutes *
                         60 + self.seconds) * factor
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def divide(self, divisor):
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        total_seconds = (self.hours * 3600 + self.minutes *
                         60 + self.seconds) // divisor
        return Time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

time1 = Time(2, 30, 45)
time2 = Time(1, 15, 20)
print("Time 1:", time1)
print("Time 2:", time2)
print("Addition:", time1.add(time2))
print("Subtraction:", time1.subtract(time2))
print("Multiplication by 2:", time1.multiply(2))
print("Division by 2:", time1.divide(2))
print("Time 1 in seconds:", time1.to_seconds())
print("Time 2 in seconds:", time2.to_seconds())
