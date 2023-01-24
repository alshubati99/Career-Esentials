flips = [
    'heads',
    'tails',
    'heads',
]
print(flips.count('heads'))
print(flips.pop())

class Attendee:
    def __init__(self, name, tickets):
        self.name= name
        self.tickets= tickets
    def displayAttendee(self):
        print('Name: {}, Teickets: {}'.format(self.name, self.tickets))
    def addTicket(self):
        self.tickets +=1
        print('{} tickets increased to {}'.format(self.name, self.tickets))
attendee1 = Attendee('Khawlah', 7)
attendee2 = Attendee('Khalil', 9)
attendee1.displayAttendee()
attendee2.addTicket()
