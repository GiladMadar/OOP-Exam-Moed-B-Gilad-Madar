from Customer import Customer, CustomerType
from FoodVoucher import FoodVoucher
from Ticket import RegularTicket, VIPTicket
from Show import Show


def main():
    # Customers Tests
    print("\n*********** Start ****************")

    print("\nCustomers Tests:\n")
    regular_customer = Customer("C001", "John", "Doe", "john.doe@example.com", "123 Main St", CustomerType.REGULAR)
    vip_customer = Customer("C002", "Jane", "Smith", "jane.smith@example.com", "456 Oak St", CustomerType.VIP, discount=20.0)

    print(f"Regular Customer Info:\n{regular_customer}")
    print(f"\nVip Customer Info:\n{vip_customer}")

    # FoodVoucher and VIP Customer Tests
    print("\n*********************************")
    print("\nFoodVoucher and VIP Customer Tests:\n")
    voucher = FoodVoucher()
    vip_customer.take_food_voucher(voucher)
    vip_customer.eat()

    # Ticket Tests
    print("\n*********************************")
    print("\nTicket Tests:\n")
    regular_ticket = RegularTicket("T001", "Concert", "2024-09-01", 5, 10, regular_customer, 100.0)
    vip_ticket = VIPTicket("T002", "Concert", "2024-09-01", 1, 1, vip_customer, 150.0)
    print(f"Regular Ticket Info:\n{regular_ticket}")
    print(f"\nVIP Ticket Info:\n{vip_ticket}")

    # Show Tests
    print("\n*********************************")
    print("\nShow Tests:\n")
    show = Show("S001", "Concert", "2024-09-01")
    print(f"  Show Info:\n{show}")

    show.add_ticket(regular_ticket)
    show.add_ticket(vip_ticket)

    # Show.calculate Tests
    print("\n*********************************")
    print("\nShow.calculate Tests:\n")
    print(" - Total Revenue:", show.calculate_revenue())
    print(" - Total Discount Given:", show.calculate_total_discount_given())

    print("\n*********** End ****************")


if __name__ == "__main__":
    main()
