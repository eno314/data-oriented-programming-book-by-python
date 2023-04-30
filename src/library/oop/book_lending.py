from datetime import date


class BookLending:
    id: str
    lending_date: date
    due_date: date

    def is_late(self) -> bool:
        pass

    def return_book(self) -> bool:
        pass
