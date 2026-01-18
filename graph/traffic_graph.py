class TrafficGraph:
    def __init__(self):
        self.graph = {}

    def add_intersection(self, intersection_id):
        self.graph[intersection_id] = []

    def connect(self, i1, i2):
        self.graph[i1].append(i2)
        self.graph[i2].append(i1)

    def display(self):
        print("\nTraffic Network (Graph Representation):")
        for node, neighbors in self.graph.items():
            print(f"Intersection {node} connected to: {', '.join(neighbors)}")
