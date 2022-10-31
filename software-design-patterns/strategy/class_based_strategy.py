import string
import random
from typing import List
from abc import ABC, abstractmethod


def generate_id(length=16):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        ...


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        return ticket_list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        ticket_list_copy = ticket_list.copy()
        ticket_list_copy.reverse()
        return ticket_list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        ticket_list_copy = ticket_list.copy()
        random.shuffle(ticket_list_copy)
        return ticket_list_copy


class BlackHoleStrategy(TicketOrderingStrategy):
    def create_ordering(self, ticket_list: List[SupportTicket]) -> List[SupportTicket]:
        return list()


class CustomerSupport:

    def __init__(self, processing_strategy: TicketOrderingStrategy):
        self.tickets = list()
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        # create the ordered list
        ticket_list = self.processing_strategy.create_ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("*************************************")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("*************************************")


# create the application
app = CustomerSupport(RandomOrderingStrategy())

# register a few tickets
app.create_ticket("Muhammad", "Make POC for AWS serverless archicture based Mobile App.")
app.create_ticket("Amir", "Write Authentication Rest Apis using FastApi, MongoDB.")
app.create_ticket("Muhammad Amir", "Integrate AWS Cognito with Rest Apis.")

# process the tickets
app.process_tickets()