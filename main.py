import time
from models.intersection import Intersection
from simulation.traffic_generator import generate_traffic
from simulation.signal_controller import SignalController
from gui.visualize import TrafficVisualizer

def main():
    intersection = Intersection("I1")
    controller = SignalController(intersection)
    gui = TrafficVisualizer(intersection)

    for cycle in range(5):
        generate_traffic(intersection)

        selected_road, cleared = controller.run_cycle()

        gui.update(selected_road.road_id)

        print(f"\n--- Cycle {cycle + 1} ---")
        print(f"Green Signal: Road {selected_road.road_id}")
        print(f"Vehicles cleared: {cleared}")

        for r in intersection.get_roads():
            print(f"Road {r.road_id}: {r.vehicle_count()} vehicles")

        time.sleep(2)

    gui.root.mainloop()

if __name__ == "__main__":
    main()
