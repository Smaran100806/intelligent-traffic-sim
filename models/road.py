from collections import deque

class Road:
    def __init__(self, road_id):
        self.road_id = road_id
        self.queue = deque()
        self.total_waiting_time = 0
        self.red_cycles = 0

    def add_vehicle(self, vehicle):
        self.queue.append(vehicle)

    def vehicle_count(self):
        return len(self.queue)

    def average_waiting_time(self):
        if self.vehicle_count() == 0:
            return 0
        return self.total_waiting_time / self.vehicle_count()
