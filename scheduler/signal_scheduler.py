from scheduler.signal_scheduler import SignalScheduler
from config import BASE_GREEN_TIME

class SignalController:
    def __init__(self, intersection):
        self.intersection = intersection
        self.scheduler = SignalScheduler()

        # Assumption: average time per car (seconds)
        self.time_per_car = 2  

    def run_cycle(self):
        # 1. Select road using priority queue
        selected = self.scheduler.select_road(
            self.intersection.get_roads()
        )

        # 2. Time-based green signal logic
        max_cars_passable = BASE_GREEN_TIME // self.time_per_car
        cleared = min(max_cars_passable, selected.vehicle_count())

        # 3. Clear vehicles
        for _ in range(cleared):
            selected.queue.popleft()

        # 4. Update starvation counters
        for road in self.intersection.get_roads():
            if road != selected:
                road.red_cycles += 1
            else:
                road.red_cycles = 0

        return selected, cleared
