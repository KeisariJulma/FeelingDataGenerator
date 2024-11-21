from faker import Faker
from Person import Person
from datetime import datetime, timedelta
import random

class FakeGenerator(Faker):
    def __init__(self, amount: int = 100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.amount = amount
        self.persons = self.gen_persons()

    def gen_persons(self) -> list[Person]:
        unique_names = set()
        while len(unique_names) < self.amount:
            firstname = self.first_name()
            surname = self.last_name()
            unique_names.add(Person(firstname, surname))
        return list(unique_names)

    def gen_year_data(self) -> dict:
        year_data = {}
        start_date = datetime(datetime.now().year, 1, 1)
        for i in range(365):
            date = start_date + timedelta(days=i)
            for person in self.persons:
                score = random.randint(0, 100)
                person.add_score(date.strftime('%Y-%m-%d'), score)
            year_data[date.strftime('%Y-%m-%d')] = self.persons
        return year_data