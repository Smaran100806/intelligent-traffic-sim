from config import ALPHA, BETA, GAMMA

def calculate_priority(road):
    return (
        ALPHA * road.vehicle_count()
        + BETA * road.average_waiting_time()
        + GAMMA * road.red_cycles
    )
