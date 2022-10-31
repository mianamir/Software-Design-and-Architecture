import string
import random
from typing import List


def generate_id(length=16):
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:

    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class CustomerSupport:

    def __init__(self, processing_strategy: str = "fifo"):
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        # if it's empty, don't do anything
        if len(self.tickets) == 0:
            print("There are no tickets to process. Keep it up my support tickets team!")
            return

        if self.processing_strategy == "fifo":
            for ticket in self.tickets:
                self.process_ticket(ticket)
        elif self.processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                self.process_ticket(ticket)
        elif self.processing_strategy == "random":
            list_copy = self.tickets.copy()
            random.shuffle(list_copy)
            for ticket in list_copy:
                self.process_ticket(ticket)

    def process_ticket(self, ticket: SupportTicket):
        print("*************************************")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("*************************************")


# create the application
app = CustomerSupport("filo")

# register a few tickets
app.create_ticket("Muhammad", "Make POC for AWS serverless archicture based Mobile App.")
app.create_ticket("Amir", "Write Authentication Rest Apis using FastApi, MongoDB.")
app.create_ticket("Muhammad Amir", "Integrate AWS Cognito with Rest Apis.")

# process the tickets
app.process_tickets()