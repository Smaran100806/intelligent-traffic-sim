import tkinter as tk

class TrafficVisualizer:
    def __init__(self, intersection):
        self.intersection = intersection
        self.root = tk.Tk()
        self.root.title("Intelligent Traffic Signal Simulator")

        self.lights = {}
        self.labels = {}

        self._build_ui()

    def _build_ui(self):
        self.root.geometry("500x500")

        title = tk.Label(
            self.root,
            text="Intelligent Traffic Signal Simulator",
            font=("Arial", 14, "bold")
        )
        title.pack(pady=10)

        canvas = tk.Canvas(self.root, width=400, height=400, bg="lightgrey")
        canvas.pack()

        # Draw intersection box
        canvas.create_rectangle(170, 170, 230, 230, fill="darkgrey")

        positions = {
            "A": (80, 190),   # Left
            "B": (190, 80),   # Top
            "C": (300, 190),  # Right
            "D": (190, 300)   # Bottom
        }

        for road_id, (x, y) in positions.items():
            light = tk.Label(
                self.root,
                text="🔴",
                font=("Arial", 24)
            )
            light.place(x=x, y=y)

            label = tk.Label(
                self.root,
                text=f"Road {road_id}: 0",
                font=("Arial", 10)
            )
            label.place(x=x - 20, y=y + 40)

            self.lights[road_id] = light
            self.labels[road_id] = label

        self.status = tk.Label(
            self.root,
            text="Current Green: None",
            font=("Arial", 12, "bold")
        )
        self.status.pack(pady=10)

    def update(self, green_road_id):
        for road_id, road in self.intersection.roads.items():
            if road_id == green_road_id:
                self.lights[road_id].config(text="🟢")
            else:
                self.lights[road_id].config(text="🔴")

            self.labels[road_id].config(
                text=f"Road {road_id}: {road.vehicle_count()}"
            )

        self.status.config(text=f"Current Green: Road {green_road_id}")
        self.root.update()
