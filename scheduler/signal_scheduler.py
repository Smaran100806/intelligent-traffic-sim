import heapq
from scheduler.priority_calc import calculate_priority

class SignalScheduler:
    def select_road(self, roads):
        heap = []

        for road in roads:
            priority = calculate_priority(road)
            heapq.heappush(heap, (-priority, road))

        _, selected_road = heapq.heappop(heap)
        return selected_road
