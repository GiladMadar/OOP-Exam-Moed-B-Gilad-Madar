from enum import Enum


class CustomerType(Enum):
    REGULAR = "REGULAR"
    VIP = "VIP"


class Customer:
    #   Constructor
    def __init__(self, customer_id: str, first_name: str, last_name: str, email: str, address: str, customer_type: CustomerType, discount: float = None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.customer_type = customer_type
        self.discount = discount
        self.food_voucher = None

    def take_food_voucher(self, food_voucher):
        self.food_voucher = food_voucher

    def eat(self):
        if self.food_voucher:
            self.food_voucher.eat()
        else:
            print("No food voucher available.")

    def __str__(self):
        discount_str = f"{self.discount:.2f}" if self.discount is not None else "None"
        return (f"  Customer Info:\n"
                f"      - Customer ID: {self.customer_id}\n"
                f"      - Name: {self.first_name} {self.last_name}\n"
                f"      - Email: {self.email}\n"
                f"      - Address: {self.address}\n"
                f"      - Customer Type: {self.customer_type}\n"
                f"      - Discount: {discount_str}\n"
                f"      - Food Voucher: {'Available' if self.food_voucher else 'Not Available'}")
