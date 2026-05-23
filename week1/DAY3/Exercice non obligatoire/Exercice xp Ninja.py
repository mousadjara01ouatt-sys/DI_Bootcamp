class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        message = f"{self.phone_number} called {other_phone.phone_number}"
        print(message)
        self.call_history.append(message)

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(message)
        other_phone.messages.append(message)
        print(f"Message sent from {self.phone_number} to {other_phone.phone_number}: {content}")

    def show_outgoing_messages(self):
        print("Outgoing messages:")
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(message)

    def show_incoming_messages(self):
        print("Incoming messages:")
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(message)

    def show_messages_from(self, other_phone):
        print(f"Messages from {other_phone.phone_number}:")
        for message in self.messages:
            if message["from"] == other_phone.phone_number:
                print(message)


# Test
phone1 = Phone("123-456-7890")
phone2 = Phone("098-765-4321")
phone3 = Phone("111-222-3333")

phone1.call(phone2)
phone1.call(phone3)
phone1.show_call_history()

phone1.send_message(phone2, "Hello!")
phone1.send_message(phone2, "How are you?")
phone3.send_message(phone1, "Hey!")

phone1.show_outgoing_messages()
phone1.show_incoming_messages()
phone1.show_messages_from(phone3)