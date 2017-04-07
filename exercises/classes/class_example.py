class Customer:
    def __init__(self, fn, ln, acct):
        self.accountNumber = acct
        self.firstName = fn
        self.lastName = ln


class Bank:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.lastName = ""

        self.customers = set()

if __name__ == '__main__':
    # Create the bank
    FirstTennessee = Bank()

    # Create some customers
    steve = Customer("Steve", "Brownlee", "000000000")
    ryan = Customer("Ryan", "Tanay", "000000000")
    charisse = Customer("Charisse", "Lambert", "000000000")

    # Add the customers into the aggregate instance variable of the bank
    FirstTennessee.customers.add(steve)
    FirstTennessee.customers.add(ryan)
    FirstTennessee.customers.add(charisse)