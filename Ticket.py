from abc import ABC, abstractmethod
from overrides import overrides
from Customer import Customer, CustomerType


class Ticket(ABC):
    #   Constructor
    def __init__(self, ticket_id: str, show_name: str, show_date: str, row: int, seat: int, customer: Customer, price: float):
        self.ticket_id = ticket_id
        self.show_name = show_name
        self.show_date = show_date
        self.row = row
        self.seat = seat
        self.customer = customer
        self.price = price

    @abstractmethod
    def calculate_price(self) -> float:
        pass

    def __str__(self) -> str:
        discount_str = f"{self.customer.discount:.2f}" if self.customer.discount is not None else "None"
        return (f"  Ticket Info:\n"
                f"    - Ticket ID: {self.ticket_id}\n"
                f"    - Show Name: {self.show_name}\n"
                f"    - Show Date: {self.show_date}\n"
                f"    - Row: {self.row}\n"
                f"    - Seat: {self.seat}\n"
                f"    - Price: ${self.price:.2f}\n")


class RegularTicket(Ticket):
    @overrides
    def calculate_price(self) -> float:
        return self.price


class VIPTicket(Ticket):
    def __init__(self, ticket_id: str, show_name: str, show_date: str, row: int, seat: int, customer: Customer, price: float):
        if customer.customer_type != CustomerType.VIP:
            raise ValueError("Customer is not VIP, cannot purchase VIP ticket.")
        super().__init__(ticket_id, show_name, show_date, row, seat, customer, price)

    @overrides
    def calculate_price(self) -> float:
        if self.customer.discount:
            return self.price - self.customer.discount
        return self.price
