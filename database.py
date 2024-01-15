class Database:
    def __init__(self):
        self.data = {}  # Dictionary to store key-value pairs
        self.transactions = []  # List to track transactions

    def execute_command(self, command):
        tokens = command.split()

        if tokens[0] == "SET":
            self.set(tokens[1], tokens[2])
        elif tokens[0] == "GET":
            self.get(tokens[1])
        elif tokens[0] == "DELETE":
            self.delete(tokens[1])
        elif tokens[0] == "COUNT":
            self.count(tokens[1])
        elif tokens[0] == "BEGIN":
            self.begin()
        elif tokens[0] == "ROLLBACK":
            self.rollback()
        elif tokens[0] == "COMMIT":
            self.commit()
        elif tokens[0] == "END":
            exit()

    def set(self, name, value):
        self.data[name] = value

    def get(self, name):
        print(self.data.get(name, "NULL"))

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def count(self, value):
        count = sum(1 for v in self.data.values() if v == value)
        print(count)

    def begin(self):
        self.transactions.append(dict(self.data))  # Create a snapshot of the current data

    def rollback(self):
        if not self.transactions:
            print("TRANSACTION NOT FOUND")
            return
        self.data = self.transactions.pop()

    def commit(self):
        self.transactions = []

if __name__ == "__main__":
    db = Database()

    while True:
        command = input().strip()
        db.execute_command(command)
