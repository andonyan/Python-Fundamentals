class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}')


emails = []
while True:
    tokens = input().split()
    if tokens[0] == 'Stop':
        break
    else:
        emails.append(Email(tokens[0], tokens[1], tokens[2]))

indices = list(map(int, input().split(', ')))
for i in indices:
    emails[i].send()
for item in emails:
    item.get_info()

