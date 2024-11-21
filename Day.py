class Day:
    def __init__(self, date: str, score: int):
        self.date = date
        self.score = score

    def __str__(self):
        return f"{self.date}: {self.score}"