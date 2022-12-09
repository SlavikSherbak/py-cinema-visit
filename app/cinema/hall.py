from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(
            self,
            movie_name: str,
            customers: list,
            cleaning_staff: Cleaner
    ) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            if isinstance(customer, Customer):
                customer.watch_movie(movie_name=movie_name)
            else:
                customer = Customer(
                    name=customer["name"],
                    food=customer["food"]
                )
                customer.watch_movie(movie_name=movie_name)
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(hall_number=self.number)
