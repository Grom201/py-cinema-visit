from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer

# write your imports here


def cinema_visit(customers: list[Customer],
                 hall_number: int,
                 cleaner: Cleaner,
                 movie: str) -> None:
    customer_objects = []
    for customer in customers:
        cust = Customer(customer["name"], customer["food"])
        CinemaBar.sell_product(cust, cust.food)
        customer_objects.append(cust)
    hall = CinemaHall(hall_number)
    cleaner = Cleaner(cleaner)
    hall.movie_session(movie_name=movie,
                       customers=customer_objects,
                       cleaning_staff=cleaner)
