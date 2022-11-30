class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.count_of_passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.count_of_passengers)
    
    def pick_up(self, person):
        self.count_of_passengers.append(person)

    def drop_off(self, person):
        self.count_of_passengers.remove(person)

    def empty(self):
        for person in self.count_of_passengers:
            self.count_of_passengers.clear()
        
    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.q_length:
            self.count_of_passengers.append(passenger)
        
        bus_stop.clear()
