import time

from models.intersection import Intersection
from simulation.traffic_generator import generate_traffic
from simulation.signal_controller import SignalController
from gui.visualize import TrafficVisualizer
from graph.traffic_graph import TrafficGraph


def main():
    # -------------------------------
    # Graph-based multi-intersection setup (design-level)
    # -------------------------------
    traffic_graph = TrafficGraph()
    traffic_graph.add_intersection("I1")
    traffic_graph.add_intersection("I2")
    traffic_graph.add_intersection("I3")

    traffic_graph.connect("I1", "I2")
    traffic_graph.connect("I1", "I3")

    traffic_graph.display()

    # -------------------------------
    # Single intersection simulation
    # -------------------------------
    intersection = Intersection("I1")
    controller = SignalController(intersection)
    gui = TrafficVisualizer(intersection)

    cycles = 5  # number of signal cycles to demonstrate

    for cycle in range(cycles):
        print(f"\n--- Cycle {cycle + 1} ---")

        # Simulate vehicle arrivals
        generate_traffic(intersection)

        # Run one signal scheduling cycle
        selected_road, cleared = controller.run_cycle()

        # Update GUI
        gui.update(selected_road.road_id)

        # Console output (demo-friendly)
        print(f"Green Signal: Road {selected_road.road_id}")
        print(f"Vehicles cleared: {cleared}")

        for road in intersection.get_roads():
            print(f"Road {road.road_id}: {road.vehicle_count()} vehicles")

        # Pause between cycles (visual clarity)
        time.sleep(2)

    # Keep GUI window open after simulation ends
    gui.root.mainloop()


if __name__ == "__main__":
    main()
