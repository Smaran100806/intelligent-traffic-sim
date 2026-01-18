import tkinter as tk

class TrafficVisualizer:
    def __init__(self, intersection):
        self.intersection = intersection
        self.root = tk.Tk()
        self.root.title("Intelligent Traffic Signal Simulator")
        self.root.geometry("500x350")
        self.root.configure(bg="white")

        self.rows = {}
        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self.root,
            text="Intelligent Traffic Signal Simulator",
            font=("Arial", 16, "bold"),
            bg="white"
        )
        title.pack(pady=5)

        subtitle = tk.Label(
            self.root,
            text="Priority Queue Based Scheduling (Single Intersection)",
            font=("Arial", 10),
            bg="white"
        )
        subtitle.pack(pady=5)

        table = tk.Frame(self.root, bg="white")
        table.pack(pady=15)

        headers = ["Road", "Signal", "Vehicles"]
        for i, h in enumerate(headers):
            tk.Label(
                table,
                text=h,
                font=("Arial", 11, "bold"),
                width=12,
                bg="white"
            ).grid(row=0, column=i, padx=5, pady=5)

        for idx, road_id in enumerate(self.intersection.roads.keys(), start=1):
            tk.Label(
                table,
                text=f"Road {road_id}",
                font=("Arial", 11),
                width=12,
                bg="white"
            ).grid(row=idx, column=0, padx=5)

            signal = tk.Label(
                table,
                text="RED",
                fg="white",
                bg="red",
                width=12,
                font=("Arial", 10, "bold")
            )
            signal.grid(row=idx, column=1, padx=5)

            count = tk.Label(
                table,
                text="0",
                font=("Arial", 11),
                width=12,
                bg="white"
            )
            count.grid(row=idx, column=2, padx=5)

            self.rows[road_id] = (signal, count)

        self.status = tk.Label(
            self.root,
            text="Current Green Signal: None",
            font=("Arial", 12, "bold"),
            fg="green",
            bg="white"
        )
        self.status.pack(pady=10)

    def update(self, green_road_id):
        for road_id, road in self.intersection.roads.items():
            signal, count = self.rows[road_id]

            if road_id == green_road_id:
                signal.config(text="GREEN", bg="green")
            else:
                signal.config(text="RED", bg="red")

            count.config(text=str(road.vehicle_count()))

        self.status.config(text=f"Current Green Signal: Road {green_road_id}")
        self.root.update()
