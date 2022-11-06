import string
import random
from typing import List, Callable


def generate_id(length=16):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


def fifoOrdering(ticket_list: List[SupportTicket]) -> List[SupportTicket]:
    return ticket_list.copy()


def filoOrdering(ticket_list: List[SupportTicket]) -> List[SupportTicket]:
    ticket_list_copy = ticket_list.copy()
    ticket_list_copy.reverse()
    return ticket_list_copy


def randomOrdering(ticket_list: List[SupportTicket]) -> List[SupportTicket]:
    ticket_list_copy = ticket_list.copy()
    random.shuffle(ticket_list_copy)
    return ticket_list_copy


def blackHoleOrdering(ticket_list: List[SupportTicket]) -> List[SupportTicket]:
    return list()


class CustomerSupport:

    def __init__(self):
        self.tickets = list()

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self, ordering: Callable[[List[SupportTicket]], List[SupportTicket]]):
        ticket_list = ordering(self.tickets)

        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("*************************************")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("*************************************")


# create the application
app = CustomerSupport()

# register a few tickets
app.create_ticket("Muhammad", "Make POC for AWS serverless archicture based Mobile App.")
app.create_ticket("Amir", "Write Authentication Rest Apis using FastApi, MongoDB.")
app.create_ticket("Muhammad Amir", "Integrate AWS Cognito with Rest Apis.")

# process the tickets
app.process_tickets(fifoOrdering)