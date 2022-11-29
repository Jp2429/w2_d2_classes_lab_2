class BusStop:
    def __init__(self, name):
        self. name = name
        self.q_length = []
    
    def queue_length(self):
        return len(self.q_length)

    def add_to_queue(self, person):
        self.q_length.append(person)

    def clear(self):
        for person in self.q_length:
            self.q_length.pop()
            