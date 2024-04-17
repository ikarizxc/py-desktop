from datetime import datetime

class Competitor:
    def __init__(self, number, name, surname):
        self.number = number
        self.name = name
        self.surname = surname
        self.result = datetime.strptime("00:00:00,000000", '%H:%M:%S,%f')
        self.position = 0

    def __str__(self) -> str:
        return f"№{self.number} : {self.surname} {self.name}\nResult: {self.result.minute:02}:{self.result.second:02},{self.result.microsecond:06}"