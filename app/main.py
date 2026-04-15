#from app.cinema.bar import CinemaBar
from cinema import bar

# write your imports here


def cinema_visit(customers: list, hall_number: int, cleaner: str, movie: str):
    for customer in customers:
        CinemaBar.sell_product(customer.name, customer.food)
