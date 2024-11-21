from FakeGenerator import FakeGenerator

if __name__ == '__main__':
    fake = FakeGenerator()
    year_data = fake.gen_year_data()

    for date, persons in year_data.items():
        for person in persons:
            score = person.get_score(date)
            print(f"  {person}: {score} :: {date}")