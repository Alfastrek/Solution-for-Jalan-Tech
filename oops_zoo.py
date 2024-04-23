class Person:
    def __init__(self, age):
        self.age = age


class Guest(Person):
    pass


class Ticket:
    def __init__(self, guests):
        self.guests = guests

    def calculate_price(self):
        total_price = sum(self._get_price(guest.age) for guest in self.guests)
        return total_price

    def _get_price(self, age):
        if age <= 2:
            return 0
        elif age < 18:
            return 100
        elif age < 60:
            return 500
        else:
            return 300

    def display_ticket_details(self):
        ticket_details = "Ticket Details:\n"
        for i, guest in enumerate(self.guests, start=1):
            ticket_details += f"Guest {i} (age: {guest.age})\n"
        return ticket_details

def test_ticketing_software():
    ticket = Ticket([Guest(1)])
    assert ticket.calculate_price() == 0
    assert ticket.display_ticket_details() == "Ticket Details:\nGuest 1 (age: 1)\n"

    ticket = Ticket([Guest(10)])
    assert ticket.calculate_price() == 100
    assert ticket.display_ticket_details() == "Ticket Details:\nGuest 1 (age: 10)\n"

    ticket = Ticket([Guest(25)])
    assert ticket.calculate_price() == 500
    assert ticket.display_ticket_details() == "Ticket Details:\nGuest 1 (age: 25)\n"

    ticket = Ticket([Guest(70)])
    assert ticket.calculate_price() == 300
    assert ticket.display_ticket_details() == "Ticket Details:\nGuest 1 (age: 70)\n"

    ticket = Ticket([Guest(5), Guest(40)])
    assert ticket.calculate_price() == 600
    assert ticket.display_ticket_details() == "Ticket Details:\nGuest 1 (age: 5)\nGuest 2 (age: 40)\n"

    ticket = Ticket([Guest(30), Guest(12), Guest(55)])
    assert ticket.calculate_price() == 1100
    assert ticket.display_ticket_details() == "Ticket Details:\nGuest 1 (age: 30)\nGuest 2 (age: 12)\nGuest 3 (age: 55)\n"

    print("All test cases passed!")


def main():
    test_ticketing_software()

if __name__ == "__main__":
    main()
