from Ticket import Ticket, VIPTicket


class Show:
    #   Constructor

    def __init__(self, show_id: str, show_name: str, show_date: str):
        self.show_id = show_id
        self.show_name = show_name
        self.show_date = show_date
        self.tickets = []

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)

    def remove_ticket(self, ticket_id: str):
        self.tickets = [ticket for ticket in self.tickets if ticket.ticket_id != ticket_id]

    def calculate_revenue(self) -> float:
        return sum(ticket.calculate_price() for ticket in self.tickets)

    def calculate_total_discount_given(self) -> float:
        return sum(ticket.customer.discount for ticket in self.tickets if isinstance(ticket, VIPTicket) and ticket.customer.discount)

    def __str__(self):
        tickets_info = "\n".join(
            f"  Ticket ID: {ticket.ticket_id}, Price: {ticket.calculate_price()}" for ticket in self.tickets)
        return (f"    - Show ID: {self.show_id}\n"
                f"    - Show Name: {self.show_name}\n"
                f"    - Show Date: {self.show_date}\n"
                f"    - Number of Tickets: {len(self.tickets)}\n"
                f"    - Revenue: ${self.calculate_revenue():.2f}\n"
                f"    - Total Discount Given: ${self.calculate_total_discount_given():.2f}\n"
                f"    - Tickets:\n{tickets_info if tickets_info else '       - No tickets available.'}")
