# Person.py
from Day import Day

class Person:
    def __init__(self, firstname: str, surname: str):
        self.name = firstname
        self.surname = surname
        self.days = []

    def add_score(self, date: str, score: int):
        self.days.append(Day(date, score))

    def get_score(self, date: str) -> int:
        for day in self.days:
            if day.date == date:
                return day.score
        return 0

    def __str__(self):
        days_str = ', '.join(str(day) for day in self.days)
        return f"{self.name} {self.surname}: {days_str}"