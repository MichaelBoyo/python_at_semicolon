

class Transaction:

    def __init__(self, transaction_type, amount: int, date, sender: str, receiver: str):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date
        self.sender = sender
        self.receiver = receiver

    def get_sender(self):
        return self.sender


    def get_receiver(self):
        return self.receiver

    def get_amount(self):
        return self.amount

    def get_transaction_type(self):
        return self.transaction_type

    def __str__(self):
        return """
        Transaction type: {}
        Amount: {}
        sender: {}
        receiver: {}
        date: {}""".format(self.get_transaction_type(),
                           self.get_amount(), self.get_sender(), self.get_receiver(), self.get_date())

    def get_date(self):
        return self.date
